# class circle:
#     def __init__(self,radius):
#         self.radius=radius 

#     def Area(self):
#         return (22/7) * self.radius * self.radius
        
#     def perimeter(self):
#         return 2* (22/7) *self.radius
# c1= circle(5)
# print(c1.Area())
# print(c1.perimeter())

# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self): 
#        print("role=", self.role)    
#        print("dept=", self.dept) 
#        print("salary=", self.salary)   

# class Engineer(Employee):
#     def __init__(self, name , age):
#        self.name=name
#        self.age=age 
#        super().__init__("manager","health","800000")     
 
# eng1 = Engineer("mudasir",22)
# print("welcome",eng1.name,"your",eng1.age,"age is more than enough you can join us with following details")
# eng1.showDetails()

# class order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price

#     def __gt__(self,ordr1):
#         return (self.price<ordr1.price)

# ordr1 = order("choips",300)
# ordr2 = order ("lays",55)

# print(ordr1>ordr2,ordr2>ordr1)

class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"MyClass instance with name '{self.name}'"

obj = MyClass("example")
print(str(obj))  # Output: MyClass instance with name 'example'

