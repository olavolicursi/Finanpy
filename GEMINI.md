# Finanpy Context for Gemini

This file provides context for the Finanpy project, a Personal Finance Management System.

## Project Overview

**Finanpy** is a web-based application for managing personal finances. It allows users to control bank accounts, categorize transactions (incomes and expenses), and view financial dashboards.

*   **Status**: Active Development (Sprint 1 - Configuration & Authentication).
*   **Key Documentation**:
    *   `PRD.MD`: Product Requirements Document (detailed features, user stories, schema).
    *   `docs/`: Contains architecture, database, design system, and setup guides.

## Architecture

The project follows a **Monolithic Django** architecture.

### Directory Structure
*   **`core/`**: Project settings, URLs, ASGI/WSGI configuration.
*   **`users/`**: Custom user model and authentication logic.
*   **`accounts/`**: Management of bank accounts.
*   **`categories/`**: Transaction categories (income/expense).
*   **`transactions/`**: Core transaction logic (recording incomes/expenses).
*   **`profiles/`**: User profiles (avatar, bio).
*   **`docs/`**: Project documentation.

### Tech Stack
*   **Backend**: Python 3.12+, Django 6.0.1.
*   **Database**: SQLite (default for dev), potentially PostgreSQL for prod.
*   **Frontend**: Django Template Language (DTL).
    *   *Planned*: TailwindCSS (currently being configured, see PRD).
*   **Authentication**: Django native auth with custom User model (email-based login).

## Development Setup

### 1. Environment
Ensure Python 3.12+ is installed.

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 2. Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database
```bash
python manage.py migrate
```

### 4. Running the Server
```bash
python manage.py runserver
```
Access at: `http://127.0.0.1:8000/`

## Coding Conventions

*   **Style**: Follow PEP8.
*   **Django**:
    *   Use Class-Based Views (CBVs) where possible.
    *   Keep logic in Models or Services/Managers, thin Views.
    *   Use `select_related` and `prefetch_related` for query optimization.
*   **Templates**: Located in `templates/` (root-level configured).
*   **Static**: Located in `static/`.

## Current Focus (from PRD)
*   Setting up TailwindCSS.
*   Implementing Custom User Model and Authentication Views.
*   Creating the base template structure.
