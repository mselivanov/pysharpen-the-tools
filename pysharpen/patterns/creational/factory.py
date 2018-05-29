"""
Module contains examples on factory design pattern.
"""

import uuid
import names
import random

# Approach 1.
# Additional class with a class method returning instance of a produced class.
class StormTrooper(object):
    def __init__(self, personal_number, force_level):
        self.__personal_number = personal_number
        self.__force_level = force_level
    
    def __str__(self):
        return "Unit {personal_number} having {force_level} level of force".format(personal_number = self.personal_number, force_level = self.force_level)
    
    @property
    def personal_number(self):
        return self.__personal_number
    
    @property
    def force_level(self):
        return self.__force_level
    
    def report(self):
        print("Private {personal_number} is ready for your command".format(personal_number = self.personal_number))
        

class StormTrooperFactory(object):
            
    @classmethod
    def create(cls):
        return StormTrooper(str(uuid.uuid1()), 0)


# Approach 2.
# Factory class inside object class.
# StarWarsFactory calls create method of an inner Factory class. 
class Jedi(object):
    class Factory(object):
        def create(self):
            return Jedi(names.get_full_name(), random.randint(10, 100))
            
    def __init__(self, nickname, force_level):
        self.__nickname = nickname
        self.__force_level = force_level
    
    def __str__(self):
        return "{nickname} says: May the force be with you".format(nickname = self.nickname)
    
    @property
    def nickname(self):
        return self.__nickname
    
    @property
    def force_level(self):
        return self.__force_level
    
    def think(self):
        print("I'm {nickname}, I have {force_level} of force inside me".format(nickname = self.nickname, force_level = self.force_level))

class StarWarsFactory(object):
    __factories = {}
    
    @classmethod
    def add_factory(cls, character_name):
        cls.__factories[character_name] = eval("{character_name}.Factory()".format(character_name = character_name))    
    
    @classmethod
    def create(cls, character_name):
        if character_name not in cls.__factories:
            cls.add_factory(character_name)
        return cls.__factories[character_name].create()
        
def produce_units():
    unit = StormTrooperFactory.create()
    print(unit)
    
    jedi = StarWarsFactory.create("Jedi")
    print(jedi)

if __name__ == '__main__':
    produce_units()