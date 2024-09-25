#constructor: function that gets called at the time of creating an object
class Point:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10,20)
point.x = 11
print(point.x)

#exrecise
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}, and I am talking...")


person1 = Person("John Smith")
person1.talk()
person2 = Person("Jack Daniel")
person2.talk()