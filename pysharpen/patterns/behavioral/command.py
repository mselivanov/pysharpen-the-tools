"""
Module demonstrates command pattern.
"""

class Command(object):
    def __init__(self, command_object):
        self.command_object = command_object
        
    def execute(self):
        raise NotImplementedError()

class PutOnOven(Command):
    def execute(self):
        self.command_object.put_on_oven()

class TurnOn(Command):
    def execute(self):
        self.command_object.turn_on()
        
class BreakEgg(Command):
    def execute(self):
        self.command_object.break_egg()
        
class Pan(object):
    def put_on_oven(self):
        print("Putting pan on oven...")

class Oven(object):
    def turn_on(self):
        print("Turning oven on...")        

class Egg(object):
    def break_egg(self):
        print("Breaking an egg...")

class Cooker(object):
    def __init__(self):
        self._program = []
    
    def add_to_program(self, command):
        self._program.append(command)
        return self
    
    def execute_program(self):
        for command in self._program:
            command.execute()

def main():
    pan = Pan()
    oven = Oven()
    egg = Egg()
    cooker = Cooker()
    cooker.add_to_program(PutOnOven(pan)).add_to_program(TurnOn(oven)).add_to_program(BreakEgg(egg))
    cooker.execute_program()

if __name__ == "__main__":
    main()
        