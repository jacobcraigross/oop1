# ATTRIBUTES

class Dog():

    # class object attribute.
    species = 'mammal'

    def __init__(self, breed, name, age):

        self.breed = breed
        self.name = name
        self.age = age

my_dog = Dog('Huskie', 'Jimbo', 4)
new_dog = Dog('Pitmix', 'Sally', 3)
last_dog = Dog('Chow', 'Blue Bear', 7)

print new_dog.age
print last_dog.species
print my_dog.name

# ----------------

# METHODS

class Circle():
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area (self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

my_circle = Circle(4)
my_circle.set_radius(999)
print my_circle.area()

# ----------------

# INHERITANCE

class Animal():

    def __init__(self):
        print 'animal created'

    def who_am(self):
        print 'animal'

    def eat (self):
        print 'I am eating'

# all dogs are animals.
class Dog(Animal): # we pass in Animal to Dog to inherit from it.

    def __init__(self):
        # Animal.__init__(self)   ..technically, we dont need this line.
        print 'dog created'

    def bark (self):
        print 'woof'

    def eat(self): # over writing the previous method
        print 'dog eating'

myd = Dog()
myd = Animal()
myd.who_am()
myd.eat()

# ----------------

# SPECIAL METHODS

# when you call print function on an object, it looks for its string representation.

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): # here we define the string rep.
        return 'title: {}, author: {}, pages: {}'.format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print 'a book has been destroyed'


b = Book('Python CVCC', 'Joserty', 255)
print b
print len(b)
del b
