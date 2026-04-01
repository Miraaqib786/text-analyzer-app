#!/bin/bash
# Build Docker image
docker build -t text-analyzer:latest .

# Apply Kubernetes manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml

# Show status
kubectl get pods
kubectl get svc
kubectl get ingress