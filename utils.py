def int_to_Roman(num):#https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def extractPositions(st):
        list0=st.split(',')
        lev=int(list0[0])
        co=int(list0[1])
        return lev,co

def extractPositionsTuple(st):
        list0=st.split(',')
        lev=int(list0[0])
        co=int(list0[1])
        pos=(lev,co)
        return pos

class Stack:#UC Berkeley CS188 Intro to AI -- Course Materials | Project 1 - Search | Link - http://ai.berkeley.edu/search.html
    "A container with a last-in-first-out (LIFO) queuing policy."
    #copied from pacman assignment
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0