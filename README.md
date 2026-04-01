# Text Analyzer

## Project Structure

```text
text-analyzer/
├── app/
├── static/
├── templates/
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

## DevOps Lab Files

- `DevOps8.md` - Experiment 8 manual Kubernetes deployment lab
- `DevOps9.md` - Experiment 9 automated deployment lab using YAML manifests
- `k8s/deployment.yaml` - Deployment definition
- `k8s/service.yaml` - Service definition
- `k8s/ingress.yaml` - Ingress definition

## Run locally

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Install dependencies and start the app:

```bash
pip install -r requirements.txt
python run.py
```

Open:

```text
http://localhost:5000
```

## Build Docker image

```bash
docker build -t text-analyzer:latest .
```

## Run Docker image

```bash
docker run -p 5000:5000 text-analyzer:latest
```

Open:

```text
http://localhost:5000
```

## Push to Docker Hub

```bash
docker login
docker tag text-analyzer:latest miraaqib786/text-analyzer:latest
docker push miraaqib786/text-analyzer:latest
```

Optional versioned tag:

```bash
docker tag text-analyzer:latest miraaqib786/text-analyzer:v1
docker push miraaqib786/text-analyzer:v1
```
