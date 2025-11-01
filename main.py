"""
VEA Main Application - Voice-Enabled Assistant
Combines all modules for complete voice interaction
"""

from stt_module import listen_and_convert
from tts_module import speak_text
from src import get_smart_response


class VEAAssistant:
    def __init__(self):
        """Initialize VEA Assistant"""
        self.commands_processed = 0
        print(" VEA Voice Assistant Starting...")
    
    def start(self):
        """Start the main VEA conversation loop"""
        print("\n" + "="*50)
        print(" VEA - Voice-Enabled Assistant")
        print("="*50)
        print("Say 'hello' to start, 'help' for commands, or 'goodbye' to exit")
        
        # Welcome message
        welcome_msg = "Hello! I'm VEA, your voice assistant. How can I help you today?"
        speak_text(welcome_msg)
        
        # Main conversation loop
        try:
            self._conversation_loop()
        except KeyboardInterrupt:
            self._shutdown()
    
    def _conversation_loop(self):
        """Main conversation loop"""
        while True:
            print("\n" + "-"*30)
            
            # Get voice input
            command = listen_and_convert()
            
            if not command:
                # If no speech detected, continue listening
                continue
            
            self.commands_processed += 1
            
            # Check for exit commands
            if self._is_exit_command(command):
                self._shutdown()
                break
            
            # Get smart response
            response = get_smart_response(command)
            
            # Speak the response
            speak_text(response)
    
    def _is_exit_command(self, command):
        """Check if user wants to exit"""
        exit_words = ['goodbye', 'bye', 'exit', 'quit', 'stop', 'see you later']
        return any(word in command.lower() for word in exit_words)
    
    def _shutdown(self):
        """Graceful shutdown"""
        print(f"\n Session complete! Processed {self.commands_processed} commands.")
        goodbye_msg = f"Goodbye! I processed {self.commands_processed} commands today. Have a great day!"
        speak_text(goodbye_msg)
        print("\n VEA Assistant stopped.")

def main():
    """Main entry point"""
    try:
        assistant = VEAAssistant()
        assistant.start()
    except Exception as e:
        print(f" Error starting VEA: {e}")

if __name__ == "__main__":
    main()
