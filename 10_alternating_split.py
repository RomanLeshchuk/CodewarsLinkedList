class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    def recursion_split(head):
        if head is None or head.next is None:
            res = Context(head, None)
            if head.next is not None:
                res.second = head.next
                head.next = None
            return res

        curr_res = Context(head, head.next)
        next_res = recursion_split(head.next.next)
        curr_res.first.next = next_res.first
        curr_res.second.next = next_res.second

        return curr_res

    if head is None or head.next is None:
        raise RuntimeError("Start list should have at least two elements")

    return recursion_split(head)
