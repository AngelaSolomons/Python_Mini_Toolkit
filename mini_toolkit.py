#Import Modules
import time
import random
import daily_quotes



# Program Welcome
def greeting(name):
    print(f"Welcome to your Mini Toolkit {name}!")
    print()

print()
name = input("Enter your name: ")
print()

greeting(name)



# Menu Options
menu_options = ("1", "2", "3", "q")

while True:
    print()
    print("** MENU **")
    print("1 = To-Do List")
    print("2 = Daily Motivation")
    print("3 = Guess the Number Game")
    print("q = Quit")
    print()

    user_input = input("Select an option: ")
    print()

# Validate Input
    if user_input not in menu_options:
        print("Option is invalid. Try again")
        continue

# Quit Program
    if user_input == "q":
        print(f"Leaving? See you later {name}!")
        break



# First mini-tool: To-Do List
    if user_input == "1":
        time.sleep(1)
        print("Welcome to your To-Do List!")
        print("What tasks will you complete today? Type done to view list.")
        print()

        def to_do():
            tasks = []

            while True:
                print(f"Tasks for the day: ")
                task = input("Add task: ")

    # Break while loop
                if task.lower() == "done":
                    break

    # Add tasks to list
                tasks.append(task)
                
            if len(tasks) == 0:
                print()
                print("You have no tasks for the day! Take a break!")
                print()
            else:
                print()
                print("These are your tasks for the day!")
                for task in tasks:
                    print(f"- {task}")

# Call Function
        to_do()
        print()
        print("Returning to menu...")
        print()
        print()
        time.sleep(3)



# Second mini-tool: Daily Motivation Generator
    elif user_input == "2":
        time.sleep(1)
        print("Welcome to your Daily Motivation!")
        print()
        print("Your quote of the day is:")

        # Define Function
        def get_quote ():
            return random.choice(daily_quotes.quotes)

        # Call function from custom module
        print(f"{get_quote()}")
        print()
        print("Returning to menu...")
        print()
        print()
        time.sleep(5)



# Third Mini-Tool: Number Guessing Game
    elif user_input == "3":
        time.sleep(1)
        print("Let's guess SUM numbers! This is Guess the Number!")
        print()

        # Define Function
        def play(max_attempts):
            correct_answer = random.randint(1, 50)
            attempts = 0

            print(f"Which number do you think it will be? You have {max_attempts} attempts!")
            print()
            print()

            for i in range(max_attempts):
                attempt = int(input("Enter your answer (1 - 50): "))
                attempts += 1

                if attempt < 1 or attempt > 50:
                    print(f"Uh oh! Your answer must be between 1 and 50.")
                    print()
                elif attempt < correct_answer:
                    print("Oops! Try a higher number...")
                    print()
                elif attempt > correct_answer:
                    print("Nope! Try a lower number next...")
                    print()  
                else:
                    print("Congratulations! You're correct!")
                    print()
                    return

            if attempts == max_attempts:
                print(f"Oh no, looks like you ran out of attempts! The correct answer was {correct_answer}")
                print("Better luck next time!") 

        # Call function
        while True:
            play(5)
            print()

            replay = input("Want to play again? (yes/no): ")

            if replay.lower() not in ["yes", "y"]:
                print()
                print("Thank you for playing, that was fun! C-alc-U-LATER!")
                print()
                break

        print()
        print("Returning to menu...")
        print()
        print()
        time.sleep(5)
