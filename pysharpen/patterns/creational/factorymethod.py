"""
Module demonstrates factory method pattern.
Problem:
1. Encapsulate object creation.
2. Type of object is determined in runtime.
"""

class Weapon(object):
	def __init__(self, weapon_type, number_of_shootings):
		self._weapon_type = weapon_type
		self._number_of_shootings = number_of_shootings
	
	def shoot(self):
		if self._number_of_shootings <= 0:
			print("{0} can't shoot. No more shootings.".format(self._weapon_type))
		else:
			self._number_of_shootings -= 1
			print("{0} shoots. {1} shootings left.".format(self._weapon_type, self._number_of_shootings))

class Shotgun(Weapon):
	def __init__(self, number_of_shootings):
		super().__init__("Shotgun", number_of_shootings)

class Rocket(Weapon):
	def __init__(self, number_of_shootings):
		super().__init__("Rocket", number_of_shootings)

def get_weapon(weapon_type):
	weapons = dict(Shotgun = Shotgun(5), Rocket = Rocket(3))
	return weapons[weapon_type]

def main():
	w1 = get_weapon("Shotgun")
	w1.shoot()
	w2 = get_weapon("Rocket")
	w2.shoot()
	
if __name__ == "__main__":
	main()