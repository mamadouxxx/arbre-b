import graphviz
from Node import Node
from BTree import Btree


class Visualization() :
    
    def __init__(self, btree):
        self.btree = btree
        self.g = graphviz.Graph()
        self.add_node_to_graph(self.btree.root)
        
    def add_node_to_graph(self, node):
        nodeKeys = repr(node.keys)
        self.g.node(nodeKeys)
        for child in node.childs:
            childKeys = repr(child.keys)
            self.g.node(childKeys)
            self.g.edge(nodeKeys, childKeys)
            self.add_node_to_graph(child)
            
    def render(self):
        self.g.format = 'jpg'
        self.g.render(directory='ArbreB', view=True)
            