# Text Analyzer

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
