
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
with sr.AudioFile('kid-saying-did-i-do-it-wrong.wav') as source:
    # Listen to the audio file and store in audio_text variable
    audio_text = r.listen(source)

    try:
        # Using Google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.UnknownValueError:
        print("Unknown error occurred")
