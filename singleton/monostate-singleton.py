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
