from pro_filer.actions.main_actions import show_details  # NOQA
from unittest.mock import patch, Mock # NOQA
from datetime import date


MOCK_FILE_CONTEXT_NO_FILE = {
    "base_path": "/home/trybe/????"
}


def test_show_details(capsys, tmp_path):
    file = tmp_path / "test.py"
    file.touch()
    mock_context = {
        "base_path": str(file)
    }
    show_details(mock_context)
    captured = capsys.readouterr()
    current_date = date.today()
    assert captured.out == (
        f"File name: test.py\n"
        f"File size in bytes: 0\n"
        f"File type: file\n"
        f"File extension: .py\n"
        f"Last modified date: {current_date}\n"
    )


def test_show_details_no_extension(capsys, tmp_path):
    file = tmp_path / "test"
    file.touch()
    mock_context_no_extension = {
        "base_path": str(file)
    }
    show_details(mock_context_no_extension)
    captured = capsys.readouterr()
    current_date = date.today()
    assert captured.out == (
        f"File name: test\n"
        f"File size in bytes: 0\n"
        f"File type: file\n"
        f"File extension: [no extension]\n"
        f"Last modified date: {current_date}\n"
    )


def test_show_details_no_file(capsys):
    show_details(MOCK_FILE_CONTEXT_NO_FILE)
    captured = capsys.readouterr()
    assert captured.out == "File '????' does not exist\n"
