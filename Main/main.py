# Import statements for files in the NaturalLanguage directory
from NaturalLanguage import audio_extraction
from NaturalLanguage import audio_recording
from NaturalLanguage import classify
from NaturalLanguage import transciber
from NaturalLanguage import audio_play

if __name__ == "__main__":
    audio_recorder = audio_recording.AudioRecording()
    audio_recorder.record(record_seconds=10)

    transcriber = transciber.Transcriber()
    media_file_path = 'recorded_audio.mp3'
    print('\nTranscription:')
    transcription_text = transcriber.transcribe_audio(media_file_path)
    print(transcription_text)

    media_file_path2 = 'recorded_audio.wav'
    player = audio_play.AudioPlayer(media_file_path2)
    player.play()