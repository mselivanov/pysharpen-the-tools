"""
Module demonstrates state pattern.
Problem:
1. Implement different behavior depending on object state.
"""

class State(object):
    
    name = ""
    _allowed = []    
   
    def go_next(self, state):
        if state.name in self._allowed:
            print("Switching to: {0}".format(state.name))
            self.__class__ = state
        else:
            print("Switching to {0} from {1} isn't allowed".format(self.name, state.name))
    
    def __str__(self):
        return name

class Training(State):
    name = "training"
    _allowed = ["rest", "training", "dead"]

class Rest(State):
    name = "rest"
    _allowed = ["rest", "training", "dead"]

class Dead(State):
    name = "dead"
    _allowed = []

class Human(object):    
    _can_handle_trainings = 3

    def __init__(self, state):
        self._nr_of_training_changes = 0    
        self._current = state()    
    
    def set_state(self, state):
        next_state = state
        if self._current.name == state.name == Training.name:
            self._nr_of_training_changes += 1
            if self._nr_of_training_changes > Human._can_handle_trainings:
                next_state = Dead            
        self._current.go_next(next_state)
    
    def __str__(self):
        return "Human is in state: {0}".format(self._current.name)
        
def main():  
    h = Human(Rest)
    print(h)
    h.set_state(Training)
    print(h)
    h.set_state(Training)
    print(h)
    h.set_state(Training)
    print(h)
    h.set_state(Training)
    print(h)
    h.set_state(Training)
    print(h)
    

if __name__ == "__main__":
    main()
                
    
        