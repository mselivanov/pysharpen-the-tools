"Module demonstrates breadth-first search algorithm"
from collections import deque
import unittest

class Node:
    "Class implements graph node"

    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        "Node data"
        return self._data

    @data.setter
    def data(self, value):
        "Set node data"
        self._data = value 

class Edge:
    "Class implements graph edge"
    def __init__(self, from_node, to_node, weight):
        "Inits edge connecting two nodes"
        self._from_node = from_node
        self._to_node = to_node
        self._weight = weight

    @property
    def from_node(self):
        "Edge from node"
        return self._from_node
    
    @property
    def to_node(self):
        "Edge to node"
        return self._to_node

    @property
    def weight(self):
        "Edge weight"
        return self._weight

class Graph:
    "Class implements graph"

    def __init__(self, directed):
        self._graph = {}
        self._directed = directed

    def _connected_nodes(self, from_node):
        return (edge.to_node for edge in self._graph[from_node])

    def add_node(self, node):
        "Adds node to graph"
        if node in self._graph:
            raise ValueError('Node is already in graph')
        self._graph[node] = [] 

    def connect(self, from_node, to_node, weight):
        "Connect two nodes"
        if not from_node in self._graph:
            self.add_node(from_node)
        if not to_node in self._graph:
            self.add_node(to_node)
        if to_node in self._connected_nodes(from_node):
            return
        edge = Edge(from_node, to_node, weight)
        self._graph[from_node].append(edge)
        if not self._directed:
            self.connect(to_node, from_node, weight)

    def is_path_exists(self, from_node, to_node):
        search_path = deque(self._graph[from_node])
        searched_edges = {}
        
        while search_path:
            edge = search_path.popleft()
            if not edge in searched_edges:
                if edge.to_node == to_node:
                    return True
                else:
                    searched_edges[edge] = True
                    search_path.extend(self._graph[edge.to_node])
        return False

class GraphTest(unittest.TestCase):
    "Class for testing graph"
    def test_two_node_undirected_graph(self):
        graph = Graph(directed=False)
        node1 = Node(None)
        node2 = Node(None)
        graph.connect(node1, node2, 1)
        self.assertTrue(graph.is_path_exists(node1, node2))
        self.assertTrue(graph.is_path_exists(node2, node1))

    def test_three_node_directed_graph(self):
        graph = Graph(directed=True)
        node1 = Node(None)
        node2 = Node(None)
        node3 = Node(None)
        graph.connect(node1, node2, 1)
        graph.connect(node2, node3, 1)
        self.assertTrue(graph.is_path_exists(node1, node3))

    def test_three_node_directed_graph_with_cycle(self):
        graph = Graph(directed=True)
        node1 = Node(None)
        node2 = Node(None)
        node3 = Node(None)
        graph.connect(node1, node2, 1)
        graph.connect(node2, node3, 1)
        graph.connect(node3, node1, 1)
        self.assertTrue(graph.is_path_exists(node1, node3))

    def test_three_node_path_not_exists(self):
        graph = Graph(directed=True)
        node1 = Node(None)
        node2 = Node(None)
        node3 = Node(None)
        graph.connect(node1, node2, 1)
        graph.add_node(node3)
        self.assertFalse(graph.is_path_exists(node1, node3))

if __name__ == '__main__':
    unittest.main()
