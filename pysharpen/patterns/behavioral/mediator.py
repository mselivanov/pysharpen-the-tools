"""
Module demonstrates mediator pattern.
"""

class Node(object):
    def __init__(self, mediator, id):
        self._mediator = mediator
        self._node_id = id
    
    def get_node_id(self):
        return self._node_id
        
    def process(self, message):
        pass
        
    def send(self, message):
        pass
    
    def receive(self, message):
        pass

class DistributedDBNode(Node):
    def __init__(self, mediator, id):
        super().__init__(mediator, id)
        
    def process(self, message):
        print("Node {0} processing message: {1}".format(self._node_id, message))
        self.send(message)
    
    def send(self, message):
        print("Node {0} sending message: {1}".format(self._node_id, message))
        self._mediator.distribute(self, message)
    
    def receive(self, message):
        print("Node {0} received message: {1}".format(self._node_id, message))
        
class Mediator(object):
    def __init__(self):
        self._nodes = []
        
    def add_node(self, node):
        pass
        
    def distribute(self, sender, message):
        pass
        
class DBCoordinator(Mediator):
    def __init__(self):
        super().__init__()
    
    def add_node(self, node):
        self._nodes.append(node)
        return self
    
    def distribute(self, sender, message):
        for node in self._nodes: 
            if node.get_node_id() != sender.get_node_id():
                node.receive(message)

def main():
    coordinator = DBCoordinator()
    node1 = DistributedDBNode(coordinator, 1)
    node2 = DistributedDBNode(coordinator, 2)
    node3 = DistributedDBNode(coordinator, 3)
    coordinator.add_node(node1).add_node(node2).add_node(node3)
    node1.process("select * from F_SuperBigTable where event_dt = '2018-03-16'")

if __name__ == "__main__":
    main()