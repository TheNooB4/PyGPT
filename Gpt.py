import time
import openai
import os
import requests
import json
import random
from pyfiglet import Figlet
from termcolor import colored, cprint
from colorama import init

init()

# Set up the OpenAI API credentials
openai.api_key = "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"

# Set up the figlet font style


# Define the main menu function
custom_fig = Figlet(font='graffiti')
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(custom_fig.renderText('ChatGpt'), color='cyan'))
    
    
    print(colored("="*60, "green"))
    print(colored("\nAuthor: TheNooB\nGithub: https://github.com/TheNooB4\nContact: +23350776941\nVersion: 0.1\n","magenta"))
    print(colored("="*60, "green"))
    time.sleep(1)
    
    
    print(colored("\n  1. Text to Image", "yellow"))
    print(colored("  2. Chat with AI", "yellow"))
    print(colored("  3. Exit", "red"))

    try:
        choice = int(input(colored("\n What would you like to do? ", "cyan")))
        if choice == 1:
            text_to_image()
            input("\n\n Press Enter to continue...")
            main_menu()
        elif choice == 2:
            chat_with_ai()
            input("\n\n Press Enter to continue...")
            main_menu()
        elif choice == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored(custom_fig.renderText('ChatGpt'), color='cyan'))
            print(colored("\n Thank you for using ChatGpt. Goodbye!\n\n", "yellow"))
        else:
            raise ValueError()
    except ValueError:
        print(colored("\n Please choose a valid option!", "red"))
        input("\n\n Press Enter to continue...")
        main_menu()

# Define the text to image function
def text_to_image():
    # Prompt user for text input
    text = input("\n Enter the text to generate an image from: ")

    # Prompt user for number of images to generate
    num_images = int(input("\n How many images do you want to generate? "))

    if num_images > 0:
        print("\n This may take a while depending on your network and internet so please wait...\n")

    for i in range(num_images):
        # Generate a random filename for each image
        filename = f"Gpt/result_{i+1}_{random.randint(1000,9999)}.jpg"

        # Use API to generate image
        response = openai.Image.create(
            prompt=text,
            n=1,
            size="1024x1024",
            model="image-alpha-001",
            response_format="url"
        )

        # Get the image url from the response
        image_url = response['data'][0]['url']

        # Download image and save to local storage
        response = requests.get(image_url)
        with open(f"/sdcard/{filename}", 'wb') as f:
            f.write(response.content)

        # Inform user of successful save location
        print(f"Image {i+1} saved as {filename} in /sdcard/Gpt directory.")


# Define the chat with AI function
def chat_with_ai():
    # Define the prompt that the chatbot will use to start the conversation
    prompt = "Hello, how can I help you today?"

    # Initialize the conversation history
    conversation_history = ""

    print("\n Start chatting with AI. Type 'exit', 'quit', or 'bye' to end the conversation.")

    # Start the main loop
    while True:
        try:
            # Get the user's input
            user_input = input(colored("\n\n You >>  ", "cyan"))
            if user_input == "":
                raise ValueError()

            # Add the user's input to the conversation history
            conversation_history += f"User: {user_input}\n"

            # Set up the OpenAI API request
            model_engine = "text-davinci-002" # Change this to the appropriate GPT-3 model for your use case
            prompt_with_history = f"{prompt}\n{conversation_history}\nAI:"

            response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt_with_history,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )

            # Get the AI's response
            ai_response = response.choices[0].text.strip()
            print(colored("\n AI: ", "green"), end="")
            for char in ai_response:
                typing_speed = 0.05 # Change this value to modify the typing speed
                time.sleep(typing_speed)
                print(char, end="", flush=True)


            # Add the AI's response to the conversation history
            conversation_history += f"AI: {ai_response}\n"

            if user_input.lower() in ["exit", "quit", "bye"]:
                # End the conversation if the user types one of these keywords
                break

        except ValueError:
            print(colored("\n Please enter a valid input!", "red"))

# Call the main menu function on startup
main_menu()
