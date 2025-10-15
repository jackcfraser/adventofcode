#regular expressions
import re
from typing import List

class Action:
    def __init__(self, position, source):
        self.position = position
        self.source = source
        self.type = re.search(".+?(?=\\()", self.source).group()
        #print(self.type)

    def multiply(self):
        nums = re.findall("\\d+", self.source)
        a = int(nums[0])
        b = int(nums[1])
        return a*b
        

with open("3.txt") as file:
    contents = file.read()
    exp = re.compile("mul+\\([0-9]+,+[0-9]+\\)|do\\(\\)|don't\\(\\)")
    
    action_list = []

    for iter in exp.finditer(contents):
        #print(f"Found at {iter.start()}, group: {iter.group()}")
        action_list.append(Action(iter.start(), iter.group()))


    total_sum = 0
    state = True

    for action in action_list:
        if(action.type=="do"):
            state = True
            continue

        if(action.type=="don't"):
            state = False
            continue
        
        if(state):
            total_sum+=action.multiply()

    print(total_sum)

