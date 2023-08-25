import speech_recognition as sr

def recognize_speech(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Record the audio from the file

    try:
        # Use Google Web Speech API for recognition
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        return "Speech recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API; {e}"

if __name__ == "__main__":
    audio_file_path = "C:/Users/Admin/Downloads/yo.flac"  # Replace with the path to your audio file

    result = recognize_speech(audio_file_path)
    print("Transcription:", result)
