import edge_tts
import asyncio
import pygame
import time


async def text_to_speech(text):

    communicate = edge_tts.Communicate(text=text, voice="en-US-GuyNeural")

    await communicate.save("response.mp3")


def play_audio(file_path):

    pygame.mixer.init()

    pygame.mixer.music.load(file_path)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():

        time.sleep(0.1)


asyncio.run(text_to_speech("Hello. I am VIVA. Welcome to your interview."))

play_audio("response.mp3")
