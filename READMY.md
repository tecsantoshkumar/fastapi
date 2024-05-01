## Install FastAPI and Uvicorn:

If you haven't already installed FastAPI and Uvicorn, you can do so using pip:

```
pip install fastapi uvicorn
```


## Create a FastAPI Application:

Create a new Python file (e.g., main.py) and define your FastAPI application:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Test": "Success"}

```
Run the FastAPI Application:
You can run the FastAPI application using the Uvicorn ASGI server. In the terminal, navigate to the directory containing your main.py file and run the following command:
bash

```
python -m uvicorn main:app --reload
```

This command tells Uvicorn to run the app object from the main module (defined in main.py). The --reload option enables auto-reloading, which automatically restarts the server when changes are detected in your code.

# Access Your FastAPI Application:
Once your FastAPI application is running, you can access it in your web browser or using a tool like curl. By default, FastAPI runs on http://127.0.0.1:8000. Open your web browser and navigate to http://127.0.0.1:8000 to see the "Hello World" message.


# Extend Your FastAPI Application:
You can extend your FastAPI application by adding more endpoints and defining more complex logic. FastAPI supports various features, such as request validation, dependency injection, and automatic documentation generation, which you can leverage to build powerful web APIs.


