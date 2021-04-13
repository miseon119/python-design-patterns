class Singleton:
	__instance = None
	def __init__(self):
		if not Singleton.__instance:
			print("__init__ called ")
		else:
			print("Instance already created ", self.getInstance())

	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance = Singleton()
		return cls.__instance

#just initialize object but not construct
s1 = Singleton()

# construct Singleton object
print("object created", Singleton.getInstance())

s2 = Singleton()
