class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def takeInput():
    inputList = [int(ele) for ele in input("Enter values -> ").split(" ")]
    head = None
    for item in inputList:
        if item == -1:
            break
        newNode = Node(item)
        if head is None:
            head = newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
    return head

def printLinkedList(head):
    print(head.data)
    if head.next is None:
        return
    return printLinkedList(head.next)
def printLLWhile(head):
    while head is not None:
        print(str(head.data) + "->", end=" ")
        head =head.next
    print("None")

if __name__ == "__main__":
    head = takeInput()
    # print(head.data)
    # print(head.next.data)
    # print(head.next.next.data)
    # printLinkedList(head)
    printLLWhile(head)
