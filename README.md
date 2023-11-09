# Starlette One shot
Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.

Starlette One shot is an implementation of Starlette with CRUD operations for MongoDB.

Docs: https://www.starlette.io/
## Getting started

1. Clone this repository
    ```
    git clone https://gitlab.com/marteyhaw/starlette-one-shot.git
    ```
2. Create a python virtual environment
   ```
   python -m venv .venv
   ```
3. Install required packages
   ```
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. Run the application (dev)
   ```
   uvicorn main:app --reload --port 8000
   ```
