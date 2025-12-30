from temp import add


def test_add() -> None:
    # assert add(1, 2) == 3
    # given
    a, b = 1, 2

    # when
    result = add(a, b)

    # then
    assert result == 3
