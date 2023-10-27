from providers.google.config import CONTROL_PLANE_HOSTNAME,BACKEND_HOSTNAME
from common.models.project import Project, ProjectState
from common.models.provider import ProviderProjectResponse
from fastapi import FastAPI
from providers.google.backend import GCPProvider
from google.cloud import resourcemanager_v3
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    print("Deregistering provider")
    
    GCPProvider.exit(control_plane_url=f'http://{CONTROL_PLANE_HOSTNAME}:8000')
    print("Exiting...")


app = FastAPI(lifespan=lifespan)
backend = GCPProvider(control_plane_url=f'http://{CONTROL_PLANE_HOSTNAME}:8000',
                      backend_url=f'http://{BACKEND_HOSTNAME}:8002')


@app.post("/create_project")
def create_project(provider_request: dict):
    print(provider_request)

    if 'parent_id' not in provider_request or 'project_id' not in provider_request:
        return ProviderProjectResponse(project=None, state=ProjectState.ERROR)

    print(provider_request['parent_id'])
    print(provider_request['project_id'])

    result = backend.create_project(
        parent_id=provider_request['parent_id'],
        project_id=provider_request['project_id']
    )

    if result.state != resourcemanager_v3.Project.State.ACTIVE:
        return ProviderProjectResponse(project=None, state=ProjectState.ERROR)

    project = Project(project_id=result.project_id,
                      project_name=result.name, parent_id=result.parent)

    return ProviderProjectResponse(project=project, state=ProjectState.ACTIVE)


@app.post("/delete_project")
def delete_project(provider_request: dict):
    print(provider_request)

    if 'project_name' not in provider_request:
        return ProviderProjectResponse(project=None, state=ProjectState.ERROR)

    result = backend.delete_project(
        project_name=provider_request['project_name']
    )

    if result.state != resourcemanager_v3.Project.State.DELETE_REQUESTED:
        return ProviderProjectResponse(project=None, state=ProjectState.ERROR)

    project = Project(project_id=result.project_id,
                      project_name=result.name, parent_id=result.parent)

    return ProviderProjectResponse(project=project, state=ProjectState.DELETED)


if __name__ == '__main__':
    project_id = "my-medium-project-id"
    project_name = "projects/my-medium-project-id"
    parent_id = "folders/926442729531"

    create_project(project_id, parent_id)
    delete_project(project_name)
