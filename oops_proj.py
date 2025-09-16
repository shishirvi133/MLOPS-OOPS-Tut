# Define a class named 'Chatbook' to encapsulate all features of the app
class Chatbook:
    __user_id = 1  # Class variable to generate unique user IDs

    def __init__(self):
        # Assign a unique user ID to each instance
        self.user_id = Chatbook.__user_id
        Chatbook.__user_id += 1  # Increment the counter for next user

        # Private attribute (name) using name mangling
        self.__name = "Default User"

        # Other user-related attributes
        self.username = ''
        self.password = ''
        self.loggedin = False
    
    @staticmethod
    def get_id(val):
        return Chatbook.__user_id 
    
    @staticmethod
    def set_id(val):
        Chatbook.__user_id = val
        
    
    

    # Getter method for the private name attribute
    def get_name(self):
        return self.__name

    # Setter method to update the private name attribute
    def set_name(self, value):
        self.__name = value

    # Main menu method, runs in a loop to allow continuous interaction
    def menu(self):
        while True:
            user_input = input("""\nWelcome to Chatbook! How would you like to proceed?
1. Press 1 to Signup
2. Press 2 to Signin
3. Press 3 to Write a Post
4. Press 4 to Message a Friend
5. Press any other key to Exit
Your choice: """)

            if user_input == '1':
                self.signup()
            elif user_input == '2':
                self.signin()
            elif user_input == '3':
                self.write_post()
            elif user_input == '4':
                self.message_friend()
            else:
                print("Exiting... Thank you for using Chatbook!")
                break

    # Signup method to register a new user
    def signup(self):
        email = input("Enter email here -> ")
        password = input("Enter your password here -> ")

        self.username = email
        self.password = password

        print("You have signed up successfully!\n")

    # Signin method for authentication
    def signin(self):
        if self.username == '' or self.password == '':
            print("No user found. Please sign up first by pressing 1 in the main menu.")
            return

        uname = input("Enter your email/username here -> ")
        password = input("Enter your password here -> ")

        if self.username == uname and self.password == password:
            print("You have signed in successfully!\n")
            self.loggedin = True
        else:
            print("Incorrect credentials. Please try again.\n")

    # Method for writing a post (only if logged in)
    def write_post(self):
        if self.loggedin:
            post = input("Write your post: ")
            print(f"Post saved: {post}\n")
        else:
            print("Please sign in first to write a post.\n")

    # Method for messaging a friend (only if logged in)
    def message_friend(self):
        if self.loggedin:
            friend = input("Enter your friend's username: ")
            message = input(f"Write a message to {friend}: ")
            print(f"Message sent to {friend}: {message}\n")
        else:
            print("Please sign in first to message a friend.\n")
