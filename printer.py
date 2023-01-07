# print a file to the default printer

import os


def print_file(fileName):
    print(f"print_file: {fileName}")
    cmd = f'node print.js {fileName}'
    print(cmd)

    # run the command on windows powershell
    os.system(cmd)
