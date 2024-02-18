import librosa
import numpy as np

class NoteExtractor:
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def extract_notes(self):
        y, sr = librosa.load(self.audio_file)
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr, hop_length=100)  # Adjust hop_length for more frequent notes
        pitches = pitches[magnitudes > np.max(magnitudes) * 0.5]
        notes = [librosa.hz_to_note(pitch) for pitch in pitches]

        return notes

if __name__ == "__main__":
    audio_file = "recorded_audio.mp3"  # Replace with the path to your audio file
    extractor = NoteExtractor(audio_file)
    notes = extractor.extract_notes()
    print("Extracted notes:", notes)
