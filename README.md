# LovableClone

An AI-powered project builder that turns a simple natural language prompt into a working web application. LovableClone uses a multi-agent workflow planning, architecture, and coding  to generate frontend files such as HTML, CSS, and JavaScript inside a generated project folder.

## ✨ Features

- **Natural language input:** describe the app you want in plain English (e.g. *"Build a colorful TODO app"*)

- **Task breakdown:** automatically decomposes the request into structured implementation tasks

- **Multi-agent workflow:** planning, architecture, and coding agents collaborate to build the app

- **Automatic file generation:** creates and updates project files without manual coding

- **Working output:** produces a runnable web app inside the `generated_project` directory

## 🧠 How It Works

1. **Planning Agent:**  interprets the user's request and defines the app requirements

2. **Architecture Agent:**  structures the project, deciding what files and components are needed

3. **Coding Agent:**  writes the actual HTML, CSS, and JavaScript files

4. **Output:**  the finished app is saved to the `generated_project` directory, ready to run

## 🛠️ Tech Stack



- Python | Core application logic 

- LangChain | LLM orchestration 

- LangGraph | Multi-agent workflow graph 

- Groq | LLM inference 

- Pydantic | Data validation and structured outputs 

## 🚀 Getting Started

### Prerequisites

- Python 3.10+

- A Groq API key

### Installation

```bash

git clone https://github.com/Ahmedkhaledd1/LovableClone.git

cd LovableClone

pip install -r requirements.txt

```

### Configuration

Create a `.env` file in the project root and add your Groq API key:

```bash

GROQ_API_KEY=your_api_key_here

```

### Usage

```bash

python main.py

```

Then enter a prompt describing the app you want to build, for example:

```

Build a colorful TODO app
```

## 🎯 Purpose

This project is a lightweight prototype for exploring how AI agents can assist in software creation  by planning, coding, and organizing files automatically inspired by tools like Lovable and v0.

## 🗺️ Roadmap

- [ ] Support for backend/API generation

- [ ] Support for additional frameworks (React, Vue)

- [ ] Add User Interface

- [ ] Iterative prompt-based editing of existing projects

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.



