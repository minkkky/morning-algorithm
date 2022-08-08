# https://www.acmicpc.net/problem/10828

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def     __init__(self):
        self.head = None
    
    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        if self.empty():
            return -1
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def size(self):
        if self.head is None:
            return 0
        return self.head.count()

    def empty(self):
        if self.head is None:
            return 1
        return 0

    def top(self):
        if self.empty():
            return -1
        return self.head.data

stack = []

loop_cnt = int(input())

for i in range(loop_cnt):

    t = input().split(' ')
    order = t[0]

    if t[1]:
        value = t[1]

    if order == "push":
        stack.append(value)
    
    if order == "pop":
        stack.pop()

    if order == "size":
        stack.size()
    
    if order == "empty":
        stack.empty()
    
    if order == "top":
        stack.top()
    
    print(stack.data)
