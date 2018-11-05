class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = node
        return self
    
    def removeNode(self, value):
        runner = self.head
        if runner.value == value:
            self.head = self.head.next
            return self
        while ((runner.next != None) and (runner.next.value != value)):
            runner = runner.next
        if (runner.next == None):
            return self
        if (runner.next.value == value):
            runner.next = runner.next.next
        return self 

    def printAllValues(self, msg=""):
        runner = self.head
        print(f"\n\nHead points to {id(self.head)}")
        print(f"Printing the values in the list ---{msg}---")
        while (runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))

print("\n\n\n========== START OF THE PROGRAM =========")
list = SList(5)

list.addNode(7).addNode(9).addNode(1).printAllValues("Added 7, 9, 1")

#list.removeNode(1).printAllValues("Post deletion of end node")
#list.removeNode(5).printAllValues("Post deletion of first node")
#list.removeNode(7).printAllValues("Post deletion of middle node")
list.removeNode(9).printAllValues("Post deletion of another middle node")