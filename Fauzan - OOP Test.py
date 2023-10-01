class Person(object):
    # Initialised all attributes
    def __init__(self, firstname, lastname, age, height, weight):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.height = height
        self.weight = weight

    # Returns All values Individually
    def getFirstName(self):
        return self.firstname
    
    def getLastname(self):
        return self.lastname
    
    def getAge(self):
        return self.age
    
    def getHeight(self):
        return self.height
    
    def getWeight(self):
        return self.weight

    # Sets all Values individually
    def setFirstName(self):
        self.firstname = input("Enter your first name:  ")

    def setLastName(self):
        self.lastname = input("Enter your last name:  ")

    def setAge(self):
        self.age = int(input("Enter your  age:  "))

    def setHeight(self):
        self.height = float(input("Enter your height (in metres):  "))

    def setWeight(self):
        self.weight = float(input("Enter your weight (in kg):  "))

    # Sets All Values at Once
    def setAllValues(self):
        self.firstname = input("Enter your first name:  ")
        self.lastname = input("Enter your last name:  ")
        self.age = int(input("Enter your  age:  "))
        self.height = float(input("Enter your height (in metres):  "))
        self.weight = float(input("Enter your weight (in kg):  "))
        
    # Returns All Values at Once
    def getAllValues(self):
        return self.firstname, self.lastname, self.age, self.height, self.weight


class Teacher(Person): # Inheritance as we passed on Person
    def __init__(self, firstname, lastname, age, height, weight):
        # Super used
        super().__init__(firstname, lastname, age, height, weight)

    # Sets the Classes
    def setClasses(self):
        lesson1 = input("What do you have period 1? \n")
        self.lesson1 = lesson1
        lesson2 = input("What do you have period 2? \n")
        self.lesson2 = lesson2
        lesson3 = input("What do you have period 3? \n")
        self.lesson3 = lesson3
        lesson4 = input("What do you have period 4? \n")
        self.lesson4 = lesson4
        lesson5 = input("What do you have period 5? \n")
        self.lesson5 = lesson5
        lesson6 = input("What do you have period 6? \n")
        self.lesson6 = lesson6

    # Prints all Classes
    def getClasses(self):
        print("Teachers Timetable")
        print("Lesson 1: ", self.lesson1)
        print("Lesson 2: ", self.lesson2)
        print("Lesson 3: ", self.lesson3)
        print("Lesson 4: ", self.lesson4)
        print("Lesson 5: ", self.lesson5)
        print("Lesson 6: ", self.lesson6)
        

class Student(Teacher): # Inheritance as we passed on Teacher
    def __init__(self, firstname, lastname, age, height, weight):
        # Super used
        super().__init__(firstname, lastname, age, height, weight)

    # Polymorphism Used
    def getClasses(self):
        print("Students Timetable") # Prints out the following statement
        print("Lesson 1: ", self.lesson1)
        print("Lesson 2: ", self.lesson2)
        print("Lesson 3: ", self.lesson3)
        print("Lesson 4: ", self.lesson4)
        print("Lesson 5: ", self.lesson5)
        print("Lesson 6: ", self.lesson6)
    
# List Created
listOfStudents = []
listOfStudentsName = []
def CreateTeacher():
    # Created Teacher instance
    Teacher1 = Teacher("", "", 0, 0, 0)
    Teacher1.setFirstName()
    Teacher1.setLastName()
    Teacher1.setAge()
    Teacher1.setHeight()
    Teacher1.setWeight()
    Teacher1.setClasses()
    firstname, lastname, age, height, weight = Teacher1.getAllValues()
    print("First Name: ", firstname)
    print("Last Name: ", lastname)
    print("Age: ", age)
    print("Height: ", height)
    print("Weight: ", weight)
    
    Teacher1.getClasses()
    
def CreateStudent(objectname, firstname, lastname):
    # Created Student Instance for each student
    objectname = Student(firstname, lastname, 0, 0, 0)
    objectname.setAge()
    objectname.setHeight()
    objectname.setWeight()
    firstname, lastname, age, height, weight = objectname.getAllValues()
    print("First Name: ", firstname)
    print("Last Name: ", lastname)
    print("Age: ", age)
    print("Height: ", height)
    print("Weight: ", weight)
    objectname.setClasses()
    objectname.getClasses()
    
    

def main():
    print("Teacher's Details")
    CreateTeacher()
    num = int(input("How many students do you wish to create: "))
    for i in range(0, num):
        firstname = input("Enter your firstname:  ")
        lastname = input("Enter your lastname:  ")
        fullname = firstname + lastname
        listOfStudents.append(fullname)
        CreateStudent(listOfStudents[i], firstname, lastname)
        fullname = firstname, lastname
        listOfStudentsName.append(fullname)
    print(listOfStudentsName)
        
if __name__ == '__main__':
    main()
