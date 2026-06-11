import pygame
import time


def play_audio(file_path):

    pygame.mixer.init()

    pygame.mixer.music.load(file_path)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():

        time.sleep(0.1)
