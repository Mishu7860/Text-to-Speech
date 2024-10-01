from gtts import gTTS
import os

def text_to_speech(text):
    # Create an instance of gTTS
    tts = gTTS(text=text, lang='en')
    
    # Save the audio file
    filename = "output.mp3"
    tts.save(filename)
    
    # Play the audio file
    os.system(f"start {filename}")  # Use "start" on Windows or "open" on macOS

if __name__ == "__main__":
    # Take user input
    user_input = input("Enter the text you want to convert to speech: ")
    text_to_speech(user_input)
