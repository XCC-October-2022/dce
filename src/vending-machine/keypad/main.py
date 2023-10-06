from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import resourcemanager_v3
import googleProvider
import requests
import azureProvider
from  provider import GCPConfig


class Data(BaseModel):
    project_id: str | None = None
    project_name: str | None = None
    parent_id: str | None = None

class DefaultConfig(BaseModel):
    provider_name: str 
    provider: GCPConfig

    

app = FastAPI()


@app.get("/")
def root():
    return {"message": "GOOOOD Afternoon Rick"}

@app.post("/new_project")
def create_project(data: Data):
    result = provider.create_project(
        project_id=data.project_id, 
        parent_id=data.parent_id
        )
    
    print(result)
    if result.state == resourcemanager_v3.Project.State.ACTIVE:
        data = {"project_id" : result.project_id, "project_name": result.name, "parent_id": result.parent, "state": result.state}
        res =requests.post(url="http://127.0.0.1:8000/add", json=data)
        print(res)

@app.post("/azure/new_project")
def create_project(data: Data):
    result = azure_provider.create_project(
        project_id=data.project_id, 
        parent_id=data.parent_id
        )
    
    print(result)
    if result.state == resourcemanager_v3.Project.State.ACTIVE:
        data = {"project_id" : result.project_id, "project_name": result.name, "parent_id": result.parent, "state": result.state}
        res =requests.post(url="http://127.0.0.1:8000/add", json=data)
        print(res)
    
@app.post("/gcp/delete_project")
def delete_project(data: Data):
    result = gcp_provider.delete_project(
        project_name=f"projects/{data.project_id}"
        )
    
    print(result)
    if result.state == resourcemanager_v3.Project.State.DELETE_REQUESTED:
        data = {"project_id" : result.project_id, "project_name": result.name, "parent_id": result.parent, "state": result.state}
        res =requests.post(url="http://127.0.0.1:8000/remove", json=data)
        print(res)

@app.post("/azure/delete_project")
def delete_project(data: Data):
    result = azure_provider.delete_project(
        project_name=f"projects/{data.project_id}"
        )
    
    print(result)
    if result.state == resourcemanager_v3.Project.State.DELETE_REQUESTED:
        data = {"project_id" : result.project_id, "project_name": result.name, "parent_id": result.parent, "state": result.state}
        res =requests.post(url="http://127.0.0.1:8000/remove", json=data)
        print(res)
        



