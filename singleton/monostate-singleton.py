# sample 1
class Borg:
	__shared_state = {"1":"2"}
	def __init__(self):
		self.x = 1
		self.__dict__ = self.__shared_state
		pass

b1 = Borg()
b2 = Borg()
b1.x = 4

print("b1 = ", b1)
print("b2 = ", b2)
print("b1 state = ", b1.__dict__)
print("b2 state = ", b2.__dict__)


# sample 2
class Berg(object):
	__shared_state = {}
	def __new__(cls, *args, **kwargs):
		obj = super(Berg, cls).__new__(cls, *args, **kwargs)
		obj.x =1
		obj.__dict__ = cls.__shared_state
		return obj

b3 = Berg()
b4 = Berg()
b3.x = 4

print("b3 = ", b3)
print("b4 = ", b4)
print("b3 state = ", b3.__dict__)
print("b4 state = ", b4.__dict__)
