
def google_speech_recog():
    import gtts
    from playsound import playsound

    #pip3 install gTTS pyttsx3 playsound

    import os
    import speech_recognition as sr
    # initialize the recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=25)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)

    # make request to google to get synthesis
    tts = gtts.gTTS(text)

def audio_speech_recognition():
    import speech_recognition as sr

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    audio_file = "test.wav"  # Replace with your file path
    with sr.AudioFile(audio_file) as source:
        # Adjust for ambient noise, if needed
        recognizer.adjust_for_ambient_noise(source)

        # Perform speech recognition
        try:
            audio_data = recognizer.record(source)
            # text = recognizer.recognize_google(audio_data)
            text = recognizer.recognize_sphinx(audio_data)
            print("Recognized text:", text)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

def mozilla_deepspeech():
    import deepspeech

    # Load DeepSpeech model
    model = deepspeech.Model('path/to/deepspeech-0.9.3-models.pbmm')
    model.enableExternalScorer('path/to/deepspeech-0.9.3-models.scorer')

    # Load audio data
    audio_file = open('test.wav', 'rb')
    audio_data = audio_file.read()

    # Perform speech recognition
    text = model.stt(audio_data)
    print("Mozilla DeepSpeech thinks you said: " + text)

    audio_file.close()

def vosk():
    from vosk import Model, KaldiRecognizer
    import wave

    # Load Vosk model
    model = Model('path/to/vosk-model-small-en-us-0.15')

    # Read audio file
    audio_file = wave.open('test.wav', 'rb')

    # Initialize recognizer
    recognizer = KaldiRecognizer(model, audio_file.getframerate())

    # Process audio
    recognizer.AcceptWaveform(audio_file.readframes(audio_file.getnframes()))

    # Get recognition result
    result = recognizer.FinalResult()
    print("Vosk thinks you said: " + result)


if __name__ == "__main__":
    # audio_speech_recognition()
    mozilla_deepspeech()