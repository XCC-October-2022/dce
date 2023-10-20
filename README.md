# capstone

## Usage
### Run Control Plane
```uvicorn src.control_plane.main:app --port 8000```

### Run DB
```uvicorn src.db.main:app --port 8001```

### Run GCP Provider
```uvicorn src.providers.google.main:app --port 8002```

### USAGE

 2019  http localhost:8000/create_project provider_name=GCP provider_request[project_id]=test-id-61 provider_request[parent_id]=folders/926442729531
 2020  http localhost:8001/provider/list
 2021  http localhost:8001/project/list
 2022* http localhost:8000/delete_project provider_request[project_name]=projects/32440684633
 2023  http localhost:8000/delete_project provider_name=GCP project_name=projects/32440684633
 2024  http localhost:8000/delete_project provider_name=GCP provider_request[project_name]=projects/32440684633
 2025  http localhost:8001/project/list
 2026  http localhost:8000/delete_project provider_name=GCP provider_request[project_name]=projects/32440684633
 2027  http localhost:8001/project/list
 2028  http localhost:8000/delete_project provider_name=GCP provider_request[project_name]=projects/1016285938541
 2029  http localhost:8001/project/list
 2030  http localhost:8000/create_project provider_name=GCP provider_request[project_id]=test-id-62 provider_request[parent_id]=folders/926442729531
 2031  http localhost:8001/project/list
 2032  http localhost:8000/delete_project provider_name=GCP provider_request[project_name]=projects/782301261586
 2033  http localhost:8001/project/list
 2034  http localhost:8001/provider/list
 2035  http localhost:8000/create_project provider_name=GCP provider_request[project_id]=test-id-63 provider_request[parent_id]=folders/926442729531
 2036  http localhost:8001/provider/list
 2037  http localhost:8001/project/list
 2038  http localhost:8000/delete_project provider_name=GCP provider_request[project_name]=projects/1037409640267
 2039  http localhost:8001/project/list