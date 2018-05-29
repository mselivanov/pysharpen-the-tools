"""
Module for demonstrating builder pattern.
Problem:
1. Avoid telescoping constructors when trying to construct complex object.
"""

class Spaceshipyard(object):
	def __init__(self, builder):
		self._builder = builder
	
	def construct_spaceship(self):
		self._builder.build_spaceship()
		self._builder.add_body()
		self._builder.add_engine()
		self._builder.add_lasers()
		return self._builder._spaceship

class Builder(object):
	def __init__(self):
		self._spaceship = None
	
	def build_spaceship(self):
		self._spaceship = Spaceship()
		
class SpaceshipBuilder(Builder):
	def add_engine(self):
		self._spaceship._engine = "Warp engine"
	
	def add_lasers(self):
		self._spaceship._lasers = "Phasers"
	
	def add_body(self):
		self._spaceship._body = "Titan body"

class Spaceship(object):
	def __init__(self):
		self._engine = None
		self._lasers = None
		self._body = None
	
	def __str__(self):
		return "Spaceship. body: {0}, engine = {1}, lasers = {2}".format(self._body, self._engine, self._lasers)

def main():
	builder = SpaceshipBuilder()
	yard = Spaceshipyard(builder)
	spaceship = yard.construct_spaceship()
	print(spaceship)

if __name__ == "__main__":
	main()