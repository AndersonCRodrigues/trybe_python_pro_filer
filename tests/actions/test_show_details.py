from pro_filer.actions.main_actions import show_details  # NOQA
import pytest
from unittest.mock import patch, Mock


class TestShowDetails:
    @pytest.mark.parametrize(
        "context, expected_output",
        [
            (
                {"base_path": "/home/trybe/????"},
                "File '????' does not exist\n"
            ),
            (
                {"base_path": "/home/trybe/Downloads/Trybe_logo.png"},
                [
                    "File name: Trybe_logo.png\n",
                    "File size in bytes: 100\n",
                    "File type: file\n",
                    "File extension: .png\n",
                    "Last modified date: 2019-05-21\n",
                ],
            ),
            (
                {"base_path": "/home/trybe/Downloads"},
                [
                    "File name: Downloads\n",
                    "File size in bytes: 500\n",
                    "File type: directory\n",
                    "File extension: [no extension]\n",
                    "Last modified date: 2019-05-21\n",
                ],
            ),
        ],
    )
    def test_show_details(
        self, capsys, context, expected_output
    ):
        mock_os_path_exists = Mock(
            return_value="????" not in context["base_path"])
        mock_os_path_getsize = Mock(
            return_value=500 if expected_output[0].startswith("File name")
            else 100)
        mock_os_path_isdir = Mock(
            return_value="directory" in expected_output[2])
        mock_os_path_splitext = Mock(
            return_value=("", ".png")
            if ".png" in expected_output[0] else ("", ""))
        mock_os_path_getmtime = Mock(
            return_value=1558447897.0442736)

        with patch("os.path.exists", mock_os_path_exists), \
             patch("os.path.getsize", mock_os_path_getsize), \
             patch("os.path.isdir", mock_os_path_isdir), \
             patch("os.path.splitext", mock_os_path_splitext), \
             patch("os.path.getmtime", mock_os_path_getmtime):

            show_details(context)
            captured = capsys.readouterr()

            if isinstance(expected_output, str):
                assert captured.out == expected_output
            else:
                for output in expected_output:
                    assert output in captured.out
