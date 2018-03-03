"""
Module demonstrates adapter pattern.
Problem:
1. Need to convert class interface to interface client is expecting.
"""

from copy import deepcopy

class DarkForceSide(object):
    """ Class represents dark side of the force"""
    def __init__(self, dark_emotions, amount):
        self._dark_emotions = deepcopy(dark_emotions)
        self.amount = amount
    
    def use_dark_force(self):
        print("Gathering all {0} to use dark force!".format(", ".join(self._dark_emotions)))

class LightForceSide(object):
    """ Class represents light side of the force"""
    def __init__(self, inner_state, amount):
        self._inner_state = inner_state
        self.amount = amount
    
    def use_light_force(self):
        print("I'm in {0} state!".format(self._inner_state))
        

class ForceAdapter(object):
    """Adapter for using any kind of force"""
    def __init__(self, force, **adaptable_methods):
        self._force = force
        self.__dict__.update(adaptable_methods)
       
    def __getattr__(self, attr):
        """Redirects attribute access to underlying object"""
        return getattr(self._force, attr)

def main():
    dark_force = DarkForceSide(["anger", "envy"], 100)
    light_force = LightForceSide("no emotions", 123)
    forces = [ForceAdapter(dark_force, use_force = dark_force.use_dark_force), ForceAdapter(light_force, use_force = light_force.use_light_force)]
    for f in forces:
        f.use_force()
        print("Amount applied: {0}".format(f.amount))
        
if __name__ == "__main__":
    main()