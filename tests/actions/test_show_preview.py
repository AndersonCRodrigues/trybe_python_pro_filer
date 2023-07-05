from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview(capsys):
    test_cases = [
        {
            "context": {
                "all_files": [],
                "all_dirs": []
            },
            "expected_output": "Found 0 files and 0 directories\n"
        },
        {
            "context": {
                "all_files": ["src/__init__.py", "src/app.py",
                              "src/utils/__init__.py"],
                "all_dirs": ["src", "src/utils"]
            },
            "expected_output": (
                "Found 3 files and 2 directories\n"
                "First 5 files: ['src/__init__.py', 'src/app.py', "
                "'src/utils/__init__.py']\n"
                "First 5 directories: ['src', 'src/utils']\n"
            )
        },
        {
            "context": {
                "all_files": ["file1.txt", "file2.txt", "file3.txt",
                              "file4.txt", "file5.txt", "file6.txt"],
                "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5", "dir6"]
            },
            "expected_output": (
                "Found 6 files and 6 directories\n"
                "First 5 files: ['file1.txt', 'file2.txt', 'file3.txt', "
                "'file4.txt', 'file5.txt']\n"
                "First 5 directories: ['dir1', 'dir2', 'dir3', 'dir4', "
                "'dir5']\n"
            )
        }
    ]

    for case in test_cases:
        show_preview(case["context"])
        captured = capsys.readouterr()
        assert captured.out == case["expected_output"]
