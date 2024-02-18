import librosa
import numpy as np

class FrequencyExtractor:
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def extract_frequencies(self):
        y, sr = librosa.load(self.audio_file)
        hop_length = int(sr * 1)  # Hop length corresponding to 1000 milliseconds
        frequencies = librosa.core.fft_frequencies(sr=sr)

        extracted_frequencies = []
        for i in range(0, len(y), hop_length):
            frame = y[i:i+hop_length]
            if len(frame) < hop_length:
                frame = np.pad(frame, (0, hop_length - len(frame)), mode='constant')
            stft = np.abs(librosa.stft(frame))
            extracted_frequencies.extend(frequencies)
        
        return extracted_frequencies    
    

# Example usage:
if __name__ == "__main__":
    audio_file = "test3.mp3"
    extractor = FrequencyExtractor(audio_file)
    extracted_frequencies = extractor.extract_frequencies()
    print("Extracted frequencies:", extracted_frequencies)
