from typing import List
from common.models.database import DatabaseProjectResponse, DatabaseProviderListResponse, DatabaseProviderResponse
from common.models.project import Project, ProjectState
from common.models.provider import Provider, ProviderState
from fastapi import FastAPI
import redis
import json
from src.db.config import REDIS_HOSTNAME

app = FastAPI()
db = redis.Redis(host=REDIS_HOSTNAME)


@app.get("/")
def root():
    return {"message": "GOOOOD Afternoon Rick"}


@app.get("/project/list")
def project_list():
    # TODO: Add filters to have more specific queries
    return [Project(**json.loads(project)) for project in db.hvals("PROJECTS")]


@app.post("/project/add")
def project_add(data: dict):
    project = Project(**data)
    db.hset("PROJECTS", project.tag, project.model_dump_json())
    return DatabaseProjectResponse(project=project,state=ProjectState.ACTIVE)


@app.post("/project/remove")
def project_remove(data: dict):
    project = Project(**data)
    print(project)
    db.hdel("PROJECTS", project.tag)
    return DatabaseProjectResponse(project=project,state=ProjectState.DELETED)


@app.get("/provider/list")
def provider_list():
    return DatabaseProviderListResponse(provider_list=[Provider(**json.loads(provider)) for provider in db.hvals("PROVIDERS")])


@app.post("/provider/add")
def provider_add(data: dict):
    provider = Provider(**data)
    print(provider)
    res = db.hset("PROVIDERS", provider.name, provider.model_dump_json()) #TODO Check db possible errors
    return DatabaseProviderResponse(provider=provider, state=ProviderState.REGISTERED)


@app.post("/provider/remove")
def provider_remove(data: dict):
    provider = Provider(**data)
    res = db.hdel("PROVIDERS", provider.name)
    return DatabaseProviderResponse(provider=provider, state=ProviderState.UNREGISTERED)
