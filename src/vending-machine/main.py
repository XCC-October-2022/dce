from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import resourcemanager_v3
import googleProvider

class Data(BaseModel):
    project_id: str | None = None
    project_name: str | None = None
    parent_id: str | None = None

app = FastAPI()

projects = {}

@app.get("/")
def root():
    return {"message": "GOOOOD Afternoon Rick"}

@app.post("/new_project")
def create_project(data: Data):
    result = googleProvider.create_project(
        project_id=data.project_id, 
        parent_id=data.parent_id
        )
    
    print(result)
    if result.state == resourcemanager_v3.Project.State.ACTIVE:
        projects[f"{data.project_id}"] = resourcemanager_v3.Project.State.ACTIVE
    
    print(projects)
    
@app.post("/delete_project")
def delete_project(data: Data):
    result = googleProvider.delete_project(
        project_name=f"projects/{data.project_id}"
        )
    
    print(result)
    if result.state == resourcemanager_v3.Project.State.DELETE_REQUESTED:
        projects[f"{data.project_id}"] = resourcemanager_v3.Project.State.DELETE_REQUESTED

    print(projects)
