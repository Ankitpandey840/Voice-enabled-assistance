"""
Text-to-Speech Module for VEA Voice Assistant
Gives your assistant a voice
"""

import pyttsx3

def speak_text(text):
    """Convert text to speech and play it"""
    if not text:
        return
    
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()
        
        # Configure voice settings
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            # Use female voice if available (index 1)
            engine.setProperty('voice', voices[1].id)
        
        # Set speaking rate and volume
        engine.setProperty('rate', 180)    # Speed of speech
        engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
        
        # Display and speak the text
        print(f" VEA: {text}")
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        print(f" TTS Error: {e}")

# Test function
if __name__ == "__main__":
    print(" Testing Text-to-Speech...")
    speak_text("Hello! I am VEA, your voice assistant. Text to speech is working perfectly!")
    speak_text("I can now speak back to you!")
