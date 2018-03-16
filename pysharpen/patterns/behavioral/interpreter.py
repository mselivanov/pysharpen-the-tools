"""
Module demonstrates interpreter pattern.
"""
from abc import ABC, abstractmethod

class AbstractExpression(object):
    def __init__(self):
        pass

    @abstractmethod
    def interpret(self):
        pass

class NonTerminalExpression(AbstractExpression):
    def __init__(self, expression):
        super().__init__()
        self._expression = expression
    
    def interpret(self):
        print("Interpreting non-terminal ...")
        self._expression.interpret()

class TerminalExpression(AbstractExpression):
    def __init__(self):
        super().__init__()
    
    def interpret(self):
        super().__init__()    
        print("Interpreting terminal ...")

def main():
    expr = NonTerminalExpression(NonTerminalExpression(TerminalExpression()))
    expr.interpret()

if __name__ == "__main__":
    main()