from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

DatasetLabel = Literal["fake", "real"]


class RawArticleRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(min_length=1)
    content: str = Field(min_length=1)
    label: str = Field(min_length=1)
    source: str | None = Field(default=None, min_length=1)
    url: HttpUrl | None = None


class ProcessedArticleRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str = Field(min_length=1)
    label: DatasetLabel
    source: str | None = Field(default=None, min_length=1)
    url: HttpUrl | None = None
