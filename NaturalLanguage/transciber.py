from openai import OpenAI

#api_key = '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'
#model_id = 'whisper-1'

client = OpenAI(api_key = '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')

media_file_path = 'test3.mp3'
media_file = open(media_file_path, 'rb')

with open("test3.mp3", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
        )
    print(transcription.text)
