# import the necessary libraries
import random
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# Load the quiz data from the file
with open("quiz_data.txt", "r", encoding="utf-8") as file:
    quiz_content = file.read().strip()

# option for empty empty quiz data/not found quiz data
if not quiz_content:
    print("[bold red]No quiz data found. Please create a quiz first.[/bold red]")
else:
    # Split the quiz content into individual questions

# Start quiz loop to allow the user to keep taking the quiz until they choose to exit
# pick a random question from the quiz data
# display the question
# Ask the user to input their answer
# Check if the answer is correct and display the result
# Update the score and display it
# Ask the user if they want to continue or exit the quiz