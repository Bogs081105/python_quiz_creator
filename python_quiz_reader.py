# import the necessary libraries
import random
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# Initialize console from rich
console = Console()
console.print(Panel.fit("[bold] Welcome to Python Quiz Reader![/bold]"))
# Initialize empty set to store the questions
questions = []

# Load the quiz data from the file
if not os.path.exists("quiz_data.txt"):
    console.print("[bold red]Quiz data file not found. Please create a quiz first.[/bold red]")
else:
    with open("quiz_data.txt", "r", encoding="utf-8") as file:
        quiz_content = file.read().strip()

# option for empty empty quiz data/not found quiz data
    if not quiz_content:
        print("[bold red]No quiz data found. Please create a quiz first.[/bold red]")
# Separate the quiz data into individual quizzes and process each one
    else:
        raw_quizzes = quiz_content.split("---\n")
        for quiz in raw_quizzes:
            lines = quiz.strip().splitlines()
            if len(lines) < 7:
                console.print("[bold red]Invalid quiz format. Please check the quiz data.[/bold red]")
                continue

            quiz_data = {
                "timestamp": lines[0].replace("Timestamp: ", ""),
                "question": lines[1].replace("Question: ", ""),
                "A": lines[2][3:].strip(),
                "B": lines[3][3:].strip(),
                "C": lines[4][3:].strip(),
                "D": lines[5][3:].strip(),
                "correct": lines[6].replace("Correct Answer: ", "").strip().upper()
            }
            questions.append(quiz_data)

        


# Start quiz loop to allow the user to keep taking the quiz until they choose to exit
while True:
    if not questions:
        console.print("[bold red]No quiz data available. Please create a quiz first.[/bold red]")
        break
# pick a random question from the quiz data
    question = random.choice(questions)

# display the question
    console.print(Panel.fit(f"[bold]Question: {question['question']}[/bold]"))
    console.print(f"A. {question['A']}")
    console.print(f"B. {question['B']}")
    console.print(f"C. {question['C']}")
    console.print(f"D. {question['D']}")
# Ask the user to input their answer
    user_answer = Prompt.ask("[bold yellow]Your answer (A/B/C/D)[/bold yellow]").strip().upper()
    
# Check if the answer is correct and display the result
# Update the score and display it
# Ask the user if they want to continue or exit the quiz