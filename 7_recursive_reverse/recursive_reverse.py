class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None or head.next is None:
        return head

    pre_last_node = None
    last_node = head
    while last_node.next is not None:
        pre_last_node = last_node
        last_node = last_node.next

    if pre_last_node is not None:
        pre_last_node.next = None

    last_node.next = reverse(head)

    return last_node
