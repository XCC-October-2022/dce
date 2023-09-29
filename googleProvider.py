
from google.cloud import resourcemanager_v3
from google.oauth2 import service_account


def create_project(project_id: str, project_name: str, parent_id: str):

    credentials = service_account.Credentials.from_service_account_file('dcevm-400513-952876057a88.json')
    client = resourcemanager_v3.ProjectsClient(credentials=credentials)

    create_project_request = resourcemanager_v3.CreateProjectRequest(project = {
        "project_id": project_id,
        "parent": parent_id,
    })

    response = client.create_project(request=create_project_request)
    print(f"Created project: {response.name}")

if __name__ == '__main__':
    project_id = "my-medium-project-id"
    project_name = "my-medium-project"
    parent_id = "folders/926442729531"

    create_project(project_id, project_name, parent_id)
