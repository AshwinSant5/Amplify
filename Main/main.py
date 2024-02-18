# Import statements for files in the NaturalLanguage directory
from NaturalLanguage import audio_extraction
from NaturalLanguage import transciber
from NaturalLanguage import audio_play
from NaturalLanguage import audio_recording
import gui
import threading
import time
import pygame

def play_audio(file_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)  # Wait for a short time
    except pygame.error as e:
        print("Error playing audio:", e)

if __name__ == "__main__":
    #audio_recorder = audio_recording.AudioRecording()
    #audio_recorder.record(record_seconds=10)
    # Assume 'notes' and 'lyrics' are provided
    media_file_path = 'NaturalLanguage/test3.mp3'
    extractor = audio_extraction.NoteExtractor(media_file_path)
    notes = extractor.extract_notes()
    print("Extracted notes:\n", notes)

    transcriber = transciber.Transcriber()
    print('\nTranscription:')
    transcription_text = transcriber.transcribe_audio(media_file_path)
    print(transcription_text)

    # Start audio playback in a separate thread
    media_file_path2 = 'recorded_audio.wav'
    audio_thread = threading.Thread(target=play_audio, args=(media_file_path2,))
    audio_thread.start()

    # Show the GUI
    show_gui = gui.MusicDisplayGUI(notes, transcription_text)