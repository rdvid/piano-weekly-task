import os

from music21 import stream, note, environment

us = environment.UserSettings()
us['lilypondPath'] = os.environ.get('LILYPOND_PATH')

def create_sheet_music(notes, output_file):
    # Create a music stream
    song_notes = stream.Stream()

    # Add notes to the stream
    for n in notes:
        song_notes.append(note.Note(n))

    # Create a music score
    song_notes.write('musicxml', output_file + ".xml")

    return song_notes.show('musicxml.png')

    # converter = LilypondConverter()
    # converter.createPDF()

    print("Music sheet generated successfully!")
