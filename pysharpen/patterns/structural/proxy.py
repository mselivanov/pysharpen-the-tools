"""
Module demonstrates proxy pattern.
Problem:
1. Avoid object creation until it's really necessary (useful when object creation is very costly).
"""

class DarkEmperor(object):
    """Producing Dark Emperor is very expensive.
    Emperor is almost always busy playing with dark force.
    """
    def meet(self):
        print("Meeting Dark Emperor!!!")
    
class EmperorProxy(object):
    __ATTEMPTS_THRESHOLD = 10
    
    """Emperor proxy"""
    def __init__(self):
        self._is_emperor_busy = True
        self._emperor = None
        self._nr_attempts = 0
    
    def meet(self):
        if not self._is_emperor_busy:
            if not self._emperor:
                self._emperor = DarkEmperor()
            self._emperor.meet()
            self._is_emperor_busy = True
            self._nr_attempts = 0
        else:
            print("Emperor is busy! Wait!")
            self._nr_attempts += 1
            if self._nr_attempts > self.__ATTEMPTS_THRESHOLD:
                self._is_emperor_busy = False
            
if __name__ == "__main__":
    ep = EmperorProxy()
    for i in range(15):
        ep.meet()