from common.models.database import DatabaseProviderRequest
from common.models.provider import Provider
from google.cloud import resourcemanager_v3
from google.oauth2 import service_account
import requests


class GCPProvider():
    def __init__(self, control_plane_url: str, backend_url: str):
        provider = Provider(name='GCP',
                            create_url=f'{backend_url}/create_project',
                            delete_url=f'{backend_url}/delete_project')

        requests.post(f'{control_plane_url}/backend/register_provider',
                      json=DatabaseProviderRequest(provider=provider).model_dump())

    def create_project(project_id: str, parent_id: str):

        credentials = service_account.Credentials.from_service_account_file(
            'credentials.json')
        client = resourcemanager_v3.ProjectsClient(credentials=credentials)

        create_project_request = resourcemanager_v3.CreateProjectRequest(project={
            "project_id": project_id,
            "parent": parent_id,
        })

        operation = client.create_project(request=create_project_request)
        print(f"Created project: {operation.result()}")

        return operation.result()

    def delete_project(project_name: str):

        credentials = service_account.Credentials.from_service_account_file(
            'credentials.json')
        client = resourcemanager_v3.ProjectsClient(credentials=credentials)

        delete_project_request = resourcemanager_v3.DeleteProjectRequest(
            name=f"{project_name}")

        operation = client.delete_project(request=delete_project_request)
        print(f"Deleted project: {operation.result()}")

        return operation.result()
