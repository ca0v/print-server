# a service that accepts a file upload and saves it to disk

import os
import sys
import time

# start a web service to listen on port 8080
# and accept a file upload
from flask import Flask, request

app = Flask(__name__)

# the upload page


@app.route('/')
def upload_form():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # get the uploaded file
        f = request.files['file']
        # confirm the file is a pdf
        if f.filename.split('.')[-1] != 'pdf':
            return 'file must be a pdf'
        # create a file name based on the time
        filename = str(int(time.time()))
        print(filename)
        # save the file
        f.save('./upload/' + filename)
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
