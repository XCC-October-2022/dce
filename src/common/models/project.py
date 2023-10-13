from enum import Enum
from pydantic import BaseModel


class ProjectState(Enum):
    ERROR = 0
    ACTIVE = 1
    DELETED = 2


class Project(BaseModel):
    project_id: str | None = None
    project_name: str | None = None
    parent_id: str | None = None

    def __hash__(self) -> int:
        return self.project_id.__hash__()
