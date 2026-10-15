import pytest

from payments_data_harness import main


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    main()

    captured = capsys.readouterr()
    assert captured.out == "Hello from payments-data-harness!\n"
