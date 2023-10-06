from google.cloud import resourcemanager_v3
from google.oauth2 import service_account


def create_project(project_id: str, parent_id: str):

    credentials = service_account.Credentials.from_service_account_file('credentials.json')
    client = resourcemanager_v3.ProjectsClient(credentials=credentials)

    create_project_request = resourcemanager_v3.CreateProjectRequest(project = {
        "project_id": project_id,
        "parent": parent_id,
    })

    operation = client.create_project(request=create_project_request)
    print(f"Created project: {operation.result()}")

    return operation.result()


def delete_project(project_name: str):

    credentials = service_account.Credentials.from_service_account_file('credentials.json')
    client = resourcemanager_v3.ProjectsClient(credentials=credentials)

    delete_project_request = resourcemanager_v3.DeleteProjectRequest(name=f"{project_name}" )

    operation = client.delete_project(request=delete_project_request)
    print(f"Deleted project: {operation.result()}")

    return operation.result()


if __name__ == '__main__':
    project_id = "my-medium-project-id"
    project_name = "projects/my-medium-project-id"
    parent_id = "folders/926442729531"

    create_project(project_id, parent_id)
    delete_project(project_name)
