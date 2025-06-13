from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.schemas import OperationRequest, OperationResponse
from app.services.services import compute_and_save
from app.db.database import get_db

router = APIRouter()

@router.post("/calculate", response_model=OperationResponse, tags=["RPN Calculator"])
def calculate(op: OperationRequest, db: Session = Depends(get_db)):
    try:
        return compute_and_save(op.expression, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))