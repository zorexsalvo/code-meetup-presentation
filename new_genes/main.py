from musicpy import *

notes = [
    "C5", "E5", "E5", "D5", "C5", "C5", "C5", "C5", "C5", "D5", "G4", "E5", "E5",
    "C5", "E5", "E5", "D5", "C5", "C5", "C5", "C5", "C5", "D5", "G4", "E5", "E5",
]
duration = [
    1/8, 1/4, 1/4, 1/4, 1/2, 1/8, 1/8, 1/4, 1/8, 1/4, 1/2, 1/4, 1,
    1/8, 1/4, 1/4, 1/4, 1/2, 1/8, 1/8, 1/4, 1/8, 1/4, 1/2, 1/4, 1
]

notes_duration = zip(notes, duration)
tune = [chord(note, duration) for note, duration in notes_duration]
play(tune)