import json
from flask import Flask, request, Response
from flask_cors import CORS
from controller.controller import create_sheet_music

app = Flask(__name__)
CORS(app)


@app.route("/generate", methods=('POST',))
def generate():
    create_sheet_music(["C4", "D4", "E4", "F4", "G4", "A4", "B4"], "test_file")
    return "done"


app.run(host='0.0.0.0', port=5000)
