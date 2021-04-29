'''class Cat:
	def __init__(self,name):
		self.name = name
		  
	def purr(self):
		return 'Purr'
	def add_one(self,x):
		return x+1

c = Cat('Tom')



#print(c.purr())


class Duck:
	def __init__(self,name,age):
		self.name = name
		self.age =age
	# gait is the method in the class	
	def display_name(self):
		return self.name

	def gait(self):
		return 	"Waddle"			

	def get_age(self):
		return self.age 
	def set_age(self,age):
		self.age = age

ins = Duck('Don',5)

print(ins.gait())
#ins.set_age(23)
#print(ins.get_age())'''

'''class Cat:
	def __init__(self):#,name):
		#self.name = name
	#def get_name(self):
	#	return self.name.upper()

	def change_name(self,name):
		self.name = name
		ne = name.upper()
		print(ne)
c = Cat('Tom')

#print(c.get_name())

c.change_name('bobby')

#print(c.get_name())

class Cat:
	def __init__(self):
		pass

	def name(self,name):
		self.name = name
		return name.upper()
ins = Cat()

print(ins.name('some'))


# I think it is Encapsulation
class Animal:
	def __init__(self,name,colour,height):
		self.name = name
		self.colour =colour
		self.height =height

	def get_height(self):
		return self.height

class Zoo:
	def __init__(self,name,max_mem):
		self.name =name
		self.max_mem = max_mem
		self.animals = []

	def add_ani(self,anim):
		if len(self.animals) < self.max_mem:
			self.animals.append(anim)
			return True
		return False

	def get_average(self):
		val =0
		for anim in self.animals:
			val+=anim.get_height()
		return val/len(self.animals)
a1 = Animal('Lion','Ochre',3)
a2 = Animal('Cheetah','Orange',4)

z =Zoo('Cat',2)
z.add_ani(a1)
z.add_ani(a2)

print(z.animals[0].name)
print(z.get_average())'''


# Inheritance
'''class Pet:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):
	
	To add new attributes and retain the old one 
	we can use super function
	def __init__(self,name,age,colour):
		super().__init__(name,age)  
		self.colour = colour

	def sound(self):
		print("Meow")

class Dog:
	def sound(self):
		print("Bark")


c1 = Cat('Tom',2,'Black')

#Dog.sound('Tom')

print(c1.colour)

print(isinstance(c1,Cat))'''


class Change:
	instances = 0
	def __init__(self,name):
		self.name = name
		Change.add_value()


	@classmethod
	def value(cls):
		return cls.instances

	@classmethod
	def add_value(cls):
		cls.instances += 1

ch = Change('Bobby')
ch2 = Change('Balu')
ch3 = Change('Arun')
print(Change.value())