class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #stack first in first out
        stack = []   
        for item in operations:
            if item == "C":
                stack.pop()
            elif item == "D":
                num = stack[-1]
                value = stack.append(num*2)
            elif item == "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(item))
        return sum(stack)
