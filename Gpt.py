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



ass = "\033[1;36;40m 1. Go to >> \033[1;31mhttps://platform.openai.com \033[1;36;40m<< and click on the sign up button. If you already have an account skip this option use temp mail\n"

asd = "\033[1;36;40m 2. After you login/signup go to >> \033[1;31mhttps://platform.openai.com/account/api-keys \033[1;36;40m<< and click on the create new secrete key button then paste it below.\n"

# Set up the OpenAI API credentials
os.system("clear")
Keys = 'chatgpt_config'

# create the config directory if it doesn't exist
if not os.path.exists(Keys):
    os.mkdir(Keys)

# check if the api key file exists
api_key_file = os.path.join(Keys, 'openai.api_key.txt')
if os.path.exists(api_key_file):
    # read the api key from the file
    with open(api_key_file, 'r') as f:
        openai.api_key = f.readline().strip()
else:
    print(colored("="*59, "green"))
    print(ass)
    print(asd)
    print(colored("="*59, "green"))
    openai.api_key = input("\n Provide your OpenAI API key: ")
    while True:
        if len(openai.api_key) != 51:
            print(colored("\n Oops!!! Invalid API key. Please provide a valid OpenAI API key.", "red"))
            openai.api_key = input("\n Provide your OpenAI API key: ")
        else:
            break

    with open(api_key_file, 'w') as f:
        f.write(openai.api_key)

# Define the main menu function
custom_fig = Figlet(font='graffiti')
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(custom_fig.renderText('   ChatGpt'), color='cyan'))    
    
    print(colored("="*59, "green"))
    print(colored("\nAuthor: TheNooB\nGithub: https://github.com/TheNooB4\nContact: +233500776941\nVersion: 0.1\n","magenta"))
    print(colored("="*59, "green"))
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
           # os.system('cls' if os.name == 'nt' else 'clear')
            print(colored(custom_fig.renderText('ChatGpt'), color='cyan'))
            print(colored("\n Thank you for using ChatGpt. Goodbye!\n\n", "yellow"))
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear') 
        else:
            raise ValueError()
    except ValueError:
        print(colored("\n Please choose a valid option!", "red"))
        input("\n\n Press Enter to continue...")
        main_menu()

# Define the text to image function
def text_to_image():
    # Prompt user for text input
    os.system("clear")
    print(colored("="*59, "green"))

    print("""\033[36m    
      _______        _   ___  _                 
     |__   __|      | | |__ \(_)                
        | | _____  _| |_   ) |_ _ __ ___   __ _ 
        | |/ _ \ \/ / __| / /| | '_ ` _ \ / _` |
        | |  __/>  <| |_ / /_| | | | | | | (_| |
        |_|\___/_/\_\\__|____|_|_| |_| |_|\__, |
                                           __/ |
                                           |___/ 
                                      \033[0m""")

    print(colored("="*59, "green"))
    
   
    # Prompt user for text input
    text = input("\n \033[1;34mEnter the text to generate an image from: \033[0m")
    # Prompt user for number of images to generate
    num_images = int(input(colored("\n How many images do you want to generate? ", "cyan")))

    if num_images > 0:
        print("\n \033[1;33mMay take a while depending on your network speed so please wait..\n\033[0m")

    for i in range(num_images):
        #Generate a random filename for each image
        
        filename = f"result_{i+1}_{random.randint(1000,9999)}.jpg"

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
        with open(f"/data/data/com.termux/files/home/storage/shared/Gpt/{filename}", 'wb') as f:
            f.write(response.content)

        # Inform user of successful save location
        print(colored("="*59, "green"))
        print(f"\033[1;32mImage {i+1} saved as \033[1;36m{filename}\033[1;32m in \033[1;35ma folder called Gpt inside your storage\033[1;32m directory.\033[0m")
        print(colored("="*59, "green"))


# Define the chat with AI function
def chat_with_ai():
    # Define the prompt that the chatbot will use to start the conversation
    prompt = "Hello, how can I help you today?"

    # Initialize the conversation history
    conversation_history = ""
    os.system("clear")
    print(colored("="*59, "green"))
    print(colored(custom_fig.renderText('      Ask_AI'), color='cyan'))    
    print(colored("\n Start chatting with AI","green"))
    print(colored("\n You can type 'exit', 'quit', or 'bye'\n to end the conversation.","green"))
    print(colored("="*59, "green"))

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


