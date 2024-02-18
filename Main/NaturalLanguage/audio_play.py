import pygame
import time

class AudioPlayer:
    def __init__(self, file_path):
        self.file_path = file_path
        pygame.mixer.init()

    def play(self):
        try:
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
        except pygame.error as e:
            print("Error playing audio:", e)

if __name__ == "__main__":
    media_file_path2 = 'recorded_audio.wav'
    player = AudioPlayer(media_file_path2)
    player.play()