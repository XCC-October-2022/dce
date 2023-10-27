from common.models.database import Database, DatabaseProjectRequest, DatabaseProjectResponse, DatabaseProviderListResponse, DatabaseProviderRequest, DatabaseProviderResponse
from common.models.provider import Provider
import requests
from control_plane.config import DATABASE_HOSTNAME


class DatabaseBackend():
    def __init__(self, database=Database(db_connection=f"http://{DATABASE_HOSTNAME}:8001")):
        self.database = database

    def get_provider_by_name(self, name: str) -> Provider | None:
        res: DatabaseProviderListResponse = DatabaseProviderListResponse(**(requests.get(url=f'{self.database.db_connection}/provider/list').json()))
        #TODO fix this
        print(res)
        filtered = next((provider for provider in res.provider_list if provider.name == name), None)
        return filtered

    def register_provider(self, data: DatabaseProviderRequest) -> DatabaseProviderResponse:
        res = requests.post(
            url=f'{self.database.db_connection}/provider/add', json=data.provider.model_dump())
        return res

    def deregister_provider(self, data: DatabaseProviderRequest) -> DatabaseProviderResponse:
        res = requests.post(
            url=f'{self.database.db_connection}/provider/remove', json=data.provider.model_dump())
        return res

    def store_project(self, data: DatabaseProjectRequest) -> DatabaseProjectResponse:
        res = requests.post(
            url=f'{self.database.db_connection}/project/add', json=data.project.model_dump())
        return res

    def remove_project(self, data: DatabaseProjectRequest) -> DatabaseProjectResponse:
        res = requests.post(
            url=f'{self.database.db_connection}/project/remove', json=data.project.model_dump())
        return res
