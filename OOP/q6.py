class Stack:
    def __init__(self):
        self.items =[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "cannot pop from an empty stack"
        
    def is_empty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Empty stack"
        
stack = Stack()

stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)

print("Stack Size", stack.size())
print("Top Element",stack.peek())

popped_items = stack.pop()
print("\nPopped item:", popped_items)
print("\nStack size:", stack.size())
print("Top element:", stack.peek())

stack1 = Stack()
print("\nStack size:", stack1.size())
popped_item = stack1.pop()
print("\nPopped item:", popped_item) 