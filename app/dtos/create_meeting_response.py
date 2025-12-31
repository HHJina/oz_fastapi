from typing import Annotated # 부가설명을 추가하기 위해서

from pydantic import BaseModel, Field

from app.dtos.frozen_config import FROZEN_CONFIG


class CreateMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

    url_code: Annotated[str, Field(description="미팅 URL 코드. unqiue 합니다.")]
