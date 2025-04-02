def loop_size(node):
    tortoise = node.next
    hare = node.next.next

    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next.next

    length = 1
    tortoise = tortoise.next
    hare = hare.next.next
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next.next
        length += 1

    return length
