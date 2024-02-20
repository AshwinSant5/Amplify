from openai import OpenAI

#model_id = 'whisper-1'

class Transcriber: 
    def __init__(self, api_key='API-KEY', model_id='whisper-1'):
        self.client = OpenAI(api_key=api_key)
        self.model_id = model_id
    
    def transcribe_audio(self, file_path):
        #client = OpenAI(api_key = '') #REPLACE API KEY WITH NEW ONE FROM OPENAI API WEBPAGE

        #media_file_path = file_path
        #media_file = open(media_file_path, 'rb')

        with open(file_path, "rb") as audio_file:
            transcription = self.client.audio.transcriptions.create(
                model=self.model_id, 
                file=audio_file
                )
            return(transcription.text)
        
if __name__ == "__main__":
    transcriber = Transcriber()

    media_file_path = 'recorded_audio.mp3'
    transcription_text = transcriber.transcribe_audio(media_file_path)
    print(transcription_text)