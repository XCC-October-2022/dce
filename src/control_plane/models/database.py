from functools import reduce
import inspect
from common.models.database import Database, DatabaseProjectRequest, DatabaseProjectResponse, DatabaseProviderRequest, DatabaseProviderResponse
from common.models.provider import Provider
import requests


class DatabaseBackend():
    def __init__(self, database=Database(db_connection="http://127.0.0.1:8001")):
        self.database = database

    def get_provider_by_name(self, name: str) -> Provider:
        res = requests.get(url=f'{self.database.db_connection}/provider/list')
        print(res)
        filtered = reduce(lambda x: x.name == name, res)
        print(filtered)
        return filtered

    def register_provider(self, data: DatabaseProviderRequest) -> DatabaseProviderResponse:
        res = requests.post(
            url=f'{self.database.db_connection}/provider/add', json=data.provider.model_dump())
        state = res  # TODO: active or error
        provider = res  # TODO: convert response into project if state is active
        return DatabaseProviderResponse(provider=provider, state=state)

    def deregister_provider(self, data: DatabaseProviderRequest) -> DatabaseProviderResponse:
        res = requests.post(
            url=f'{self.database.db_connection}/provider/remove', json=data.provider.model_dump())
        state = res  # TODO: active or error
        provider = res  # TODO: convert response into project if state is active
        return DatabaseProviderResponse(provider=provider, state=state)

    def store_project(self, data: DatabaseProjectRequest) -> DatabaseProjectResponse:
        res = requests.post(
            url=f'{self.database.db_connection}/project/add', json=data.project.model_dump())
        state = res  # TODO: active or error
        project = res  # TODO: convert response into project if state is active
        return DatabaseProjectResponse(project=project, state=state)

    def remove_project(self, data: DatabaseProjectRequest) -> DatabaseProjectResponse:
        res = requests.post(
            url=f'{self.database.db_connection}/project/remove', json=data.project.model_dump())
        state = res  # TODO: deleted or error
        project = res  # TODO: convert response into project if state is active
        return DatabaseProjectResponse(project=project, state=state)
