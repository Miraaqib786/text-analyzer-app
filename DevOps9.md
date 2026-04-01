# DevOps Lab Experiment 9

## Title

Automated deployment and management of a Dockerized Flask application on Docker Desktop Kubernetes using Kubernetes manifest files

## Aim

To deploy and manage the Text Analyzer application in Docker Desktop Kubernetes using Kubernetes YAML manifest files instead of manual resource creation commands.

## Learning Outcomes

After completing this experiment, the student should be able to:

- understand the role of Kubernetes manifest files
- use `deployment.yaml`, `service.yaml`, and `ingress.yaml`
- deploy an application using `kubectl apply`
- inspect and manage the deployed application
- scale, restart, and delete resources using manifest-based workflow
- understand the difference between manual deployment and automated deployment

## Prerequisites

- Git installed
- Docker Desktop installed and running
- Kubernetes enabled in Docker Desktop
- `kubectl` available in terminal
- internet connection
- Docker image available on Docker Hub:

```text
miraaqib786/text-analyzer:latest
```

## Repository

Clone the project from:

```text
https://github.com/Miraaqib786/text-analyzer-app.git
```

## Theory

In Experiment 8, Kubernetes resources were created manually using commands such as `kubectl create deployment` and `kubectl expose deployment`.

In this experiment, the same process is automated using YAML manifest files. This approach is better because:

- it is repeatable
- it is easier to maintain
- it reduces command complexity
- it is closer to real DevOps and Infrastructure as Code practices

## Procedure

### Step 1. Clone the repository

```powershell
git clone https://github.com/Miraaqib786/text-analyzer-app.git
cd text-analyzer-app\text-analyzer
```

### Step 2. Verify Kubernetes is running

```powershell
kubectl config current-context
kubectl get nodes
```

Expected result:

- current context is usually `docker-desktop`
- at least one node should be visible

### Step 3. Verify the Kubernetes manifest files

The repository already contains the Kubernetes manifest files required for automated deployment:

- `k8s/deployment.yaml`
- `k8s/service.yaml`
- `k8s/ingress.yaml`

Verify:

```powershell
dir k8s
```

### Step 4. Apply the manifest files

Run:

```powershell
kubectl apply -f k8s\deployment.yaml
kubectl apply -f k8s\service.yaml
kubectl apply -f k8s\ingress.yaml
```

Expected result:

- Deployment created
- Service created
- Ingress created

### Step 5. Verify the resources

```powershell
kubectl get deployment
kubectl get pods
kubectl get svc
kubectl get ingress
kubectl get all
```

Expected result:

- Deployment named `text-analyzer`
- pods running
- Service named `text-analyzer-service`
- Ingress named `text-analyzer-ingress`

### Step 6. Access the application

Run:

```powershell
kubectl port-forward svc/text-analyzer-service 5000:80
```

Open:

```text
http://localhost:5000
```

Expected result:

- the Text Analyzer app opens in the browser

Optional Ingress-based access:

Add this line to the Windows hosts file:

```text
127.0.0.1 text-analyzer.local
```

Then open:

```text
http://text-analyzer.local
```

### Step 7. Inspect the Deployment

In another terminal:

```powershell
kubectl describe deployment text-analyzer
kubectl logs deployment/text-analyzer
```

### Step 8. Scale the Deployment

```powershell
kubectl scale deployment/text-analyzer --replicas=3
kubectl get pods
```

Expected result:

- three pods should be running

### Step 9. Restart the Deployment

```powershell
kubectl rollout restart deployment/text-analyzer
kubectl rollout status deployment/text-analyzer
```

### Step 10. View rollout history

```powershell
kubectl rollout history deployment/text-analyzer
```

### Step 11. Reapply the manifests

Run the same commands again:

```powershell
kubectl apply -f k8s\deployment.yaml
kubectl apply -f k8s\service.yaml
kubectl apply -f k8s\ingress.yaml
```

Observation:

- applying the same files again does not create duplicate resources
- Kubernetes updates the existing resources if needed

### Step 12. Delete the resources using manifest files

```powershell
kubectl delete -f k8s\ingress.yaml
kubectl delete -f k8s\service.yaml
kubectl delete -f k8s\deployment.yaml
```

Verify:

```powershell
kubectl get all
```

## Comparison with Experiment 8

### Manual deployment in Experiment 8

- resources were created using direct commands
- useful for learning the fundamentals

### Automated deployment in Experiment 9

- resources are described in YAML files
- deployment becomes repeatable and easier to manage
- better suited for real DevOps workflows

## Observations

Students should record:

- names of manifest files created
- number of replicas configured in `deployment.yaml`
- service port and target port
- ingress host name
- number of running pods after deployment
- number of running pods after scaling
- rollout history output

## Result

The Flask Text Analyzer application was successfully deployed and managed in Docker Desktop Kubernetes using Kubernetes manifest files, demonstrating a repeatable and automated deployment workflow.

## Troubleshooting

### `kubectl get nodes` fails

- Kubernetes is not enabled or not ready in Docker Desktop

### Pod shows `ImagePullBackOff`

- verify internet connection
- verify the image exists on Docker Hub:

```powershell
docker pull miraaqib786/text-analyzer:latest
```

### YAML file gives an error

- check indentation carefully
- YAML is whitespace sensitive

### Application does not open in browser

- ensure `kubectl port-forward` is running
- verify the Service:

```powershell
kubectl get svc
```

## Viva Questions

1. What is a Kubernetes manifest file?
2. Why is YAML used in Kubernetes?
3. What is the purpose of `deployment.yaml`?
4. What is the purpose of `service.yaml`?
5. What is the purpose of `ingress.yaml`?
6. How is Experiment 9 different from Experiment 8?
7. What are the advantages of automated deployment?
8. What does `kubectl apply` do?
9. Why is YAML-based deployment considered Infrastructure as Code?
