"""
Module demonstrates visitor pattern.
Problem:
1. Add functionality to existing class hierarchy without changing it.
"""

class Planet(object):
    """ Plane class """
    def __init__(self, planet_name):
        self._planet_name = planet_name
        
    def accept(self, visitor):
        visitor.visit(self)
    
    def destroy_forests(self):
        print("Forests on {0} are destroyed".format(self._planet_name))
    
    def save_fresh_water(self):
        print("Fresh water on {0} is saved".format(self._planet_name))
    
    def welcome_visitor(self, visitor):
        print("Welcome {0} on {1}".format(visitor, self._planet_name))

class Visitor(object):
    def __init__(self, name):
        self._name = name
    
    def __str__(self):
        return self.name
    
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        self._name = name
        
class SpaceshipEnterprise(Visitor):
    def __init__(self):
        super().__init__("Enterprise NCC-1701")
    
    def visit(self, planet):
        planet.welcome_visitor(self)
        planet.save_fresh_water()
        
class Khan(Visitor):
    def __init__(self):
        super().__init__("Khan")

    def visit(self, planet):
        planet.welcome_visitor(self)
        planet.destroy_forests()

def main():
    planet = Planet("Diva")
    enterprise = SpaceshipEnterprise()
    khan = Khan()
    planet.accept(enterprise)
    planet.accept(khan)

if __name__ == "__main__":
    main()
    