from __future__ import annotations

from tortoise import Model, fields

from app.tortoise_models.base_model import BaseModel


class MeetingModel(BaseModel, Model):
    url_code = fields.CharField(max_length=255, unique=True)

    class Meta:
        table = "meetings"

    @classmethod
    async def create_meeting(cls, url_code: str) -> MeetingModel:
        return await cls.create(url_code=url_code)

    @classmethod  # 클래스 메서드임을 명시 (인스턴스 생성 없이 MeetingModel.get_by_url_code()로 호출 가능)
    async def get_by_url_code(cls, url_code: str) -> MeetingModel | None:
        # 1. cls(MeetingModel) 테이블에서 url_code 컬럼을 검색
        # 2. 결과가 있으면 해당 모델 객체를 반환, 없으면 None 반환
        # 3. 비동기 DB 조작이므로 await 사용
        return await cls.filter(url_code=url_code).get_or_none()
