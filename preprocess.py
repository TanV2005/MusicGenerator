# from music21 import converter, note, chord
# import glob

# def extract_notes(path):
#     notes = []
    
#     for file in glob.glob(path + "/*.mid"):
#         midi = converter.parse(file)
        
#         for element in midi.flat.notes:
#             if isinstance(element, note.Note):
#                 notes.append(str(element.pitch))
#             elif isinstance(element, chord.Chord):
#                 notes.append('.'.join(str(n) for n in element.normalOrder))
    
#     return notes




import warnings
warnings.filterwarnings("ignore")

import os
from music21 import converter, instrument, note, chord

def get_notes(midi_path):
    notes = []

    for file in os.listdir(midi_path):
        if file.endswith(".mid"):
            midi = converter.parse(os.path.join(midi_path, file))

            parts = instrument.partitionByInstrument(midi)
            notes_to_parse = parts.parts[0].recurse() if parts else midi.flat.notes

            for element in notes_to_parse:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

    return notes