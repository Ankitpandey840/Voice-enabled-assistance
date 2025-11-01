"""
Speech-to-Text Module for VEA Voice Assistant
Based on your working stt_test.py
"""

import speech_recognition as sr

def listen_and_convert():
    """Your working STT function - enhanced with better structure"""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print(" Say something...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # reduce background noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)  # uses Google Speech API
        print(f" You said: {text}")
        return text.lower()  # Convert to lowercase for easier processing
    except sr.UnknownValueError:
        print(" Could not understand audio")
        return None
    except sr.RequestError:
        print(" API unavailable")
        return None

# Test function
if __name__ == "__main__":
    result = listen_and_convert()
    if result:
        print(f"Captured text: '{result}'")
