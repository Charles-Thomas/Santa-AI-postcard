import time
import random
import openai
import datetime
import os
import config



class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'

def print_colored_message(message, color):
    print(f"{color}{message}{Color.RESET}")

class xmas:
    name= ""
    age= ""
    wishes= ""



def jolly_intro():
    print_colored_message("HO HO HO--", Color.RED)
    time.sleep(1)
    print("oh wait--we're not Santa!")
    time.sleep(1)
    print_colored_message("We're Santa's Elves, or as you humans like to call us, his helpers", Color.GREEN)
    time.sleep(1)
    print("Santa is REALLY busy this year so with help from @BLKSheep and @Uzvara")
    time.sleep(1)
    print_colored_message("He created Sant-AI, but we like to call him SantAI", Color.RED)
    time.sleep(1)
    print("And now all of your postcards will be answered right away!")
    time.sleep(1)
    print_colored_message("Just tell SantAI what's on your wish list", Color.GREEN)
    time.sleep(1)
    print("And SantAI will take care of all the rest!")

def wish_list():
    time.sleep(2)
    dear_santa = input("Would you like to write a postcard to Santa Claus? Y/N   ").lower()
    time.sleep(2)
    if dear_santa == "y":
        xmas.name = input("What is your name?  ")
        time.sleep(2)
        xmas.age = input("And how old are you?  ")
        time.sleep(2)
        xmas.wishes = input("Santa wants to give you exactly what you want this year, so make sure you include everything before pressing enter:  ")
        postcard()
    else:
        print("HO HO HO! I'LL SEE YOU NEXT YEAR")
        
        
def postcard():
    

    time.sleep(2)
    print("Let's make sure we've got it all right before we ship off this postcard!")
    time.sleep(2)
    print_colored_message("Your name is " + xmas.name, Color.RED)
    time.sleep(2)
    print("You are " + str(xmas.age) + " years old")
    time.sleep(2)
    print_colored_message("And here is your letter to Santa: ", Color.GREEN)
    time.sleep(1) 
    envelope()
        
    print("Looks like santa has got a reply for you....")
    # openai.api_key = "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"
    # openai.api_key = os.environ['OPENAI_API_KEY']
    config.openai.api_key
    xmas()  # Creating an instance of the Xmas class

 

    prompt = f"React to the list of gifts that the child wants for Christmas and make sure you say you're going to get it for them: {xmas.wishes}"
      
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a jolly Santa replying to what a kid wants for Christmas this year in a letter wihtout saying their name"},
            {"role": "user", "content": xmas.wishes}
        ]
    )

    hohoho()
    print("====================================================================================")
        # play loop of letter opening 
    print(completion.choices[0].message["content"])

    print("===================================================================================")

   
def envelope():
    my_list = []
    today = datetime.date.today()
    my_list.append(str(today))
    date =''.join(my_list)
    letter = [
        "  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _",
        " /                                                                        \\",
        "|    Dear SantAI,                                                            |",
        "|                                                                            |",
        "|    My name is " + xmas.name + " and I am " + xmas.age + "     years old.   |",
        "|    For Christmas this year, I want " + xmas.wishes + "                     |",                                                                                                                          
        "|                                                                            |",
        "|    Happy Holidays,                                                         |",
        "|    " + xmas.name + "                                      "      +date+ "  |",
        " \\_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ /"
    ] 
    def generate_snow(width, height):
        snow = []
        for _ in range(height):
            row = ""
            for _ in range(width):
                if random.random() > 0.7:  
                    row += "*"
                else:
                    row += " "
            snow.append(row)
        return snow

    def print_scene(letter, snow):
        for i in range(len(letter)):
            print(letter[i])
        for row in snow:
            print(row)

    letter_width = len(letter[0])
    letter_height = len(letter)

    snow = generate_snow(letter_width, letter_height)

    for i in range(letter_height):
        print("\n" * 5)  # Clear the screen for a "refreshed" animation
        print_scene(letter[:i + 1], snow)
        time.sleep(0.2)

    corrections()
    hohoho()
   

# Simulate snow 

def corrections():
        correct = input("Is all of this correct? Y/N  ").lower()
        if correct == "y":
            time.sleep(2)
            print_colored_message("What a phenomenal list! I'm sure Santa and the rest of us elves are going to get right to work for you!", Color.RED)
        else: 
            print_colored_message("Looks like we got our lights all tangled! Let's try again", Color.GREEN)
            time.sleep(1)
            redo = input("Is more than one part of your information wrong? Y/N:  ").lower()

            if redo == "y":
                time.sleep(2)
                print_colored_message("Let's start all the way over so we can make sure Santa gets your postcard!", Color.RED)
                wish_list()
                postcard()
            else:
                jolly_redo = int(input("Which part is incorrect? 1. Name 2. Age 3. Wish List (Enter corresponding number) "))
                if jolly_redo == 1:
                    jolly_name_redo = input("Sorry we fudged your name, let's try that again. What is your name?  ")
                    xmas.name = jolly_name_redo
                    postcard()
                elif jolly_redo == 2:
                    jolly_age_redo = input("Oops! Did we make you too old? Too young? Elves live so long we forget! Re-enter your age:  ")
                    xmas.age = jolly_age_redo
                    postcard()
                elif jolly_redo == 3:
                    jolly_wish_redo = input("WHEW! Good catch! Let's make sure that list is perfect. Re-enter your wish list here (Remember-don't press enter until you're done):  ")
                    xmas.wishes = jolly_wish_redo
                    postcard()
                else:
                    print_colored_message("Uh oh! Looks like we're gonna have to start over.", Color.GREEN)
                    wish_list()
                    postcard()

def hohoho():
    segue = [
        " _    _  ____    _    _  ____    _    _  ____  ",
        "| |  | |/ __ \  | |  | |/ __ \  | |  | |/ __ \ ",
        "| |__| | |  | | | |__| | |  | | | |__| | |  | |",
        "|  __  | |  | | |  __  | |  | | |  __  | |  | |",
        "| |  | | |__| | | |  | | |__| | | |  | | |__| |",
        "|_|  |_|\____/  |_|  |_|\____/  |_|  |_|\____/",
        "\n",
        "\n"
    ]

    for line in segue:
        print_colored_message(line, Color.RED if "RED" in line else Color.GREEN)
        time.sleep(0.2)
def candy():
    print_colored_message("  =========== ", Color.RED) 
print("----------====")
print_colored_message("-----     ====", Color.RED)
print("-----     ====")
print_colored_message("-----     ====", Color.RED)
print("=====")
print_colored_message("-----", Color.RED)
print("=====")
print_colored_message("-----", Color.RED)
print("=====")
print_colored_message("-----", Color.RED)
print("=====")
print_colored_message("-----", Color.RED)
print("=====")
print_colored_message("-----", Color.RED)
print("=====")




jolly_intro()
wish_list() 


