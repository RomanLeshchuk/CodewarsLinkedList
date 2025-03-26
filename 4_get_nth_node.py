class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if index < 0:
        raise RuntimeError("Invalid index value should throw error.")

    if node is None:
        raise RuntimeError("None linked list should throw error.")

    while index:
        node = node.next

        if node is None:
            raise RuntimeError("Invalid index value should throw error.")

        index -= 1

    return node.data
