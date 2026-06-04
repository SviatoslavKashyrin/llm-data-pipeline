from pydantic import BaseModel, Field
from typing import Dict, Any

class ExtractionRequest(BaseModel):
    text: str = Field(..., description="Raw unstructured text for analysis")
    target_schema: Dict[str, Any] = Field(..., description="JSON schema defining what data to extract")

class ExtractionResponse(BaseModel):
    task_id: str
    status: str