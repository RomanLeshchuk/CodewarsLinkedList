class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    print(node.data)
    if node.data is not None:
        stringify(node.next)
