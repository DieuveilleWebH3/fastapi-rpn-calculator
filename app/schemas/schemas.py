from pydantic import BaseModel

class OperationRequest(BaseModel):
    expression: str

class OperationResponse(BaseModel):
    expression: str
    result: float
