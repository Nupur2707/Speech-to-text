import speech_recognition as sr
from pydub import AudioSegment

def convert_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="wav")

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
    return recognizer.recognize_google(audio_data)

input_audio_path = "C:\Users\nupur bhatkhande\Desktop\hac\squats-analysis"
converted_audio_path = "converted_audio.wav"
output_text_path = "transcription.txt"

convert_to_wav(input_audio_path, converted_audio_path)
transcription = transcribe_audio(converted_audio_path)

with open(output_text_path, "w") as file:
    file.write(transcription)
