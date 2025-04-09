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
    console.print("[dark_magenta]Enter answer for A[/dark_magenta]")
    answer_a = Prompt.ask("A")

    console.print("[dark_magenta]Enter answer for B[/dark_magenta]")
    answer_b = Prompt.ask("B")
    
    console.print("[dark_magenta]Enter answer for C[/dark_magenta]")
    answer_c = Prompt.ask("C")

    console.print("[dark_magenta]Enter answer for D[/dark_magenta]")
    answer_d = Prompt.ask("D")

# ask the user to enter the correct answer of the question
    correct_answer = Prompt.ask("[green]Enter the correct answer(A/B/C/D)[/green]").upper()
    if correct_answer not in ["A", "B", "C", "D"]:
        console.print("[red]INVALID ENTRY![/red][bold] Please enter A, B, C, or D[/bold]")

# add a new set that includes the answers inputted
data = [question, answer_a, answer_b, answer_c, answer_d, correct_answer]

# add the questions and answers into the empty list
quiz_data.append(data)

# save the inputs into the file
with open("quiz_creator.csv", mode='a', newline='', encoding='utf-8' ) as file:
    writer = csv.writer(file)
    writer.writerow([question])
    writer.writerow([answer_a])
    writer.writerow([answer_b])
    writer.writerow([answer_c])
    writer.writerow([answer_d])
    writer.writerow([correct_answer])

# ask the user if they want to continue or not
ask_again = Prompt.ask("[bold]Ask another question?[/bold]([bold green]Yes[/bold green]/[bold red]No[/bold]").lower
if ask_again != "yes":
    console.print("\n[bold cyan] Good job! Quiz has now been finished![/bold cyan]")