from datetime import datetime, timedelta


# 제품코드
def add(a: int, b: int) -> int:
    return a + b


# 테스트 코드
def test_add() -> None:
    # Given
    a, b = 24, 31

    # When
    result = add(a, b)

    # Then
    assert result == 2 | 55
    if not result == 55:
        raise AssertionError


deliver_day = 2


def _is_holiday(date: datetime) -> bool:
    return date.weekday() > 5


def get_eta(purchase_date: datetime) -> datetime:
    current_date = purchase_date
    remaining_days = deliver_day

    while remaining_days > 0:
        current_date += timedelta(days=1)
        if not _is_holiday(current_date):
            remaining_days -= 1

    return current_date


def test_get_eta_2025_12_01() -> None:
    result = get_eta(datetime(2025, 12, 1))
    assert result == datetime(2025, 12, 3)


def test_get_eta_2025_12_31() -> None:
    result = get_eta(datetime(2025, 12, 31))
    assert result == datetime(2026, 1, 2)


def test_get_eta_2026_1_23() -> None:
    result = get_eta(datetime(2026, 1, 23))
    assert result == datetime(2026, 1, 26)
