"""
Module for demonstrating chain of responsibility pattern.
Problem:
1. Pass request to next handler in case you can't handle it.
"""

import math

class Handler(object):
	
	def handle(self, request):
		pass

class ForceUser(Handler):
	def __init__(self, name, force_level, successor):
		self._successor = successor
		self._force_level = force_level
		self._name = name
	
	@property
	def name(self):
		return self._name
	
	@property
	def force_level(self):
		return self._force_level
		
	@force_level.setter
	def force_level(self, value):
		self._force_level = value
	
	def handle(self, request):
		handled = self._handle(request)
		if not handled:
			self._successor.handle(request)
	
	def _handle(self, request):
		raise NotImplementedError("Must implement _handle method!")
	
	
class Luke(ForceUser):
	
	def __init__(self, successor):
		super().__init__("Luke Skywalker", 100, successor)
	
	def _handle(self, request):
		if request.force_level > self.force_level:
			print("{1} says: my force is weaker than force of {0}".format(request.name, self.name))		
			return False
		else:
			print("{1} says: Can fight with {0} myself".format(request.name, self.name))
			return True

class Joda(ForceUser):
	
	def __init__(self, successor):
		super().__init__("Joda", 300, successor)
	
	def _handle(self, request):
		if request.force_level > self.force_level:
			print("{1} says: my force is weaker than force of {0}".format(request.name, self.name))				
			return False
		else:
			print("{1} says: Can fight with {0} myself".format(request.name, self.name))
			return True

class MasterJedi(ForceUser):
	def __init__(self):
		super().__init__("Master", math.inf, None)
	
	def _handle(self, request):
		print("{2} says: Can fight with {0} myself cause my force {1}".format(request.name, self.force_level, self.name))
		return True

class DarkPadavan(ForceUser):
	def __init__(self):
		super().__init__("Dark Padavan", 100, None)


class DartVeider(ForceUser):
	def __init__(self):
		super().__init__("Dart Veider", 290, None)

class DarkEmperor(ForceUser):
	def __init__(self):
		super().__init__("Dark Emperor", 3000, None)
		
def main():
	jedi = Luke(Joda(MasterJedi()))
	darks = [DarkPadavan(), DartVeider(), DarkEmperor()]
	for dark in darks:
		jedi.handle(dark)

if __name__ == "__main__":
	main()