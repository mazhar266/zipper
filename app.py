import os
import hashlib
from flask import Flask, jsonify, request, send_from_directory

from config import SETTINGS

app = Flask(__name__)


# the root url containing app info
@app.route("/")
def info():
    return jsonify(SETTINGS["INFO"])


# this will zip the files given to it
@app.route("/api/v1/zip", methods=["GET", ])
def zip():
    # let it be empty
    zip_file_name = ""

    # parse the filenames and make a string
    for file_name in request.args.getlist("file"):
        zip_file_name = "{}#{}".format(
            zip_file_name,
            hashlib.md5(file_name.encode(
                "ascii",
                "ignore"
            )).hexdigest()
        )
    
    # now add ext and folder names
    zip_file_name = "{}/{}.{}".format(
        SETTINGS["ZIP_FOLDER"],
        zip_file_name,
        "zip"
    )

    # if there is already a zipped file
    if os.path.isfile(zip_file_name):
        # serve it
        return send_from_directory(SETTINGS["ZIP_FOLDER"], zip_file_name)

    # make the zip file and serve it
    files_cmd = ''
    # traverse the filenames one more time
    for file_name in request.args.getlist("file"):
        # first get the extension
        filename, file_extension = os.path.splitext(file_name)
        
        # save to the cache folder
        os.system("wget -P {}/{}{} {}".format(
            SETTINGS["CACHE_FOLDER"],
            hashlib.md5(file_name.encode(
                "ascii",
                "ignore"
            )).hexdigest(),
            file_extension,
            file_name
        ))

        # make the cmd
        files_cmd = '{} {}/{}{}'.format(
            files_cmd,
            SETTINGS["CACHE_FOLDER"],
            hashlib.md5(file_name.encode(
                "ascii",
                "ignore"
            )).hexdigest(),
            file_extension
        )
    
    # zip it now
    os.system("zip {} {}".format(
        zip_file_name,
        files_cmd
    ))
    
    # serve it now
    return send_from_directory(SETTINGS["ZIP_FOLDER"], zip_file_name)
