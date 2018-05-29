#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module contains strategy pattern example.

@author: mselivanov
"""

import types

class Strategy(object):
    """Strategy class"""
    def __init__(self, name, strategy_function = None):
        self._name = name
        
        if strategy_function:
            self.execute = types.MethodType(strategy_function, self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    def execute(self):
        print("Strategy {0}: I don't move".format(self.name))

def fight_strategy(self):
    self.name = "Fight"
    print("Strategy {0}: I'm going to fight!".format(self.name))

def main():
    s1 = Strategy("Freeze")
    s1.execute()
    s2 = Strategy("Fight", fight_strategy)
    s2.execute()

if __name__ == "__main__":
    main()
