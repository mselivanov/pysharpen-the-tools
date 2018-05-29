"""
Module to demonstrate observer pattern.
Problem:
1. There is a subject and multiple observers.
2. Observers need to be notified when there is a change in subject.
"""

class Subject(object):
    """Abstract subject class"""
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError as e:
            print("Observer {1} is not found in observers list".format(observer))
    
    def notify(self, modifier = None):        
        for observer in self._observers:
            if observer != modifier:
                observer.update(self)
            

class UniverseForce(Subject):
    def __init__(self, force_level):
        super().__init__()
        self._force_level = force_level
    
    @property
    def force_level(self):
        return self._force_level
    
    @force_level.setter
    def force_level(self, value):
        self._force_level = value
        super().notify(self)

class Jedi(object):
    def __init__(self, name):
        self._name = name
    
    def update(self, subject):
        print("{0} says: time to check force. It's {1} now".format(self._name, subject.force_level))

class DarkLord(object):
    def __init__(self, name):
        self._name = name
    
    def update(self, subject):
        print("I, {0}, feel change in force. It's {1} now".format(self._name, subject.force_level))

def main():
    force = UniverseForce(1024)
    dv = DarkLord("Dart Veider")
    j = Jedi("Luke Skywalker")
    force.attach(dv)
    force.attach(j)
    force.force_level = 400
    force.force_level = 500
        
if __name__ == "__main__":
    main()