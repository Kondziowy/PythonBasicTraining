class Parent:
  def __init__(self, a):
    self.a = a
  def method(self):
    print(self.a)
	
obj = Parent(2)
obj.method()

class Child(Parent):
  def __init__(self,a):
    super(Child, self).__init__(a)
    self.b = "data"
  def __eq__(self, right):
    return self.a == right.a

obj = Child(2)
obj.method()
print(obj.b)
obj2 = Child(2)
print(obj == obj2) 
obj2 = OtherChild(2)
print(obj == obj2) 