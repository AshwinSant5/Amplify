import math

class Classify:
    def __init__(self, notes=['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']):
        self.notes = notes

    def freq_to_note(self, freq):
        note_number = 12 * math.log2(freq / 440) + 49  
        note_number = round(note_number)
            
        note = (note_number - 1 ) % len(self.notes)
        note = self.notes[note]
        
        octave = (note_number + 8 ) // len(self.notes)
        
        return note, octave
    
if __name__ == "__main__":
    classifier = Classify()
    note, octave = classifier.freq_to_note(560)
    print(f"Note: {note}, Octave: {octave}")