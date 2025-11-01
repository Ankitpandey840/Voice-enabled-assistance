"""
Quick test to combine STT and TTS
"""

from stt_module import listen_and_convert
from tts_module import speak_text

def test_voice_loop():
    """Test one complete voice interaction"""
    speak_text("Hello! Say something and I will repeat it back to you.")
    
    # Listen for input
    user_input = listen_and_convert()
    
    if user_input:
        # Speak back what was heard
        response = f"You said: {user_input}"
        speak_text(response)
    else:
        speak_text("I didn't hear anything. Please try again.")

if __name__ == "__main__":
    test_voice_loop()
