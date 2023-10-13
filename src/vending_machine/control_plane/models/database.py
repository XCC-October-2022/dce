from pydantic import BaseModel
import requests
from vending_machine.control_plane.models.project import ProjectState
from vending_machine.control_plane.models.provider import Provider, ProviderState

from vending_machine.db.main import Project


class DatabaseProviderRequest(BaseModel):
    provider: dict


class DatabaseProviderResponse(BaseModel):
    provider: Provider
    state: ProviderState


class DatabaseProjectRequest(BaseModel):
    project: dict


class DatabaseProjectResponse(BaseModel):
    project: Project
    state: ProjectState


class Database(BaseModel):
    def __init__(db_connection: str = "http://127.0.0.1:8001/"):
        db_connection = db_connection

    def get_provider_by_name(self, name: str) -> Provider:
        ...

    def register_provider(self, data: DatabaseProviderRequest) -> DatabaseProviderResponse:
        ...

    def unregister_provider(self, data: DatabaseProviderRequest) -> DatabaseProviderResponse:
        ...

    def store_project(self, data: DatabaseProjectRequest) -> DatabaseProjectResponse:
        res = requests.post(url=self.create_url, json=data.project)
        state = res  # TODO: active or error
        project = res  # TODO: convert response into project if state is active
        return DatabaseProjectResponse(project=project, state=state)

    def remove_project(self, data: DatabaseProjectRequest) -> DatabaseProjectResponse:
        res = requests.post(url=self.delete_url, json=data.project)
        state = res  # TODO: deleted or error
        project = res  # TODO: convert response into project if state is active
        return DatabaseProjectResponse(project=project, state=state)
