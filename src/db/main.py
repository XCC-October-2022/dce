from common.models.project import Project
from common.models.provider import Provider
from fastapi import FastAPI
import redis
import json

app = FastAPI()
db = redis.Redis()


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
    db.hset("PROJECTS", project.__hash__(), project.model_dump_json())


@app.post("/project/remove")
def project_remove(data: dict):
    project = Project(**data)
    db.hdel("PROJECTS", project.__hash__())


@app.get("/provider/list")
def provider_list():
    return [Provider(**json.loads(provider)) for provider in db.hvals("PROVIDERS")]


@app.post("/provider/add")
def provider_add(data: dict):
    provider = Provider(**data)
    print(provider)
    db.hset("PROVIDERS", provider.__hash__(), provider.model_dump_json())


@app.post("/provider/remove")
def provider_remove(data: dict):
    provider = Provider(**data)
    db.hdel("PROVIDERS", provider.__hash__())
