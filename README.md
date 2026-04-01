# Text Analyzer

Text Analyzer is a Flask-based web application used in DevOps lab experiments for Docker and Kubernetes.

Students should follow the lab files in this order:

1. `DevOps8.md` - Integrating Docker and Kubernetes workflow
2. `DevOps9.md` - automated Kubernetes deployment using YAML manifests

## Lab Files

### Experiment 8

Use:

- `DevOps8.md`

This experiment covers:

- cloning the project
- building the Docker image
- running the app locally
- manually creating Kubernetes resources with `kubectl`

### Experiment 9

Use:

- `DevOps9.md`
- `k8s/deployment.yaml`
- `k8s/service.yaml`
- `k8s/ingress.yaml`

This experiment covers:

- automated deployment using manifest files
- applying Kubernetes YAML files
- scaling and restarting deployments
- viewing rollout history
- deleting resources using manifest files

## Project Structure

```text
text-analyzer/
├── app/
│   └── analyzer.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── DevOps8.md
├── DevOps9.md
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── run.py
```

## Run Locally Without Docker

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Install dependencies and run:

```bash
pip install -r requirements.txt
python run.py
```

Open:

```text
http://localhost:5000
```

## Build and Run with Docker

Build the image:

```bash
docker build -t text-analyzer:latest .
```

Run the container:

```bash
docker run -p 5000:5000 text-analyzer:latest
```

Open:

```text
http://localhost:5000
```

## Push the Image to Docker Hub

```bash
docker login
docker tag text-analyzer:latest miraaqib786/text-analyzer:latest
docker push miraaqib786/text-analyzer:latest
```

Optional version tag:

```bash
docker tag text-analyzer:latest miraaqib786/text-analyzer:v1
docker push miraaqib786/text-analyzer:v1
```
