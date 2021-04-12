class Singleton(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance

s1 = Singleton()
print("create 1 = ", s1)

s2 = Singleton()
print("create 2 = ", s2)
