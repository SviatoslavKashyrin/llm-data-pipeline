from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.extractions.schemas import ExtractionRequest, ExtractionResponse
from app.extractions.models import ExtractionTask


router = APIRouter(prefix="/api/v1/extractions", tags=["Extractions"])


@router.post("/", response_model=ExtractionResponse)
async def create_extraction_task(
        request: ExtractionRequest,
        session: AsyncSession = Depends(get_async_session)
):

    new_task = ExtractionTask(
        text=request.text,
        target_schema=request.target_schema
    )


    session.add(new_task)
    await session.commit()


    await session.refresh(new_task)


    return ExtractionResponse(
        task_id=new_task.id,
        status=new_task.status
    )