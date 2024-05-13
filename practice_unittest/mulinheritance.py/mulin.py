# class A:
#     varA="welcome to class A"


# class B:
#     varB="welcome to class B"

    
# class C(A,B):
#     varC="welcome to class C"

# c1=C()

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)
# class person:
#     name="noone"

    # def chagename(self,name):
    #     self.__class__.name="mudasir" #self.__class__. , person.name,>>>>class methods,static method,property decorator
    # ,getter and setter decorator
#     @classmethod 
#     def changename(cls,name):
#       cls.name = name



# p1= person()
# p1.changename("mudasir") 
# print(p1.name)   
# print(person.name)  

# class complex:
#   def __init__(self,real,img):
#         self.real=real
#         self.img=img

#   def shownum(self):
#         print(self.real,"i+",self.img, "j")

#   def __add__(num1, num2):
#         newreal=num1.real + num2.real
#         newimg=num1.img + num2.img
#         return complex(newreal,newimg)

# num1 = complex(1,4)
# num1.shownum()

# num2 = complex(4,8)
# num2.shownum()

# num3=num1 + num2
# num3.shownum()

# class Car:
#  def __init__(self,type): 
#       self.type=type

#  @staticmethod 
#  def start():
#   print("car started")

#  @staticmethod 
#  def stop():
#   print("car stopped")

# class toyota_car(Car): 
#     def __init__(self,name,type):
#      self.name = name
#      super().__init__(type)
    

  
  
# car1 = toyota_car("prius","HQ") 
# print(car1.type) 
# print(car1.name)
# car1.start() 
# car1.stop()


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

# for x in (car1, boat1, plane1):
#   x.move()
print(car1.brand)
car1.move()
boat1.move()
plane1.move()
