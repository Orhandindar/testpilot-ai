from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models import Project, TestCase


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="TestPilot AI",
    description="AI-Powered Software Testing & Quality Intelligence Platform",
    version="0.1.0",
)


# =========================
# Pydantic Schemas
# =========================

class ProjectCreate(BaseModel):
    name: str
    description: str


class ProjectUpdate(BaseModel):
    name: str
    description: str


class TestCaseCreate(BaseModel):
    project_id: int
    title: str
    description: str
    test_type: str
    framework: str
    generated_code: str | None = None
    status: str = "draft"


class TestCaseUpdate(BaseModel):
    title: str
    description: str
    test_type: str
    framework: str
    generated_code: str | None = None
    status: str


# =========================
# Database
# =========================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# =========================
# Health
# =========================

@app.get("/api/v1/health")
def health_check():
    return {
        "status": "ok",
        "service": "TestPilot AI",
    }


# =========================
# PROJECTS
# =========================

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


@app.get("/api/v1/projects/{project_id}")
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        )

    return {
        "project": {
            "id": project.id,
            "name": project.name,
            "description": project.description,
        }
    }


@app.put("/api/v1/projects/{project_id}")
def update_project(
    project_id: int,
    project_data: ProjectUpdate,
    db: Session = Depends(get_db),
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        )

    project.name = project_data.name
    project.description = project_data.description

    db.commit()
    db.refresh(project)

    return {
        "message": "Project updated successfully.",
        "project": {
            "id": project.id,
            "name": project.name,
            "description": project.description,
        },
    }


@app.delete("/api/v1/projects/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        )

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully.",
    }


# =========================
# TEST CASES
# =========================

@app.post("/api/v1/test-cases")
def create_test_case(
    test_case: TestCaseCreate,
    db: Session = Depends(get_db),
):
    project = (
        db.query(Project)
        .filter(Project.id == test_case.project_id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        )

    new_test_case = TestCase(
        project_id=test_case.project_id,
        title=test_case.title,
        description=test_case.description,
        test_type=test_case.test_type,
        framework=test_case.framework,
        generated_code=test_case.generated_code,
        status=test_case.status,
    )

    db.add(new_test_case)
    db.commit()
    db.refresh(new_test_case)

    return {
        "message": "Test case created successfully.",
        "test_case": {
            "id": new_test_case.id,
            "project_id": new_test_case.project_id,
            "title": new_test_case.title,
            "description": new_test_case.description,
            "test_type": new_test_case.test_type,
            "framework": new_test_case.framework,
            "generated_code": new_test_case.generated_code,
            "status": new_test_case.status,
        },
    }


@app.get("/api/v1/test-cases")
def get_test_cases(db: Session = Depends(get_db)):
    test_cases = db.query(TestCase).all()

    return {
        "test_cases": [
            {
                "id": test_case.id,
                "project_id": test_case.project_id,
                "title": test_case.title,
                "description": test_case.description,
                "test_type": test_case.test_type,
                "framework": test_case.framework,
                "generated_code": test_case.generated_code,
                "status": test_case.status,
            }
            for test_case in test_cases
        ]
    }


@app.get("/api/v1/test-cases/{test_case_id}")
def get_test_case(
    test_case_id: int,
    db: Session = Depends(get_db),
):
    test_case = (
        db.query(TestCase)
        .filter(TestCase.id == test_case_id)
        .first()
    )

    if not test_case:
        raise HTTPException(
            status_code=404,
            detail="Test case not found.",
        )

    return {
        "test_case": {
            "id": test_case.id,
            "project_id": test_case.project_id,
            "title": test_case.title,
            "description": test_case.description,
            "test_type": test_case.test_type,
            "framework": test_case.framework,
            "generated_code": test_case.generated_code,
            "status": test_case.status,
        }
    }


@app.put("/api/v1/test-cases/{test_case_id}")
def update_test_case(
    test_case_id: int,
    test_case_data: TestCaseUpdate,
    db: Session = Depends(get_db),
):
    test_case = (
        db.query(TestCase)
        .filter(TestCase.id == test_case_id)
        .first()
    )

    if not test_case:
        raise HTTPException(
            status_code=404,
            detail="Test case not found.",
        )

    test_case.title = test_case_data.title
    test_case.description = test_case_data.description
    test_case.test_type = test_case_data.test_type
    test_case.framework = test_case_data.framework
    test_case.generated_code = test_case_data.generated_code
    test_case.status = test_case_data.status

    db.commit()
    db.refresh(test_case)

    return {
        "message": "Test case updated successfully.",
        "test_case": {
            "id": test_case.id,
            "project_id": test_case.project_id,
            "title": test_case.title,
            "description": test_case.description,
            "test_type": test_case.test_type,
            "framework": test_case.framework,
            "generated_code": test_case.generated_code,
            "status": test_case.status,
        },
    }


@app.delete("/api/v1/test-cases/{test_case_id}")
def delete_test_case(
    test_case_id: int,
    db: Session = Depends(get_db),
):
    test_case = (
        db.query(TestCase)
        .filter(TestCase.id == test_case_id)
        .first()
    )

    if not test_case:
        raise HTTPException(
            status_code=404,
            detail="Test case not found.",
        )

    db.delete(test_case)
    db.commit()

    return {
        "message": "Test case deleted successfully.",
    }