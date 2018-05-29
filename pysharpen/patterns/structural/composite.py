"""
Module for demonstrating composite pattern
Problem:
1. Represent whole-part relationships.
"""
class AbstractRussianDoll(object):
    """ Abstract class representing russian doll aka Matryoshka"""
    def __init__(self, name, coloring):
        pass
        
    def unpack(self, indent = 0):
        pass

class ConcreteRussianDoll(AbstractRussianDoll):
    """Concrete russian doll with a name and coloring"""
    def __init__(self, name, coloring):
        self.name = name
        self.coloring = coloring
        
    def unpack(self, indent = 0):
        indentation = " "*indent    
        print("{2}I'm {0} in {1} colors".format(self.name, ",".join(self.coloring), indentation))

class CompositeRussianDoll(AbstractRussianDoll):
    """"Composite of russian dolls"""
    def __init__(self, name, coloring):
        self.name = name
        self.coloring = coloring
        self.baby_dolls = []   
    
    def add_doll(self, doll):
        self.baby_dolls.append(doll)
    
    def remove_doll(self, doll):
        if doll in self.baby_dolls:
            self.baby_dolls.remove(doll)
        for baby_doll in self.baby_dolls:
            baby_doll.remove_doll(doll)
    
    def unpack(self, indent = 0):
        indentation = " "*indent
        print("{2}I'm {0} in {1} colors".format(self.name, ",".join(self.coloring), indentation))
        for baby_doll in self.baby_dolls:
            baby_doll.unpack(indent = indent + 2)
    
def main():
    doll1 = CompositeRussianDoll("Mother Russia", ["white", "blue", "red"])
    doll2 = CompositeRussianDoll("Sister Belarus", ["green", "red"])
    doll3 = CompositeRussianDoll("Ukraine", ["blue", "yellow"])
    doll4 = ConcreteRussianDoll("Minsk", ["snow"])
    doll5 = ConcreteRussianDoll("Kiev", ["happiness"])
    doll1.add_doll(doll2)
    doll1.add_doll(doll3)
    doll2.add_doll(doll4)
    doll3.add_doll(doll5)
    doll1.unpack()
    
if __name__ == "__main__":
    main()