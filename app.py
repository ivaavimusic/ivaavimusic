from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

def recognize_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
        try:
            transcription = r.recognize_google(audio)
            return transcription
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return "Could not request results from Google Web Speech API; {0}".format(e)


@app.route('/', methods=['GET', 'POST'])
def index():
    transcription = None
    if request.method == 'POST':
        audio_file = request.files['audio_file']
        if audio_file:
            print("Received audio file:", audio_file.filename)
            transcription = recognize_audio(audio_file)
    return render_template('index.html', transcription=transcription)

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
