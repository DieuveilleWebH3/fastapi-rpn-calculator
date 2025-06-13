import os
from fastapi import BackgroundTasks
from sqlalchemy.orm import Session
import tempfile
from app.models.models import Operation
from app.core.rpn import rpn_calculator
from fastapi.responses import FileResponse
import csv

def compute_and_save(expr: str, db: Session) -> dict[str, str | float]:
    result = rpn_calculator(expr)
    op = Operation(expression=expr, result=result)
    db.add(op)
    db.commit()
    db.refresh(op)
    return {"expression": expr, "result": result}

def export_csv(db: Session, background_tasks: BackgroundTasks) -> FileResponse:
    ops = db.query(Operation).all()

    # Use tempfile to create a cross-platform temporary file
    with tempfile.NamedTemporaryFile(suffix=".csv", mode="w", newline="", delete=False) as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Expression", "Result"])
        for op in ops:
            writer.writerow([op.id, op.expression, op.result])  # type: ignore
        temp_path = f.name

    # Schedule the deletion of the temporary file after the response is sent
    background_tasks.add_task(os.remove, temp_path)

    return FileResponse(temp_path, filename="operations.csv")

def get_operations_paginated(skip: int, limit: int, db: Session) -> list[Operation]:
    return db.query(Operation).order_by(Operation.id).offset(skip).limit(limit).all()
