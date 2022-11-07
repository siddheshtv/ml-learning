class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linkedlist(head):
    if(head == 'None'):
        return
    print(head.data)
    print(head.next)

if __name__ == '__main__':
    start = Node("Sarthak")
    n1 = Node("Shivani")
    start.next = n1
    n2 = Node("tejas")
    n1.next = n2
    n3 = Node("Rohit")
    n2.next = n3

linkedlist(start)