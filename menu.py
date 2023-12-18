class MainMenu:
    """The menu that will be displayed while running the code."""
    def __init__(self) -> None:
        self.menu_entries = {}
        
    def register_entry(self, number, description, command):
        self.menu_entries[number] = (description, command)
        
    def display_menu(self):
        print("Main Menu:")
        for number, (description, _) in self.menu_entries.items():
            print(f"{number}. {description}")
            
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1/2/3/4.../0 to exit): ")
            try:
                choice_1 = int(choice)
            except ValueError as err:
                print("Invalid input. Please enter a valid number.")
                continue

            if choice == "0":
                print("Goodbye!")
                break
            elif choice in self.menu_entries:
                _, command = self.menu_entries[choice]
                command()
                input("Press ENTER to return to the main menu.")
            else:
                print("Command not found. Try again!")
