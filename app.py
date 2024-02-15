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

# @app.route("/generate", methods=('POST',))
# def generate():
#     stream2 = stream.Stream()
#     n3 = note.Note('D#5')  # octave values can be included in creation arguments
#     stream2.repeatAppend(n3, 4)
#     stream2.show()


app.run(host='0.0.0.0', port=5000)
