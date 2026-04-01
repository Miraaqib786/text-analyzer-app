# Text Analyzer App

A simple **Flask-based Text Analyzer** web application that analyzes text input and provides live metrics such as:

- Character count  
- Word count  
- Sentence count  
- Paragraph count  
- Average word length  
- Top 5 most frequent words  

This project is **Dockerized** for easy deployment and can be deployed on **Kubernetes** clusters.
---
## **Project Structure**
text-analyzer/
│
├── app.py # Main Flask application
├── app/
│ └── analyzer.py # Text analysis logic
├── templates/
│ └── index.html # Frontend HTML
├── static/
│ └── style.css # CSS for styling
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image build file
└── .gitignore # Files to ignore in git
---
## **Live Demo**

> You can deploy this project locally or on Kubernetes using Docker Desktop.  

---

## **Prerequisites**

- Python 3.x  
- Docker Desktop (with Kubernetes enabled if using Kubernetes)  
- Git (for cloning the repository)

---

## **Installation / Running Locally**

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/text-analyzer.git
cd text-analyzer
Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
Run the Flask app:
python app.py
Open your browser at:
http://localhost:5000

# Docker Instructions
## Build the Docker image
docker build -t <your-dockerhub-username>/text-analyzer:latest .
## Run the Docker container locally
docker run -p 5000:5000 <your-dockerhub-username>/text-analyzer:latest
## Push Docker image to Docker Hub
docker login
docker push <your-dockerhub-username>/text-analyzer:latest

## pull the image directly:
docker pull <your-dockerhub-username>/text-analyzer:latest

# Kubernetes Deployment (Optional)

## deploy the app on Docker Desktop Kubernetes using the Docker Hub image.

1. Clone the repository and navigate to Kubernetes manifests folder:
git clone https://github.com/<your-username>/text-analyzer.git
cd text-analyzer/k8s

2. Apply manifests
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml

3. Access the App
## If using Ingress, add to /etc/hosts (or C:\Windows\System32\drivers\etc\hosts on Windows):
127.0.0.1 text-analyzer.local
Then open in browser:
http://text-analyzer.local

## Or use port-forward:
kubectl port-forward svc/text-analyzer-service 5000:80