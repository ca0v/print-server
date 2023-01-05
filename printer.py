# print a file to the default printer

import os


def print_file(fileName):
    print(f"print_file: {fileName}")
    cmd = (f"Get-Content -Path {fileName} | Out-Printer")
    print(cmd)

    # run the command on windows powershell
    #os.system(f'powershell.exe -Command {cmd}')
    os.remove(fileName)
