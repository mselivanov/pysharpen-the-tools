"""
Module demonstrates memento pattern.
Problem:
1. Store transaction history of other object.
"""
import pickle
from copy import deepcopy

class Table(object):
    def __init__(self, columns_list):
        self._data = []
        self._columns_list = deepcopy(columns_list)
    
    def __str__(self):
        return str(self._data)
    
    def insert(self, row):
        self._data.append(row)
    
    def delete(self, where_clause):
        result = []
        for row in self._data:
            if not where_clause(row):
                result.append(row)
        self._data = result
    
    def get_checkpoint(self):
        return pickle.dumps(vars(self))
    
    def rollback_to_checkpoint(self, checkpoint):
        prev_state = pickle.loads(checkpoint)
        vars(self).clear()
        vars(self).update(prev_state)

def main():
    t = Table(["customer_id", "customer_name"])
    t.insert({"customer_id":1, "customer_name": "Bill Gates"})
    t.insert({"customer_id":2, "customer_name": "Warren Buffet"})
    cp = t.get_checkpoint()
    print("Checkpoint: " + str(t))
    t.delete(lambda row: 1 == 1)
    print("After delete: " + str(t))
    t.rollback_to_checkpoint(cp)
    print("After rollback: " + str(t))
    
    

if __name__ == "__main__":
    main()
                
    
