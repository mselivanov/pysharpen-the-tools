"""
Module demonstrated iterator pattern.
Problem:
1. Allow sequential access over object elements without exposing its internal structure.
"""

class Spaceship(object):
	def __init__(self, spaceship_type):
		self._spaceship_type = spaceship_type
	
	def __str__(self):
		return "Spaceship {0}".format(self._spaceship_type)
	
class MissileCruiser(Spaceship):
	def __init__(self):
		super().__init__("Missile Cruiser")

class Starfighter(Spaceship):
	def __init__(self):
		super().__init__("Starfighter")
		
class SpaceFleet(object):	
	class SpaceFleetIterator(object):
		def __init__(self, fleet):
			self._position = -1
			self._fleet = fleet
		
		def __iter__(self):
			return self
		
		def __next__(self):
			self._position += 1			
			if self._position > len(self._fleet._ships) - 1:
				raise StopIteration()
			return self._fleet._ships[self._position]

	def __init__(self):
		self._ships = []
	
	def add_to_fleet(self, spaceship):
		if spaceship not in self._ships:
			self._ships.append(spaceship)
	
	def remove_from_fleet(self, spaceship):
		if spaceship in self._ships:
			self._ships.remove(spaceship)
	
	def __iter__(self):
		return SpaceFleet.SpaceFleetIterator(self)	

def main():
	sf = SpaceFleet()
	ss1 = MissileCruiser()
	ss2 = Starfighter()
	sf.add_to_fleet(ss1)
	sf.add_to_fleet(ss2)
	for s in sf:
		print(s)
	
if __name__ == "__main__":
	main()