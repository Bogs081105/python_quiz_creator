# import necessary libraries
import csv # save as csv file
from rich.console import Console # add colors into the text inside the terminal
from rich.prompt import Prompt

#initialize console from rich 
console = Console()

# initialize an empty list to store the quiz data
quiz_data = []

# use while loop to continuously ask the user
while True:
    console.print("[bold yellow] Add a New question[/bold yellow]")
# ask the user to input questions
    question = Prompt.ask("[bold]Please enter your question[/bold]")
# add exit condition
    if question == "exit":
        console.print("[bold green] Exiting the quiz creator...[/bold green]")
        break
# ask the user to input the choices of the questions [A, B, C, D]
    answer_a = Prompt.ask("[dark_magenta]A[/dark magenta]")
    answer_b = Prompt.ask("[dark_magenta]B[/dark magenta]")
    answer_c = Prompt.ask("[dark_magenta]C[/dark magenta]")
    answer_d = Prompt.ask("[dark_magenta]D[/dark magenta]")
# ask the user to enter the correct answer of the question
# add the questions and answers into the empty list
# save the inputs into the file
# ask the user if they want to continue or not