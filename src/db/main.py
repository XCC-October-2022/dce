from common.models.project import Project
from fastapi import FastAPI
import redis
import json

app = FastAPI()
db = redis.Redis()


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
