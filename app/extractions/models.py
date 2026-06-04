import uuid
from datetime import datetime, UTC
from sqlalchemy import Column, String, DateTime, JSON
from app.database import Base

class ExtractionTask(Base):
    __tablename__ = "extraction_tasks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    text = Column(String, nullable=False)
    target_schema = Column(JSON, nullable=False)
    status = Column(String, default="PENDING", nullable=False)
    result = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC).replace(tzinfo=None))