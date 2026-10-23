from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("")
def list_items():
    # TODO: construct and call the application use case.
    raise HTTPException(status_code=501, detail="Implement the Task Management API feature")
