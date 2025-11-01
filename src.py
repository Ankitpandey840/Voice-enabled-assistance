"""
Smart Response Module for VEA Voice Assistant
Intelligent responses using Google Speech-to-Text (FREE) - NO API keys needed!
"""

import datetime
import random
import webbrowser
import re

def get_smart_response(user_input):
    """Generate intelligent responses based on user input"""
    
    if not user_input:
        return "I didn't catch that. Please try again."
    
    user_input = user_input.lower()
    
    # Greetings
    if any(word in user_input for word in ['hello', 'hi', 'hey']):
        return "Hello! I'm VEA, your voice assistant. How can I help you?"
    
    # Time queries
    if any(phrase in user_input for phrase in ['time', 'what time']):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    
    # Date queries
    if any(phrase in user_input for phrase in ['date', 'today']):
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}."
    
    # Math calculations
    if any(word in user_input for word in ['plus', 'add', 'minus', 'times', 'multiply']):
        return handle_math(user_input)
    
    # Web commands
    if 'open youtube' in user_input:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube for you!"
    
    # Assistant info
    if any(phrase in user_input for phrase in ['who are you', 'what are you']):
        return "I'm VEA, your Voice-Enabled Assistant built with Python and Google Speech recognition!"
    
    # Help
    if 'help' in user_input:
        return "I can tell time, do math, open websites, and chat with you. Just speak naturally!"
    
    # Jokes
    if 'joke' in user_input:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the Python programmer break up? Because they had tuple problems!"
        ]
        return random.choice(jokes)
    
    # Default friendly responses
    responses = [
        "That's interesting! What else would you like to know?",
        "I'm still learning! Try asking about time, math, or websites.",
        "Good question! I can help with time, calculations, or opening sites."
    ]
    return random.choice(responses)

def handle_math(user_input):
    """Handle basic math operations"""
    numbers = re.findall(r'\d+', user_input)
    
    if len(numbers) < 2:
        return "I need two numbers for math. Try 'what is 5 plus 3'."
    
    num1, num2 = int(numbers[0]), int(numbers[1])
    
    if 'plus' in user_input or 'add' in user_input:
        return f"{num1} plus {num2} equals {num1 + num2}."
    elif 'minus' in user_input:
        return f"{num1} minus {num2} equals {num1 - num2}."
    elif 'times' in user_input or 'multiply' in user_input:
        return f"{num1} times {num2} equals {num1 * num2}."
    
    return f"I can add, subtract, or multiply {num1} and {num2}."

# Test function
if __name__ == "__main__":
    print(" Testing Smart Responses...")
    
    tests = [
        "hello",
        "what time is it", 
        "what is 10 plus 5",
        "open youtube",
        "tell me a joke"
    ]
    
    for test in tests:
        print(f" User: {test}")
        print(f"VEA: {get_smart_response(test)}\n")
