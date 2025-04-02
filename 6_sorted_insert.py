class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    if head is None or data < head.data:
        new_node = Node(data)
        new_node.next = head
        return new_node

    curr_node = head

    while curr_node.next is not None:
        if data < curr_node.next.data:
            new_node = Node(data)
            new_node.next = curr_node.next
            curr_node.next = new_node
            break
    else:
        curr_node.next = Node(data)

    return head
