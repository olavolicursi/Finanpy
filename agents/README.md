# Finanpy AI Agents

This directory contains the definitions for specialized AI agents designed to assist in the development of **Finanpy**. These agents are tailored to the specific stack (Django + TailwindCSS) and requirements of the project.

## Available Agents

### 1. [Backend Developer](backend_agent.md)

* **Specialty**: Python, Django, Database, Business Logic.
* **Use for**: Creating models, views, APIs, forms, and handling data processing.
* **Key Tool**: `context7` (Django Docs).

### 2. [Frontend Developer](frontend_agent.md)

* **Specialty**: HTML, Django Templates, TailwindCSS, UX/UI.
* **Use for**: Building interfaces, styling pages, implementing the Design System, and handling static files.
* **Key Tool**: `context7` (Tailwind Docs).

### 3. [QA / Tester](qa_agent.md)

* **Specialty**: End-to-End Testing, Validation, Bug Hunting.
* **Use for**: Verifying features, running tests, checking UI correctness, and ensuring quality.
* **Key Tool**: `playwright` (Browser Automation).

## How to Use

When assigning a task, select the agent most suited for the domain of the problem.

* **Coding a new feature?** Start with the **Backend Agent** to build the data structure, then switch to the **Frontend Agent** to build the UI.
* **Fixing a bug?** If it's a server error (500), use the **Backend Agent**. If it's a layout issue, use the **Frontend Agent**.
* **Finished a task?** Call the **QA Agent** to verify the implementation against the PRD requirements.
