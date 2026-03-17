from __future__ import annotations

from pydantic import BaseModel, EmailStr, Field, field_validator


class TestEmailRequest(BaseModel):
    to_email: EmailStr | None = None


class TriggerResponse(BaseModel):
    message: str
    run_type: str


class RunNowRequest(BaseModel):
    keywords_list: list[list[str]] | None = Field(default=None)


class RunNowTaskStatus(BaseModel):
    task_id: str
    run_type: str
    status: str
    progress_stage: str
    progress_message: str
    result_message: str = ""
    error_message: str = ""
    created_at: str
    updated_at: str
    started_at: str = ""
    finished_at: str = ""


class RunNowSubmitResponse(BaseModel):
    message: str
    task: RunNowTaskStatus


class DispatchLogItem(BaseModel):
    id: int
    run_type: str
    status: str
    message: str
    created_at: str


class PaperRecordItem(BaseModel):
    id: int
    uid: str
    push_date: str
    title: str
    url: str
    venue: str
    publisher: str
    source: str
    published_date: str
    keywords: list[str]
    run_type: str
    created_at: str
