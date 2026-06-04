import asyncio
from app.celery_app import celery_app
from app.database import async_session_maker
from app.extractions.models import ExtractionTask


async def _process_task_async(task_id: str):
    async with async_session_maker() as session:
        task = await session.get(ExtractionTask, task_id)
        if not task:
            return f"Task {task_id} not found."
        task.status = "PROCESSING"
        await session.commit()


        await asyncio.sleep(5)


        task.result = {"mock_extracted_data": "success"}
        task.status = "COMPLETED"
        await session.commit()

        return f"Task {task_id} completed successfully."


@celery_app.task(name="app.extractions.tasks.process_extraction")
def process_extraction_task(task_id: str):
    return asyncio.run(_process_task_async(task_id))