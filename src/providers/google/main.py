from common.models.project import Project, ProjectState
from common.models.provider import ProviderProjectResponse
from fastapi import FastAPI
from providers.google.backend import GCPProvider
from google.cloud import resourcemanager_v3

app = FastAPI()
backend = GCPProvider(control_plane_url='http://localhost:8000',
                      backend_url='http://localhost:8002')


@app.post("/create_project")
def create_project(provider_request: dict):
    if 'parent_id' not in provider_request or 'project_id' not in provider_request:
        return ProviderProjectResponse(project=None, state=ProjectState.ERROR)

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
