"""
Module demonstrates algorithm for solving dynamic connectivity problem.
Two algorithms are demonstrated:
    - quick find
    - quick union

Quick find: all objects store id of a component they all belong to.
    Find operation: check if component id of one object is equal to id of another object.
    Union operation: set id of component p to id of component q.

Quick union: all objects contain link to parent component. Root component point to itself.
    Find operation: check if roots for objects are equal.
    Union operation: set parent for root of component p to root of component q.

Improvements:
    1. Weighting. Keep track of tree size in quick union algorithm. Always connect smaller tree to larger tree.
    2. Path compression. Keep link to root from all nodes on the path.

"""

class UnionFind:
    """
    Class implements union-find algorithm.
    Objects must be hashable.
    """

    def __init__(self):
        "Class initialization"
        pass

    def union(self, obj1, obj2):
        "Make a connection between obj1 and obj2"
        pass

    def is_connected(self, obj1, obj2):
        """
        Check if obj1 and obj2 are connected
        Args:
            obj1 (object): first object to connect
            obj2 (object): second object to connect
        Returns:
            True - if objects are connected (directly or via other objects)
            False - if objects are not connected
        """
        pass
