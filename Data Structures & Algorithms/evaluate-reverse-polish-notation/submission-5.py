class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        numstack = []

        while tokens != []:
            print(numstack)
            tok = tokens.pop(0)
            print(tok)
            if tok == "+":
                op2 = numstack.pop()
                op1 = numstack.pop()
                numstack.append(int(op1) + int(op2))
            elif tok == "-":
                op2 = numstack.pop()
                op1 = numstack.pop()
                numstack.append(int(op1) - int(op2))
            elif tok == "*":
                op2 = numstack.pop()
                op1 = numstack.pop()
                numstack.append(int(op1) * int(op2))
            elif tok == "/":
                op2 = numstack.pop()
                op1 = numstack.pop()
                numstack.append(int(int(op1) / int(op2)))
            else:
                numstack.append(tok)
        return numstack[0]

        