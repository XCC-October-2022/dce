from fastapi import FastAPI
from pydantic import BaseModel
import googleProvider

class Data(BaseModel):
    project_id: str | None = None
    project_name: str | None = None
    parent_id: str | None = None

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello"}

@app.post("/new_project")
def create_project(data: Data):
    googleProvider.create_project(
        project_id=data.project_id, 
        parent_id=data.parent_id
        )
    
@app.post("/delete_project")
def delete_project(data: Data):
    googleProvider.delete_project(
        project_name=data.project_name
        )
