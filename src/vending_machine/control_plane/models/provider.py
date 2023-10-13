from enum import Enum
from pydantic import BaseModel
import requests
from vending_machine.control_plane.models.project import ProjectState


class ProviderState(Enum):
    ERROR = 0
    REGISTERED = 1
    UNREGISTERED = 2


class ProviderProjectRequest(BaseModel):
    provider_name: str | None = None
    provider_request: dict | None = None


class ProviderProjectResponse(BaseModel):
    project: dict
    state: ProjectState


class Provider(BaseModel):
    def __init__(create_url: str, delete_url: str):
        create_url = create_url
        delete_url = delete_url

    def create_project(self, data: ProviderProjectRequest) -> ProviderProjectResponse:
        res = requests.post(url=self.create_url, json=data.provider_request)
        state = res  # TODO: active or error
        project = res  # TODO: convert response into project if state is active
        return ProviderProjectResponse(project=project, state=state)

    def delete_project(self, data: ProviderProjectRequest) -> ProviderProjectResponse:
        res = requests.post(url=self.delete_url, json=data.provider_request)
        state = res  # TODO: deleted or error
        project = res  # TODO: convert response into project if state is active
        return ProviderProjectResponse(project=project, state=state)
