# MINI TOOLKIT
## Overview
**Mini Toolkit** is a Python console application that combines productivity, motivation, and entertainment into one simple program. The project was designed around the idea that productivity is not only about completing tasks, but also about maintaining the right mindset and taking healthy breaks.

The application contains three mini tools:
- To-Do List – Helps users organize their daily tasks.
- Daily Motivation Generator – Displays a random motivational quote to encourage and inspire users before they begin working.
- Guess the Number Game – A small game designed to provide users with a quick mental break and some fun during the day.
  
***The goal of the project was to create a balanced program that supports productivity while also focusing on motivation and relaxation.***


## Features
The **To-Do List** allows users to enter and manage tasks for the day. This tool represents the “serious” side of the application by helping users stay organized and productive.
Features:
- Users can continuously add tasks.
- Tasks are stored in a list.
- Typing "done" stops task entry and displays all tasks entered.
- If no tasks are entered, the program encourages the user to take a break then returns to menu.

The **Daily Motivation generator** displays a random motivational quote selected from a custom quotes module. This tool was designed to help users get into a positive and focused mindset before tackling their daily tasks.
- Random quote generation using Python’s random module.
- Quotes are stored separately inside a custom module called daily_quotes.
- Encourages users before starting their work.


The **Guess the Number game** is a small interactive game where users try to guess a randomly generated number between 1 and 50. This mini game acts as a fun distraction and gives users a chance to relax and reset before returning to work.
- Random number generation.
- Users have 5 attempts to guess correctly.
- Feedback is provided after each guess:
    - Too high
    - Too low
    - Correct answer
- Replay option included.

## Python concepts I used
- Variables and data types
- User input and output
- Type casting
- Conditional statements
- Loops
- Functions
- Lists
- Built-in modules
- Custom module
- Comparison and logical operators

## How to Run the Project
### Requirements:
Python installed
### Steps:
- Download the project files
- Make sure these files are in the same folder:
  - main.py
  - daily_quotes.py
  - Open a terminal or command prompt
- Navigate to the project folder
- Run the program:

## Challenges I faced
One challenge was figuring out how to create my first menu system, and having my functions within the same file, as putting the menu first resulted in the functions not being defined. 

## How I overcame these challenges
I overcame these challenges by carefully planning the program structure, testing the code frequently, and using loops and conditionals to control how the program behaved.

## What I learned
I learned how to create a program with multiple features that work together in one application, while improving my understanding of the python concepts, especially regarding functions and loops. I am proud that I successfully created three different tools inside one application and made them work together smoothly.

## Future Improvements
While there are many improvements to be made, my next focus will be adding better error handling, and improving the appearance of the program by creating a graphical interface so the application is easier and more enjoyable to use. In the future I want to add a "save tasks" feature in my to-do list so that the user can refer back to their tasks at a later stage, as well as adding the option to close the tool and return to menu or to continue, as currently two of the tools automatically end as soon as they have run their course.

## Author
Created by Angela Solomons
