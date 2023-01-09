import glob
import os
from time import sleep
from printer import print_file

import requests

# create a download folder if it doesn't exist
if not os.path.exists("download"):
    os.mkdir("download")

# create a printed folder if it doesn't exist
if not os.path.exists("printed"):
    os.mkdir("printed")
    os.mkdir("printed/download")

# read the server endpoint from the settings file
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
UPLOAD_URL = config.get("servers", "upload_url")


def download_files():
    response = requests.get(f"{UPLOAD_URL}/file")
    if (response.ok == False):
        print(f"error getting files: {response}")
        return
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
        response = requests.get(f"{UPLOAD_URL}/file/{file}")
        # save the file
        fileName = os.path.join("download", file)
        with open(fileName, "wb") as f:
            print(f"writing {fileName}")
            f.write(response.content)
            count = count + 1


def print_files():
    print("print_files")
    # get all files that start with temp*
    files = glob.glob(os.path.join("download", "*"))
    for file in files:
        print("printing file {file}")
        # rename and print the file
        filenameToPrint = os.path.join('printed', f'{file}.pdf')
        os.replace(file, filenameToPrint)
        print_file(filenameToPrint)

        # delete the file on server
        file = file.split("/")[-1].split("\\")[-1]  # windows using \
        response = requests.delete(f"{UPLOAD_URL}/file/{file}")
        if (response.ok == False):
            print(f"error deleting {file}: {response}")


if __name__ == "__main__":
    while True:
        # print current time
        import datetime
        print(datetime.datetime.now())
        print("downloading files...")
        try:
            download_files()
            print_files()
            sleep(15)
        except Exception as e:
            print(e)
            sleep(60)
