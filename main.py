from fastapi import FastAPI
import googleProvider

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello"}

@app.post("/new_project")
def create_new_project():
    googleProvider.create_project()
