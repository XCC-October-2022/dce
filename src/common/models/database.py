import json
from common.models.project import Project, ProjectState
from common.models.provider import Provider, ProviderState
from pydantic import BaseModel
from typing import List


class DatabaseProviderRequest(BaseModel):
    provider: Provider


class DatabaseProviderResponse(BaseModel):
    provider: Provider
    state: ProviderState


class DatabaseProviderListRequest(BaseModel):
    provider_name: str

class DatabaseProviderListResponse(BaseModel):
    provider_list: List[Provider]

class DatabaseProjectRequest(BaseModel):
    project: Project


class DatabaseProjectResponse(BaseModel):
    project: Project
    state: ProjectState


class Database(BaseModel):
    db_connection: str
