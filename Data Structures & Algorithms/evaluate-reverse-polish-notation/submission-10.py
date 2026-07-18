class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        possible_opps = {"*", "+", "-", "/"}
        number_stack = []

        for t in tokens:
            print(t)
            print(number_stack)
            if t in possible_opps:
                op1 = int(number_stack.pop(-1))
                op2 = int(number_stack.pop(-1))
                if t == "+":
                    number_stack.append(str(op1+op2))
                elif t == "-":
                    number_stack.append(str(op2-op1))
                elif t == "*":
                    number_stack.append(str(op1*op2))
                else:
                    number_stack.append(str(int(op2 / op1)))
            else:
                number_stack.append(t)
        #print(number_stack)
        return int(number_stack[-1])