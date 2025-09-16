# Define a class named 'Chatbook' to encapsulate all features of the app
class Chatbook:
    def __init__(self):
        # Initialize attributes:
        # - username and password for storing user credentials
        # - loggedin flag to track if the user is signed in
        self.username = ''
        self.password = ''
        self.loggedin = False

        # Automatically display the main menu when a Chatbook object is created
        self.menu()

    # Main menu method, runs in a loop to allow continuous interaction
    def menu(self):
        # Loop to keep the program running until user chooses to exit
        while True:
            # Display the main options to the user and get their input
            user_input = input("""\nWelcome to Chatbook! How would you like to proceed?
1. Press 1 to Signup
2. Press 2 to Signin
3. Press 3 to Write a Post
4. Press 4 to Message a Friend
5. Press any other key to Exit
Your choice: """)

            # Handle user input by calling the corresponding method
            if user_input == '1':
                self.signup()  # User wants to create a new account
            elif user_input == '2':
                self.signin()  # User wants to log into an existing account
            elif user_input == '3':
                self.write_post()  # User wants to write a new post
            elif user_input == '4':
                self.message_friend()  # User wants to message someone
            else:
                # Exit the program if user chooses anything else
                print("Exiting... Thank you for using Chatbook!")
                break  # Breaks the while loop and ends the program

    # Method to allow the user to sign up (register)
    def signup(self):
        # Prompt the user for email and password
        email = input("Enter email here -> ")
        password = input("Enter your password here -> ")

        # Save credentials to object attributes
        self.username = email
        self.password = password

        # Confirm successful signup
        print("You have signed up successfully!\n")

    # Method to allow the user to sign in (authenticate)
    def signin(self):
        # If no user has signed up yet, prompt them to sign up first
        if self.username == '' or self.password == '':
            print("No user found. Please sign up first by pressing 1 in the main menu.")
            return  # Return to menu

        # Ask for login credentials
        uname = input("Enter your email/username here -> ")
        password = input("Enter your password here -> ")

        # Check if entered credentials match the stored ones
        if self.username == uname and self.password == password:
            print("You have signed in successfully!\n")
            self.loggedin = True  # Set login flag to True
        else:
            print("Incorrect credentials. Please try again.\n")

    # Method to allow a logged-in user to write a post
    def write_post(self):
        # Check if the user is logged in
        if self.loggedin:
            post = input("Write your post: ")
            # Simulate saving the post (currently just prints it)
            print(f"Post saved: {post}\n")
        else:
            # If not logged in, deny access
            print("Please sign in first to write a post.\n")

    # Method to allow a logged-in user to message a friend
    def message_friend(self):
        # Check if the user is logged in
        if self.loggedin:
            friend = input("Enter your friend's username: ")
            message = input(f"Write a message to {friend}: ")
            # Simulate sending a message (currently just prints it)
            print(f"Message sent to {friend}: {message}\n")
        else:
            # If not logged in, deny access
            print("Please sign in first to message a friend.\n")


# Create an instance of the Chatbook class
# This will automatically call the constructor and start the menu
#obj = Chatbook()
