from pydantic import BaseModel,Field,ConfigDict
from typing import Optional

class File(BaseModel):
    name: str = Field(..., description="The patjh of the file to be created or modified")
    purpose: str = Field(..., description="The purpose of the file")


class Plan(BaseModel):
    name: str = Field(..., description="Name of the project")
    description: str = Field(..., description="Description of the project")
    techstack: str = Field(..., description="Technology stack to be used")
    features: list[str] = Field(..., description="List of features to be implemented")
    files: list[File] = Field(..., description="List of files to be created")



class ImplementationTask(BaseModel):
    filepath: str = Field(description="The path to the file to be modified")
    task_description: str = Field(description="A detailed description of the task to be performed on the file, e.g. 'add user authentication', 'implement data processing logic', etc.")

class TaskPlan(BaseModel):
    implementation_steps: list[ImplementationTask] = Field(description="A list of steps to be taken to implement the task")
    model_config = ConfigDict(extra="allow")


    
class CoderState(BaseModel):
    task_plan: TaskPlan = Field(description="The plan for the task to be implemented")
    current_step_idx: int = Field(0, description="The index of the current step in the implementation steps")
    current_file_content: Optional[str] = Field(None, description="The content of the file currently being edited or created")