class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        res = Context(head, head.next)
        if res.first.next is not None:
            res.first.next = None
        return res

    curr_res = Context(head, head.next)
    next_res = alternating_split(head)
    curr_res.first.next = next_res.first
    curr_res.second.next = next_res.second

    return curr_res
