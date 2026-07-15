from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langgraph.graph import END, StateGraph,START
from dotenv import load_dotenv
from prompts import *
from states import *
from tools import *
import json

load_dotenv()








planner_llm = ChatGroq(model="openai/gpt-oss-120b")
coder_llm   = ChatGroq(model="openai/gpt-oss-120b")

coder_tools = [read_file, write_file, list_files, get_current_directory,run_cmd,list_files]

system_prompt = coder_system_prompt()
    
react_agent = create_agent(
    model=coder_llm,
    tools=coder_tools,
    system_prompt=system_prompt
)

def planner_agent(state: dict) -> dict:
    """Converts user prompt into a structured Plan."""
    user_prompt = state["user_prompt"]
    resp = planner_llm.with_structured_output(Plan).invoke(
        planner_prompt(user_prompt)
    )
    if resp is None:
        raise ValueError("Planner did not return a valid response.")
    return {"plan": resp}


def architect_agent(state: dict) -> dict:
    """Creates TaskPlan from Plan."""
    plan: Plan = state["plan"]
    resp = planner_llm.with_structured_output(TaskPlan).invoke(
        architect_prompt(plan=plan.model_dump_json())
    )
    if resp is None:
        raise ValueError("Planner did not return a valid response.")

    resp.plan = plan
    return {"task_plan": resp}


def coder_agent(state: dict) -> dict:
    """LangGraph tool-using coder agent."""
    coder_state: CoderState = state.get("coder_state")
    if coder_state is None:
        coder_state = CoderState(task_plan=state["task_plan"], current_step_idx=0)

    steps = coder_state.task_plan.implementation_steps
    if coder_state.current_step_idx >= len(steps):
        return {"coder_state": coder_state, "status": "DONE"}

    current_task = steps[coder_state.current_step_idx]
    existing_content = read_file.run(current_task.filepath)


    user_prompt = (
        f"Task: {current_task.task_description}\n"
        f"File: {current_task.filepath}\n"
        f"Existing content:\n{existing_content}\n"
        "Use write_file(path, content) to save your changes."
    )



    result = react_agent.invoke({
        "messages": [
            ("user", user_prompt)
        ]
    })
    coder_state.current_step_idx += 1
    return {"coder_state": coder_state}





graph = StateGraph(dict)
graph.add_node("Planner",planner_agent)
graph.add_edge(START, "Planner")
graph.add_node("Architect",architect_agent)
graph.add_edge("Planner", "Architect")
graph.add_node("Coder",coder_agent)
graph.add_edge("Architect", "Coder")
graph.add_conditional_edges(
    "Coder",
    lambda s: "END" if s.get("status") == "DONE" else "Coder",
    {"END": END, "Coder": "Coder"}
)


agent=graph.compile()

if __name__ == "__main__":
    result = agent.invoke({"user_prompt": "Build a simple Colorful TODO web application html css js"},
                        {"recursion_limit": 100})
    
    print("Final State:", result)