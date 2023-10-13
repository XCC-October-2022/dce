from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import resourcemanager_v3
import redis
import json


class Project(BaseModel):
    project_id: str | None = None
    project_name: str | None = None
    parent_id: str | None = None
    state: resourcemanager_v3.Project.State | None = None

    def __hash__(self) -> int:
        return self.project_id.__hash__()


app = FastAPI()
db = redis.Redis()
projects = {}


@app.get("/")
def root():
    return {"message": "GOOOOD Afternoon Rick"}


@app.post("/add")
def add(project: Project):
    print(project)
    db.hset("PROJECTS", project.__hash__(), project.model_dump_json())


@app.post("/remove")
def remove(project: Project):
    db.hdel("PROJECTS", project.__hash__())


@app.get("/list")
def list():
    # TODO: Add filters to have more specific queries
    return [Project(**json.loads(project)) for project in db.hvals("PROJECTS")]
