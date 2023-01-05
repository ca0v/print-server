import glob
import os
from time import sleep
from printer import print_file

import requests


def download_files():
    response = requests.get("http://127.0.0.1:8080/file")
    data = response.text
    if (data == "[]"):
        print("no files to download")
        return

    print(data)
    # strip the first and last character
    data = data[1:-1]
    # split the string into a list
    data = data.split(sep=", ")
    # remove the quotes from the list
    data = [x.strip('"') for x in data]
    data = [x.strip("'") for x in data]

    # download the files
    for count, file in enumerate(data):
        print(f"downloading {file}...")
        response = requests.get(f"http://127.0.0.1:8080/file/{file}")
        # safe the file
        fileName = f"download/{file}"
        with open(fileName, "wb") as f:
            print(f"writing {fileName}")
            f.write(response.content)
            count = count + 1


def remove_file(fileName):
    file = fileName.split("/")[-1]
    response = requests.delete(f"http://127.0.0.1:8080/file/{file}")
    if (response.ok == False):
        print(f"error deleting {file}")


def print_files():
    # get all files that start with temp*
    files = glob.glob("download/*")
    # print the files
    for file in files:
        print_file(file)
        # delete the file
        remove_file(file)


if __name__ == "__main__":
    while True:
        print("downloading files...")
        try:
            download_files()
            print_files()
            sleep(5)
        except Exception as e:
            print(e)
            sleep(30)
