class MenuPage():
    """
    A class representing a menu page in a terminal interface.
    Each page can have multiple options that lead to other pages.(Tree structure)"""
    def __init__(self, title):
         self.title = title
         self.options = []
         self.parent = None
    
    def add_option(self, option):
        self.options.append(option)
        option.parent = self

    def display(self):
        print(f"\n{self.title}")
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option.title}")
        print("0. Back")

class MenuController():
    """
    A class to control the navi of a meny system in terminal interface.
    It allows navigation through a tree of menu pages.
    """
    def __init__(self, root_page):
        self.current_page = root_page

    def navigate(self, choice):
        if choice == 0:
            if self.current_page.parent != None:
                self.current_page = self.current_page.parent
                self.current_page.display()
            return
        if 1<= choice <= len(self.current_page.options):
            self.current_page = self.current_page.options[choice - 1]
            self.current_page.display()
        else:
            print("Invalid choice. Please try again.")
            self.current_page.display()
            
    def run(self):
        self.current_page.display()
        while True:
            try:
                choice = int(input("Enter your choice: "))
                self.navigate(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")
            except KeyboardInterrupt:
                print("\nExiting the menu.")
                break