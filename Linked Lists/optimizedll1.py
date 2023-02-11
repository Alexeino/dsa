class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def takeInput():
    inputList = [int(ele) for ele in input("Enter values -> ").split(" ")]
    head = None
    tail = None
    for item in inputList:
        if item == -1:
            break
        newNode = Node(item)
        if head is None:
            head = newNode
            tail = head
        else:
            tail.next = newNode
            tail = tail.next
            # OR current = newNode works too.
        # print("current ",tail.data)
    return head

def printLinkedList(head):
    if head.next is None:
        return
    return printLinkedList(head.next)
def printLLWhile(head):
    while head is not None:
        print(str(head.data) + "->", end=" ")
        head =head.next
    print("None")

def length(head):
    counter = 0
    while head is not None:
        counter += 1
        head = head.next
    return counter
    
def printIthNode(head,i):
    if i >= length(head) or head is None:
        return
    for _ in range(i):
        head = head.next
    return head.data

def printIthNode2(head,i):

    if i>0:
        for x in range(i):
            if head is not None:
                head = head.next
        print(head.data)
    return

def insertatPos(head,i,data):

    if i < 0 or i >length(head):
        return head
    count = 0
    current = head
    prev = None
    newNode = Node(data)
    if i ==0:
        head = newNode
        newNode.next = current
    else:
        while count < i:
            # I reach ith position
            prev = current #will stay at i-1 th
            current = current.next # it will be on ith
            count += 1

        prev.next = newNode
        newNode.next = current

    return head

def deleteAtI(head,i):
    if i < 0 or i >= length(head):
        return head
    count = 0
    current = head
    prev = None

    if i==0:
        head = current.next
    
    else:
        while count < i:
            count += 1
            prev = current
            current = current.next
        # will put cursor at i-1 and ith position
        prev.next = current.next

    return head
 
def lengthRecursively(head):
    
    if head is None:
        return 0

    return 1 + lengthRecursively(head.next)

def insertAtIRecursive(head,i,data):

    if i == 0:
        newNode = Node(data)
        head = newNode.next
        return head

    return insertAtIRecursive(head.next,i-1,data)

if __name__ == "__main__":
    head = takeInput()
    # print(head.data)
    # print(head.next.data)
    # print(head.next.next.data)
    # printLinkedList(head)
    # printLLWhile(head)
    # print(length(head))
    # print(printIthNode(head,2))
    # printIthNode2(head,2)
    # head = insertatPos(head,5,10)
    # printLLWhile(head)
    # head = insertatPos(head,3,20)
    # printLLWhile(head)
    # head = deleteAtI(head,2)
    # printLLWhile(head)
    # head = deleteAtI(head,0)
    # printLLWhile(head)
    print(lengthRecursively(head))