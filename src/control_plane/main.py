from common.models.database import DatabaseProviderRequest
from common.models.project import ProjectState
from common.models.provider import Provider, ProviderProjectRequest
from control_plane.backends.database import DatabaseBackend
from control_plane.backends.provider import ProviderBackend
from fastapi import FastAPI, Response

db = DatabaseBackend()
app = FastAPI()


@app.get("/")
def root():
    return {"message": "GOOOOD Afternoon Rick"}


@app.post("/backend/register_provider")
def register_provider(data: dict):
    print(data)
    req = DatabaseProviderRequest(**data)
    res = db.register_provider(req)
    print(res)


@app.post("/backend/deregister_provider")
def deregister_provider(data: dict):
    print(data)
    req = DatabaseProviderRequest(**data)
    res = db.deregister_provider(req)
    print(res)


@app.get("/list_providers")
def list_providers():
    ...


@app.get("/list_projects")
def list_projects():
    ...


@app.post("/create_project")
def create_project(data: dict):
    print(data)
    req = ProviderProjectRequest(**data)

    #TODO input validation

    provider: Provider = db.get_provider_by_name(req.provider_name)
    #print(provider)

    if not provider:
        raise Exception(f"Provider not registered with name {req.provider_name}") 

    backend = ProviderBackend(provider=provider)
    result = backend.create_project(data=req)

    #print(result)
    if result.state == ProjectState.ACTIVE:
        res = db.store_project(result)
        #print(res)


@app.post("/delete_project")
def delete_project(data: dict):
    print(data)
    req = ProviderProjectRequest(**data)

    #TODO input validation

    provider = db.get_provider_by_name(req.provider_name)
    #print(provider)

    if not provider:
        return Response(status_code=204)

    backend = ProviderBackend(provider=provider)
    result = backend.delete_project(data=req)

    #print(result)
    if result.state == ProjectState.DELETED:
        res = db.remove_project(result)
        #print(res)

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
