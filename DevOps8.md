# DevOps Lab Experiment 8

## Title

Manual deployment and management of a Dockerized Flask application on Docker Desktop Kubernetes

## Aim

To build a Docker image from source code, run the application locally in a container, enable Kubernetes in Docker Desktop, and manually deploy and manage the application in Kubernetes using `kubectl` commands.

## Learning Outcomes

After completing this experiment, the student should be able to:

- clone a project from GitHub
- build a Docker image from a `Dockerfile`
- run the container locally on `localhost`
- enable and verify Docker Desktop Kubernetes
- create a Kubernetes Deployment manually
- expose the Deployment as a Service
- access the application using port forwarding
- scale, restart, inspect, and delete Kubernetes resources

## Prerequisites

- Git installed
- Docker Desktop installed and running
- Kubernetes enabled in Docker Desktop
- `kubectl` available in terminal
- internet connection

## Repository

Clone the project from:

```text
https://github.com/Miraaqib786/text-analyzer-app.git
```

## Software Required

- Docker Desktop
- PowerShell or Docker Desktop terminal
- Web browser

## Project Overview

The project is a Flask-based Text Analyzer application. It accepts text input and shows:

- character count
- word count
- sentence count
- paragraph count
- average word length

In this experiment, the application will first be built as a Docker image and then deployed manually in Kubernetes.

## Procedure

### Step 1. Clone the repository

Open PowerShell and run:

```powershell
git clone https://github.com/Miraaqib786/text-analyzer-app.git
cd text-analyzer-app\text-analyzer
```

### Step 2. Verify the project files

```powershell
dir
```

You should see files and folders such as:

- `Dockerfile`
- `README.md`
- `requirements.txt`
- `run.py`
- `app`
- `templates`
- `static`

### Step 3. Build the Docker image

```powershell
docker build -t text-analyzer:latest .
```

### Step 4. Verify that the image was created

```powershell
docker images
```

Expected result:

- an image named `text-analyzer` with the tag `latest`

### Step 5. Run the container locally

```powershell
docker run -p 5000:5000 text-analyzer:latest
```

Open the browser and visit:

```text
http://localhost:5000
```

Expected result:

- the Text Analyzer application should open successfully

### Step 6. Stop the running container

Press:

```text
Ctrl + C
```

### Step 7. Enable Kubernetes in Docker Desktop

In Docker Desktop:

1. Open `Settings`
2. Go to `Kubernetes`
3. Enable `Kubernetes`
4. Click `Apply & Restart`
5. Wait until Kubernetes shows as running

### Step 8. Verify Kubernetes

Open a fresh PowerShell terminal and run:

```powershell
kubectl config get-contexts
kubectl config current-context
kubectl get nodes
```

Expected result:

- current context is usually `docker-desktop`
- at least one node should be listed

### Step 9. Create a Deployment manually

Run:

```powershell
kubectl create deployment text-analyzer --image=miraaqib786/text-analyzer:latest
```

Note:

- this experiment uses the Docker Hub image so the pod can pull the image reliably on each machine

### Step 10. Verify the Deployment

```powershell
kubectl get deployment
kubectl get pods
```

Expected result:

- one Deployment named `text-analyzer`
- one pod created and moving to `Running`

### Step 11. Expose the Deployment as a Service

```powershell
kubectl expose deployment text-analyzer --type=ClusterIP --port=80 --target-port=5000 --name=text-analyzer-service
```

Verify:

```powershell
kubectl get svc
```

Expected result:

- one Service named `text-analyzer-service`

### Step 12. Access the application through Kubernetes

Run:

```powershell
kubectl port-forward svc/text-analyzer-service 5000:80
```

Open in browser:

```text
http://localhost:5000
```

Keep the terminal open while testing the application.

### Step 13. Inspect Kubernetes resources

Open another terminal and run:

```powershell
kubectl get all
kubectl describe deployment text-analyzer
```

### Step 14. View logs

```powershell
kubectl logs deployment/text-analyzer
```

If needed:

```powershell
kubectl get pods
kubectl logs <pod-name>
```

### Step 15. Scale the Deployment

Scale up:

```powershell
kubectl scale deployment/text-analyzer --replicas=3
kubectl get pods
```

Scale down:

```powershell
kubectl scale deployment/text-analyzer --replicas=1
kubectl get pods
```

### Step 16. Restart the Deployment

```powershell
kubectl rollout restart deployment/text-analyzer
kubectl rollout status deployment/text-analyzer
```

### Step 17. View rollout history

```powershell
kubectl rollout history deployment/text-analyzer
```

### Step 18. Delete the resources

```powershell
kubectl delete service text-analyzer-service
kubectl delete deployment text-analyzer
```

Verify cleanup:

```powershell
kubectl get all
```

## Observations

Students should record:

- image name used for deployment
- current Kubernetes context
- number of pods before scaling
- number of pods after scaling
- service name
- rollout status
- log output summary

## Result

The Flask Text Analyzer application was successfully built as a Docker image, run locally, manually deployed to Docker Desktop Kubernetes, exposed through a Service, accessed in the browser, managed with `kubectl`, and removed successfully.

## Troubleshooting

### `docker build` fails

- make sure Docker Desktop is running
- make sure the command is run inside the project folder

### `kubectl` is not recognized

- use the Docker Desktop terminal or install `kubectl`

### `kubectl get nodes` fails

- Kubernetes is not enabled or not fully started

### Pod shows `ImagePullBackOff`

- verify the image name
- verify internet connection
- try:

```powershell
docker pull miraaqib786/text-analyzer:latest
```

### Browser does not open the app

- ensure `kubectl port-forward` is still running
- verify the service exists:

```powershell
kubectl get svc
```

## Viva Questions

1. What is the purpose of a `Dockerfile`?
2. What is the difference between a Docker image and a container?
3. What is a Kubernetes Deployment?
4. Why do we create a Service?
5. What is the use of `kubectl port-forward`?
6. What happens when a Deployment is scaled?
7. What is `kubectl rollout restart`?
8. What is the use of `kubectl logs`?

