from musicpy import *

notes = [
    "C5", "E5", "E5", "D5", "C5", "C5", "C5", "C5", "C5", "D5", "G4", "E5", "E5",
    "C5", "E5", "E5", "D5", "C5", "C5", "C5", "C5", "C5", "D5", "G4", "E5", "E5",
    "C5", "D5", "E5", "D5", "C5", "B4", "C5", "D5", "D5",
    "C5", "G5", "E5", "E5", "E5", "E5", "D5", "E5", "D5",
    "E5", "E5", "E5", "D5", "E5", "D5" 
]
duration = [
    1/8, 1/4, 1/4, 1/4, 1/2, 1/8, 1/8, 1/4, 1/8, 1/4, 1/2, 1/4, 1,
    1/8, 1/4, 1/4, 1/4, 1/2, 1/8, 1/8, 1/4, 1/8, 1/4, 1/2, 1/4, 1,
    1/3, 1/3, 1/4, 1/2, 1/2, 1/3, 1/3, 1/4, 1/3,
    1/8, 1/4, 1/2, 1/4, 1/4, 1/8, 1/8, 1/8, 2/3,
    1/4, 1/4, 1/8, 1/8, 1/8, 1/4,
]

notes_duration = zip(notes, duration)
tune = [chord(note, duration) for note, duration in notes_duration]
play(tune, bpm=180)
input("Please enter to exit")