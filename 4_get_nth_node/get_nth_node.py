class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if index < 0:
        raise RuntimeError("Invalid index value")

    if node is None:
        raise RuntimeError("None linked list")

    while index:
        node = node.next

        if node is None:
            raise RuntimeError("Invalid index value")

        index -= 1

    return node
