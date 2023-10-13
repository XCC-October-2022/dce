from fastapi import FastAPI
from models.project import ProjectState
from models.provider import ProviderProjectRequest
from models.database import Database


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

# @app.post("/azure/new_project")
# def create_project(data: Data):
#     result = azure_provider.create_project(
#         project_id=data.project_id,
#         parent_id=data.parent_id
#     )

#     print(result)
#     if result.state == resourcemanager_v3.Project.State.ACTIVE:
#         data = {"project_id": result.project_id, "project_name": result.name,
#                 "parent_id": result.parent, "state": result.state}
#         res = requests.post(url="http://127.0.0.1:8000/add", json=data)
#         print(res)


# @app.post("/gcp/delete_project")
# def delete_project(data: Data):
#     result = gcp_provider.delete_project(
#         project_name=f"projects/{data.project_id}"
#     )

#     print(result)
#     if result.state == resourcemanager_v3.Project.State.DELETE_REQUESTED:
#         data = {"project_id": result.project_id, "project_name": result.name,
#                 "parent_id": result.parent, "state": result.state}
#         res = requests.post(url="http://127.0.0.1:8000/remove", json=data)
#         print(res)


# @app.post("/azure/delete_project")
# def delete_project(data: Data):
#     result = azure_provider.delete_project(
#         project_name=f"projects/{data.project_id}"
#     )

#     print(result)
#     if result.state == resourcemanager_v3.Project.State.DELETE_REQUESTED:
#         data = {"project_id": result.project_id, "project_name": result.name,
#                 "parent_id": result.parent, "state": result.state}
#         res = requests.post(url="http://127.0.0.1:8000/remove", json=data)
#         print(res)
