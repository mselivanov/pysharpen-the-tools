"""
Module for demonstrating singleton pattern.
Problem:
1. Only one instance of an object must exist in runtime.
"""

class Borg(object):
	_shared_state = {}
	
	def __init__(self):
		self.__dict__ = Borg._shared_state

class Singleton(Borg):
	def __init__(self, **kwargs):
		super().__init__()
		self._shared_state.update(kwargs)
	
	def __str__(self):
		return "State: {0}".format(self._shared_state)
		
def main():
	s1 = Singleton(FTP = "File transfer protocol")
	print(s1)
	s2 = Singleton(HTTP = "Hyper text transfer protocol")
	print(s1)
	print(s2)
	
if __name__ == "__main__":
	main()