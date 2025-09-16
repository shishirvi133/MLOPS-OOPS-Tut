# Initiate a class
class employee:
      # Constructor: Initializes core attributes
      def __init__(self):
            self.id = 123
            self.salary = 50000
            self.designation = "SDE"

      # A method that doesn't use 'self' – will cause issues if called via object
      def travel(self,destination):
            print("This travel function was called manually")
            print(f"Employee is now travelling to {destination}")

# Create an instance of the class
sam = employee()

# ✅ Dynamically adding a new attribute to the object outside the class
sam.name = "Sam Kumar"

# Accessing the dynamically created attribute
print(sam.name)  # Output: Sam Kumar

# Accessing the attribute that was defined in __init__
# print(sam.id)

# sam.travel("kerala")

# Check object type
# print(type(sam))

print(sam.__dict__)

