from google.cloud import resourcemanager_v3

def create_project():
    client = resourcemanager_v3.ProjectsClient()
    # Initialize request argument(s)
    request = resourcemanager_v3.CreateProjectRequest(
    )

    # Make the request
    operation = client.create_project(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

    