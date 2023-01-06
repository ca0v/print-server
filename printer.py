# print a file to the default printer

import os


def print_file(fileName):
    print(f"print_file: {fileName}")
    # move file to printing folder
    
    # cmd = (f"Get-Content -Path {fileName} | Out-Printer")

    # Start-Process -FilePath “c:\docstoprint\doc1.pdf” –Verb Print -PassThru | %{sleep 10;$_} | kill    
    cmd = (f"Start-Process -FilePath \"{fileName}\" -Verb Print -PassThru | %{{sleep 10;$_}} | kill")
    cmd = f'powershell.exe -Command "{cmd}"'
    print(cmd)

    # run the command on windows powershell
    os.system(cmd)
