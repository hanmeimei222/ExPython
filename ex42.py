# Animal is-a object
class Animal(object):
    def introduce(self):
        print "This is Animal\n"


# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a __init__ that takes self and name parameters
        self.name = name

    def introduce(self):
        print "This is Dog\n"


# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a __init__ that takes self and name parameters
        self.name = name


# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a __init__ that takes self and name paramters
        self.name = name
        print "Person's init function called"
        # Person has-a pet of some kind
        self.pet = None


# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # Employee has-a __init__ that inherit from
        # parent class Person's __init__
        print "Employee's init function called"
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a Fish
class Salmon(Fish):
    pass


# Halibut is-a Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")
rover.introduce()
print rover.name

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# frank is-a Employee, he has-a name called Frank and salary about 120000
frank = Employee("Frank", 120000)
print frank.name
print frank.salary

# frank has-a pet named rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
