# capstone

## Usage
### Run Control Plane
```uvicorn src.control_plane.main:app --port 8000```

### Run DB
```uvicorn src.db.main:app --port 8001```

### Run GCP Provider
```uvicorn src.providers.google.main:app --port 8002```