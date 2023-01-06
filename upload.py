# a service that accepts a file upload and saves it to disk

import os
import sys
import time

# start a web service to listen on port 8080
# and accept a file upload
from flask import Flask, request

app = Flask(__name__)

# the upload page


@app.route('/upload', methods=['GET', 'POST'])
def upload_form():
    # if the request is a post, then the user has submitted the form
    if request.method == 'POST':
        # get the uploaded file
        f = request.files['file']
        # confirm the file is a pdf
        if f.filename.split('.')[-1] != 'pdf':
            return 'file must be a pdf'
        # create a file name based on the time
        filename = str(int(time.time()))
        print(filename)
        # determine the file encoding
        if (f.content_type != 'application/pdf'):
            return 'file type must be a application/pdf'

        # save the file
        f.save('./upload/' + filename)
        return 'file uploaded successfully'
    # if the request is a get, then the user is requesting the form
    else:
        # set the content header
        with open('./wwwroot/upload.html', 'r') as f:
            return f.read()

# return list of all files in the upload directory


@app.route('/file', methods=['GET'])
def list_files():
    files = os.listdir('./upload')
    return str(files)

# return the contents of a file


@app.route('/file/<fileId>', methods=['GET', 'DELETE'])
def get_file(fileId):

    fileName = './upload/' + fileId

    # if the request is a delete, then the user is requesting to delete the file
    if request.method == 'DELETE':
        # delete the file
        os.remove(fileName)
        return 'file deleted successfully'

    # if the request is a get, then the user is requesting the file
    # open the file in binary mode
    # r=>readonly, b=>binary
    with open(fileName, 'rb') as f:
        # write file as part of response
        response = app.make_response(f.read())
        # decorate the response as application/pdf
        response.headers['Content-Type'] = 'application/pdf'
        return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
