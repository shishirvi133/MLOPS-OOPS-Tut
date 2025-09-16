# Define a class named 'Chatbook'
class Chatbook:
    def __init__(self):
        # Initialize attributes for username, password, and login status
        self.username = ''
        self.password = ''
        self.loggedin = False

        # Call the menu method directly from the constructor
        # This means the menu will be displayed immediately when an object is created
        self.menu()

    # Define a method to show the main menu
    def menu(self):
        # Display a multi-line menu and take user input
        user_input = input("""\nWelcome to Chatbook! How would you like to proceed?
1. Press 1 to Signup
2. Press 2 to Signin
3. Press 3 to Write a Post
4. Press 4 to Message a Friend
5. Press any other key to Exit
Your choice: """)

        # Use if-elif statements to determine what action to take based on user input
        if user_input == '1':
            pass  # Placeholder for signup functionality
        elif user_input == '2':
            pass  # Placeholder for signin functionality
        elif user_input == '3':
            pass  # Placeholder for writing a post
        elif user_input == '4':
            pass  # Placeholder for messaging a friend
        else:
            # If user enters any other key, exit the program
            exit()

# Create an instance of the Chatbook class
# Since self.menu() is called in __init__, the menu is shown immediately
obj = Chatbook()
