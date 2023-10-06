from pydantic import BaseModel

class Project(BaseModel):
    project_id: str | None = None
    project_name: str | None = None
    parent_id: str | None = None