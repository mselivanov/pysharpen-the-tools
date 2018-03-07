"""
Module for demonstrating prototype design pattern
"""

import copy

class Prototype(object):
    """
    Class implements object prototyping
    """
    def __init__(self):
        self.__prototypes = {}
    
    def register_prototype(self, prototype_name, obj):
        """Method saves obj prototype using prototype_name"""
        self.__prototypes[prototype_name] = obj
    
    def unregister_prototype(self, prototype_name):
        """Method saves obj prototype using prototype_name"""
        del self.__prototypes[prototype_name]
    
    def clone(self, prototype_name, **args):
        """ Method makes deep copy of prototyped object and updates object attributes"""
        obj = copy.deepcopy(self.__prototypes[prototype_name])
        obj.__dict__.update(args)
        return obj

class StarTrooper(object):
    def __init__(self, name, personal_number, weight, height, skills):
        self.name = name
        self.personal_number = personal_number
        self.weight = weight
        self.height = height 
        self.skills = copy.deepcopy(skills)
    
    def __str__(self):
        return "Name: {0}\nPersonal number: {1}\nWeight: {2}\nHeight: {3}\nSkills: {4}".format(self.name, 
            self.personal_number, 
            self.weight, 
            self.height, 
            ", ".join(self.skills))

if __name__ == "__main__":
    prototype = Prototype()
    st1 = StarTrooper("Jack Black", "X0102", 75, 1.82, ["Laser weapon", "Surviving in jungles"])
    prototype.register_prototype("Surviver", st1)
    st2 = prototype.clone("Surviver", **{"name": "Andrew First"})
    print(st1)
    print(st2)