import sys
import time

def type_text(text, delay=0.014):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()   # make sure it's displayed immediately
        time.sleep(delay)
    print()  # new line after typing is done

def type_text_ascii(text, delay=0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()   # make sure it's displayed immediately
        time.sleep(delay)
    print()  # new line after typing is done


print(r'''
 __        __   _                                            
 \ \      / /__| | ___ ___  _ __ ___   ___     
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   
   \ V  V /  __/ | (_| (_) | | | | | |  __/      
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|        
''')


def treasure_island():
    type_text('''This is a Game developed by: "Rudraksha Deshmukh" ''')
    type_text("\n🏝️ Welcome brave adventurer, to **Treasure Island**!")
    type_text(
        "Legend speaks of a hidden treasure buried deep within this mysterious land. Many have tried to claim it, "
        "but none have returned...\nThey say whoever discovers it will become the richest person in the world!")
    type_text("Will you be the one to uncover its secrets and emerge victorious?")
    type_text("The journey begins now...")

    type_text("\n🌅 As you stand at a dusty crossroads, the sun sets behind you, casting long shadows. "
                    "To the **left**, the path winds through a quiet forest. To the **right**, a steep cliff "
                    "falls into darkness.\n")
    choice1 = input("Which way do you go?\n Type 'left' or 'right': ").lower()
    if choice1 == "left":
        type_text("\n🌊 You emerge from the woods and find a wide, shimmering lake blocking your path. "
                        "A faint mist hangs above the water.\nYou can **wait** by the shore to see if help arrives, "
                        "or **swim** across showing your swimming skills!\n")
        choice2 = input("\nWhat do you want to do? Type 'wait' or 'swim': ").lower()
        if choice2 == "wait":
            type_text("\n🚤 After some time, an old boat silently drifts to shore. "
                            "You climb aboard, and it takes you across safely.\nYou arrive at a strange island "
                            "clearing, where a worn-down cottage stands with three painted doors: "
                            "one **red**, one **yellow**, and one **blue**.\n")
            choice3 = input("\nWhich door do you choose? "
                            "Type 'red', 'yellow', or 'blue': ").lower()
            if choice3 == "yellow":
                type_text("\n💰 As the yellow door creaks open, sunlight floods a hidden chamber filled with "
                      "glittering treasure! You’ve found it — the legendary treasure of the island!"
                      "\n🎉 Congratulations adventurer! You win!\nHere is the treasure: ")
                type_text_ascii(r'''
                *******************************************************************************
                          |                   |                  |                     |
                 _________|________________.=""_;=.______________|_____________________|_______
                |                   |  ,-"_,=""     `"=.|                  |
                |___________________|__"=._o`"-._        `"=.______________|___________________
                          |                `"=._o`"=._      _`"=._                     |
                 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                |___________________|_."  `. ` ` `` ,  `"-._"-._   ". '__|___________________
                          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
                |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/
                ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/___
                /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/
                ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/___
                /______/______/______/______/______/______/______/______/______/______/_____/
                /*****************************************************************************\
                |                                                                             |
                |   💰💰💰  CONGRATULATIONS! YOU FOUND THE TREASURE!  💰💰💰                    |
                |                                                                             |
                |      You open the chest and it bursts with sparkling gold, shining         |
                |      jewels, ancient coins, and priceless artifacts from long-lost kings.  |
                |      Your journey has been rewarded beyond imagination.                    |
                |_____________________________________________________________________________|
                ''')

                play_again()
            elif choice3 == "red":
                type_text("\n🔥 You open the red door, and flames burst out, engulfing the room and You!.. "
                      "It's a trap!\nGame Over.")
                try_again()
            elif choice3 == "blue":
                type_text("\n👹 Behind the blue door lies a dark chamber filled with glowing eyes. "
                      "Before you can react, someone covered your face with a blanket and tied you up! \nGame Over.")
                try_again()
            else:
                type_text("🚪 You chose a door that doesn't exist. Game Over.")
                try_again()
        elif choice2 == "swim":
            type_text("You are brave, I got it 👍...But the large black boat with a skull faced flag emerges"
                  "from nowhere and within no time they reached you. They are Pirates!!! Game Over.")
            try_again()
        else:
            type_text("😕 Invalid input. Game Over.")
            try_again()
    elif choice1 == "right":
        type_text("Heading right is not always a right choice❌...💀 You fell into a trapped-hole. Game Over.")
        try_again()
    else:
        type_text("😕 Invalid input. Game Over.")
        try_again()


def try_again():
    response = input("\nWould you like to try again? (yes/no): ").lower()
    if response == "yes":
        treasure_island()
    elif response == "no":
        type_text("Thanks for playing! Goodbye! 👋")
    else:
        type_text("❌ Invalid input. Exiting the game.")
        type_text("Goodbye! 👋")


def play_again():
    response = input("\nWould you like to play again and try a different path? (yes/no): ").lower()
    if response == "yes":
        treasure_island()
    elif response == "no":
        type_text("Great job finding the treasure! See you next time! 🏆")
    else:
        type_text("❌ Invalid input. Exiting the game.")
        type_text("Goodbye! 👋")


# Start the game
treasure_island()


input("Press any key to Exit...")