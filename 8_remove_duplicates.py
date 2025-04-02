class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    curr_node = head

    while curr_node is not None:
        while curr_node.next is not None and curr_node.data == curr_node.next.data:
            curr_node.next = curr_node.next.next
        curr_node = curr_node.next

    return head
