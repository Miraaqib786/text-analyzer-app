# Text Analyzer App

A lightweight Flask application that accepts user text, computes live readability metrics, and displays the results on a single page. The UI is bundled with the backend so you can run it locally, in Docker, or inside a Kubernetes cluster without extra glue.

## Table of contents
- [Features](#features)
- [Tech stack](#tech-stack)
- [Project structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Running locally](#running-locally)
- [Docker](#docker)
- [Kubernetes](#kubernetes)

## Features
- Counts characters, words, sentences, and paragraphs in real time
- Calculates average word length and highlights the top five most frequent words
- Slim Flask + Jinja frontend with a single form-based page
- Dockerized service and Kubernetes manifests for production-ready deployment

## Tech stack
- Python 3.x and Flask
- Jinja2 templates with static CSS layout
- Dockerfile + Docker Compose for container builds
- Kubernetes manifests under `k8s/` for deployment and ingress routing

## Project structure
```
text-analyzer/
├── app/
│   └── analyzer.py         # Text analysis helper functions
├── templates/
│   └── index.html         # Single-page UI
├── static/
│   └── style.css          # Styles for the frontend
├── k8s/                   # Kubernetes deployment/service/ingress
├── Dockerfile             # Build instructions for the Flask service
├── docker-compose.yaml    # Optional multi-service stack
├── requirements.txt       # Python dependencies
└── run.py                 # Flask entry point
```

## Prerequisites
- Python 3.9+ and `pip`
- Docker Desktop (enable Kubernetes if you plan to use the `k8s/` manifests)
- Git for cloning, if you are not copying locally

## Running locally
```
git clone https://github.com/<your-username>/text-analyzer.git
cd text-analyzer
python -m venv venv                    # create a virtual environment
# activate the venv
# on Linux/macOS:
source venv/bin/activate
# on Windows (PowerShell):
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```
Then open http://localhost:5000 in your browser.

## Docker
1. Build the image:
```
docker build -t <your-dockerhub-username>/text-analyzer:latest .
```
2. Run it locally:
```
docker run -p 5000:5000 <your-dockerhub-username>/text-analyzer:latest
```
3. Push it to Docker Hub:
```
docker login
docker push <your-dockerhub-username>/text-analyzer:latest
```
You can also pull the published image on any machine with:
```
docker pull <your-dockerhub-username>/text-analyzer:latest
```

## Kubernetes
1. Clone the repo (if needed) and apply the manifests in `k8s/`:
```
git clone https://github.com/<your-username>/text-analyzer.git
cd text-analyzer/k8s
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```
2. Access the service:
   - With ingress, add the following entry to your hosts file (`/etc/hosts` or `C:\Windows\System32\drivers\etc\hosts`):
     `127.0.0.1 text-analyzer.local`
     Then visit http://text-analyzer.local
   - Or use port forwarding:
```
kubectl port-forward svc/text-analyzer-service 5000:80
```

Feel free to customize the Docker image tag, Kubernetes resource names, or ingress host to suit your environment.
