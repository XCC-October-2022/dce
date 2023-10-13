from enum import Enum
from common.models.project import Project, ProjectState
from pydantic import BaseModel


class ProviderState(Enum):
    ERROR = 0
    REGISTERED = 1
    UNREGISTERED = 2


class ProviderProjectRequest(BaseModel):
    provider_name: str | None = None
    provider_request: dict | None = None


class ProviderProjectResponse(BaseModel):
    project: Project | None = None
    state: ProjectState


class Provider(BaseModel):
    name: str
    create_url: str
    delete_url: str
