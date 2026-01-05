import random
from datetime import datetime

# 명시적으로 클래스를 가져오면 Mypy 에러 해결에 도움이 됩니다.
# 만약 그래도 에러가 난다면 뒤에 # type: ignore를 붙여주세요.
# 숫자로부터 짧은 고유 코드를 가져오는 라이브러리
from sqids import Sqids  # type: ignore[attr-defined]

# 인스턴스 변수명은 소문자로, 클래스와 구분되게 지어줍니다.
_sqids_instance = Sqids()


class SquidUtility:  # 클래스명을 더 명확하게 변경
    @classmethod
    def encode(cls, nums: list[int]) -> str:
        return _sqids_instance.encode(nums)


if __name__ == "__main__":
    now = datetime.now()
    # 인코딩할 숫자 리스트 생성
    data_to_encode = [
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second,
        now.microsecond,
        random.randint(1, 9),
    ]

    print(f"Generated ID: {SquidUtility.encode(data_to_encode)}")
