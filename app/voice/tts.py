from faster_whisper import WhisperModel

model = WhisperModel("base", compute_type="int8")
import sounddevice as sd
from scipy.io.wavfile import write


def transcribe(audio_file):
    segments, _ = model.transcribe(audio_file)
    text = ""
    for segment in segments:
        text += segment.text
    return text.strip()


def record_audio(filename="input.wav", duration=10):
    fs = 16000
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    return filename


audio_file = record_audio()
text = transcribe(audio_file)
print(text)
