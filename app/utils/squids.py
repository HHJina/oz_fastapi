import random
from datetime import datetime

import sqids  # 숫자로부터 짧은 고유 코드를 생성하는 라이브러리

squid = sqids.Sqids()


class Squids:

    @classmethod
    def encode(cls, nums: list[int]) -> str:
        return squid.encode(nums)


if __name__ == "__main__":
    now = datetime.now()
    print(
        Squids.encode(
            [now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, random.randint(1, 9)]
        )
    )
