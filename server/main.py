import os
import json
import glob
from docx import Document
import docx2txt
from flask import Flask, redirect, url_for, jsonify
app = Flask(__name__)

UPLOAD_DIRECTORY = os.getcwd() + '/static'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.route('/')
def hello():
    return 'Welcome user'

@app.route('/name/<name>')
def name(name):
    return 'Hello %s' % name

@app.route('/admin/<name>')
def admin(name):
    return 'Hello Admin'

@app.route('/guest/<name>')
def guest(name):
    return 'Hello Guest'

@app.route('/user/<name>')
def user(name):
    if(name == 'admin'):
        return redirect(url_for('admin', name = name))
    else:
        return redirect(url_for('guest', name = name))

@app.route('/read')
def read_file():
    files = []
    docFiles = []
    wel_msg = ""

    os.chdir(UPLOAD_DIRECTORY)
    filesData = glob.glob("*.*")

    for filename in filesData:
        fileName, fileExt = os.path.splitext(filename)

        if(fileExt == '.txt'):
            with open(filename,"r") as f:
                wel_msg = f.read()
                # wel_msg = f.read().replace('\n', '') --> replacing /n(comes when file contains multiple lines)
                files.append(wel_msg)
        else:
            fileText = docx2txt.process(filename)
            docFiles.append(fileText)
    return jsonify(doc = docFiles, txt = files)

if(__name__) == '__main__':
    app.run()
