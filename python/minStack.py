class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c=='+':
                stack.append(stack.pop()+stack.pop())
            elif c=='-':
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif c=='*':
                stack.append(stack.pop()*stack.pop())

            elif c=='/':
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()