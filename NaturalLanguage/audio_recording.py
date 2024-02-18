import pyaudio
import wave


class AudioRecording:
    def __init__(self, format=pyaudio.paInt16, channels=1, rate=44100, chunk=1024, record_seconds=None):
        self.FORMAT = format                       # Format of audio samples (16-bit signed integers)
        self.CHANNELS = channels                   # Number of audio channels (1 for mono, 2 for stereo)
        self.RATE = rate                           # Sample rate (samples per second)
        self.CHUNK = chunk                         # Number of frames per buffer
        self.RECORD_SECONDS = record_seconds       # Duration of recording in seconds


    def record(self, record_seconds):
        p = pyaudio.PyAudio()

        stream = p.open(format=self.FORMAT,
        channels=self.CHANNELS,
        rate=self.RATE,
        input=True,
        frames_per_buffer=self.CHUNK)

        print("Recording...")
        frames = []

        for _ in range(0, int(self.RATE / self.CHUNK * (record_seconds+1))):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("Recording finished.")

        stream.stop_stream()
        stream.close()

        WAVE_OUTPUT_FILENAME = "recorded_audio.mp3"

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        print("Recording saved as", WAVE_OUTPUT_FILENAME)

        p.terminate()

if __name__ == "__main__":
    audio_recording = AudioRecording()
    audio_recording.record(record_seconds=10)