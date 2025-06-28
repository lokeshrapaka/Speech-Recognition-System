import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Path to audio file (change if needed)
audio_path = r"harvard.wav"

# Load the audio file
with sr.AudioFile(audio_path) as source:
    print("🎙️ Listening from file...")
    audio_data = recognizer.record(source)  # read the entire file

# Try to recognize the speech
try:
    text = recognizer.recognize_google(audio_data)
    print("\n📝 Transcribed Text:\n")
    print(text)

except sr.UnknownValueError:
    print("Speech was unclear, unable to transcribe.")
except sr.RequestError as e:
    print(f"Could not request results from Google API; {e}")
