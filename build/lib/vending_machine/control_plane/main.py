from fastapi import FastAPI

from vending_machine.control_plane.models.database import Database
from vending_machine.control_plane.models.project import ProjectState
from vending_machine.control_plane.models.provider import ProviderProjectRequest


app = FastAPI()
db = Database()


@app.get("/")
def root():
    return {"message": "GOOOOD Afternoon Rick"}


@app.post("/backend/register_provider")
def register_provdier():
    ...


@app.post("/backend/deregsiter_provider")
def deregister_provider():
    ...


@app.get("/list_providers")
def list_providers():
    ...


@app.get("/list_projects")
def list_projects():
    ...


@app.post("/create_project")
def create_project(data: ProviderProjectRequest):
    provider = db.get_provider_by_name(data.provider_name)

    result = provider.create_project(data.provider_request)

    print(result)
    if result.state == ProjectState.ACTIVE:
        res = db.store_project(result.project)
        print(res)


@app.post("/delete_project")
def delete_project(data: ProviderProjectRequest):
    provider = db.get_provider_by_name(data.provider_name)

    result = provider.delete_project(data.provider_request)

    print(result)
    if result.state == ProjectState.DELETED:
        res = db.remove_project(result.project)
        print(res)

