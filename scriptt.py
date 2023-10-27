import requests

# Define the URL and data to send
url = "http://localhost:8000/delete_project"
provider_name = "GCP"
provider_request = {
    "project_name": "projects/398145720123",
}

# Create a dictionary with the data to send in the request
data = {
    "provider_name": provider_name,
    "provider_request": provider_request
}

# Send the POST request
try:
    response = requests.post(url, json=data)

    # Check the response status code
    if response.status_code == 204:
        print("Request was successful.")
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
