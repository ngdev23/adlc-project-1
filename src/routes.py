from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1")

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/projects")
async def list_projects():
    return {"projects": [], "total": 0}

@router.post("/projects")
async def create_project(data: dict):
    return {"id": "new-uuid", "message": "Project created"}

@router.get("/projects/{project_id}")
async def get_project(project_id: str):
    raise HTTPException(status_code=404, detail="Not found")