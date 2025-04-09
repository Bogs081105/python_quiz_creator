# import necessary libraries
from rich.console import Console # add colors into the text inside the terminal
from rich.prompt import Prompt
from rich.panel import Panel

#initialize console from rich 
console = Console()

console.print(Panel.fit("[bold] Welcome to Python Quiz Creator![/bold]"))

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

# add a time stamp

# save the inputs into the file
    with open("quiz_data.txt", mode='a', newline='', encoding='utf-8' ) as file:
    #insert the timestamp here
        file.write(f"Question: {question}\n")
        file.write(f"A. {answer_a}\n")
        file.write(f"B. {answer_b}\n")
        file.write(f"C. {answer_c}\n")
        file.write(f"D. {answer_d}\n")
        file.write(f"Correct Answer: {correct_answer}\n")
        file.write("---\n")
       

# ask the user if they want to continue or not
    ask_again = Prompt.ask("[bold]Ask another question?[bold]([bold green]Yes[/bold green]/[bold red]No)[/bold red]").lower()
    if ask_again != "yes":
        console.print("\n[bold cyan] Good job! Quiz has now been finished![/bold cyan]")
        break