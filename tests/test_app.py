from app import welcome


def test_welcome() -> None:
    assert welcome() == "Hello, world!"
