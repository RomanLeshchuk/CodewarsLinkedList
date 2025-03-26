class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s == "None":
        return None

    arr_data = s.split(" -> ")
    res = Node(int(arr_data[0]))
    curr = res

    for i in range(1, len(arr_data) - 1):
        curr.next = Node(int(arr_data[i]))
        curr = curr.next

    return res
