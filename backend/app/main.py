from fastapi import FastAPI

app = FastAPI(
    title="TestPilot AI",
    description="AI-Powered Software Testing & Quality Intelligence Platform",
    version="0.1.0",
)


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "ok",
        "service": "TestPilot AI",
    }