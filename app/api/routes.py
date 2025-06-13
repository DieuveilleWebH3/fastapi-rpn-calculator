from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from app.schemas.schemas import OperationRequest, OperationResponse
from app.services.services import compute_and_save, export_csv, get_operations_paginated
from app.db.database import get_db
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks

router = APIRouter()

@router.post("/calculate", response_model=OperationResponse, tags=["RPN Calculator"])
def calculate(op: OperationRequest, db: Session = Depends(get_db)):
    try:
        return compute_and_save(op.expression, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/export", response_class=FileResponse, tags=["RPN Calculator"])
def export(background_tasks: BackgroundTasks, db: Session = Depends(get_db)) -> FileResponse:
    return export_csv(db, background_tasks)

@router.get("/operations", tags=["RPN Calculator"])
def list_operations(skip: int = Query(0, ge=0), limit: int = Query(10, le=100), db: Session = Depends(get_db)):
    return get_operations_paginated(skip=skip, limit=limit, db=db)
