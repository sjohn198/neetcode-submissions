"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        node_map = {}
        queue = [node]
        new_graph = Node(val=node.val)
        node_map[node] = new_graph
        while queue:
            cur_node = queue.pop(0)
            for n in cur_node.neighbors:
                if n in list(node_map.keys()):
                    node_map[cur_node].neighbors.append(node_map[n])
                else:
                    temp_node = Node(val=n.val)
                    node_map[cur_node].neighbors.append(temp_node)
                    node_map[n] = temp_node
                    queue.append(n)
        return new_graph
            
        