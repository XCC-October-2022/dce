from common.models.project import Project, ProjectState
from common.models.provider import Provider, ProviderState
from pydantic import BaseModel


class DatabaseProviderRequest(BaseModel):
    provider: Provider


class DatabaseProviderResponse(BaseModel):
    provider: Provider
    state: ProviderState


class DatabaseProjectRequest(BaseModel):
    project: Project


class DatabaseProjectResponse(BaseModel):
    project: Project
    state: ProjectState


class Database(BaseModel):
    db_connection: str
