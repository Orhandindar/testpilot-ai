from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models import Project


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="TestPilot AI",
    description="AI-Powered Software Testing & Quality Intelligence Platform",
    version="0.1.0",
)


class ProjectCreate(BaseModel):
    name: str
    description: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "ok",
        "service": "TestPilot AI",
    }


@app.post("/api/v1/projects")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
):
    new_project = Project(
        name=project.name,
        description=project.description,
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {
        "message": "Project created successfully.",
        "project": {
            "id": new_project.id,
            "name": new_project.name,
            "description": new_project.description,
        },
    }
@app.get("/api/v1/projects")
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()

    return {
        "projects": [
            {
                "id": project.id,
                "name": project.name,
                "description": project.description,
            }
            for project in projects
        ]
    }