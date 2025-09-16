#initiate a class
class employee:
      #special method/magic method/dunder  method  -constructor
      def __init__(self):
            print("Started executing attributes/data")
            self.id = 123
            self.salary = 50000
            self.designation = "SDE"
            print("Attribute/data has been in initaiated")


      def travel(self,destination):
            print("This travel function was call manually")
            print(f"Employee is now travlelling to {destination}")

#create an obj/instance of the class
sam = employee()

#print(sam.id)

sam.travel("kerala")

print(type(sam))