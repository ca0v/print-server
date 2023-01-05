# print a file to the default printer

import os


def print_file(file_path):
    print(f"Get-Content -Path {file_path}.pdf | Out-Printer")
