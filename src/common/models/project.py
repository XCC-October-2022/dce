from enum import Enum
from pydantic import BaseModel
from uuid import uuid4


class ProjectState(Enum):
    ERROR = 0
    ACTIVE = 1
    DELETED = 2


class Project(BaseModel):
    tag: str = str(uuid4())
    project_id: str | None = None
    project_name: str | None = None
    parent_id: str | None = None
