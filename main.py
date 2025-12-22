from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import init, Fore, Style

init()

def print_colored(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL)

def main():
    N = 10

    rect = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")

    print_colored(f"Создан {rect}", Fore.BLUE)
    print_colored(f"Создан {circle}", Fore.GREEN)
    print_colored(f"Создан {square}", Fore.RED)


if __name__ == "__main__":
    main()
