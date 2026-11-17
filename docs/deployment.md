# Production Deployment Guide

## Docker Compose Quickstart

1. Set your Gemini API key:
   ```bash
   export GEMINI_API_KEY="your-api-key"
   ```

2. Build and launch:
   ```bash
   docker compose up --build -d
   ```

3. Open your browser:
   Navigate to `http://localhost:8501`.

## Health Check
Verify the container status:
```bash
docker compose ps
curl http://localhost:8501/_stcore/health
```
