from common.models.database import Database, DatabaseProjectRequest, DatabaseProjectResponse, DatabaseProviderRequest, DatabaseProviderResponse
from common.models.provider import Provider
import requests


class DatabaseBackend():
    def __init__(self, database=Database(db_connection="http://127.0.0.1:8001/")):
        self.database = database

    def get_provider_by_name(self, name: str) -> Provider:
        ...

    def register_provider(self, data: DatabaseProviderRequest) -> DatabaseProviderResponse:
        ...

    def unregister_provider(self, data: DatabaseProviderRequest) -> DatabaseProviderResponse:
        ...

    def store_project(self, data: DatabaseProjectRequest) -> DatabaseProjectResponse:
        res = requests.post(url=f'{self.database.db_connection}/add', json=data.project)
        state = res  # TODO: active or error
        project = res  # TODO: convert response into project if state is active
        return DatabaseProjectResponse(project=project, state=state)

    def remove_project(self, data: DatabaseProjectRequest) -> DatabaseProjectResponse:
        res = requests.post(url=f'{self.database.db_connection}/remove', json=data.project)
        state = res  # TODO: deleted or error
        project = res  # TODO: convert response into project if state is active
        return DatabaseProjectResponse(project=project, state=state)
