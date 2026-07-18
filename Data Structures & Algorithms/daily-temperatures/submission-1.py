class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            # print(results)
            # print(i,t)
            # print(stack)
            if stack == []:
                stack.append((i, t))
                #print(f"filling stack: {stack}")
            else:
                if t > stack[-1][1]:
                    #print("cleaning stack")
                    while stack != [] and t > stack[-1][1]:
                        #print(stack)
                        remove = stack.pop(-1)
                        results[remove[0]] = i - remove[0]
                    stack.append((i, t))
                    #print(f"done cleaning: {stack}")
                else:
                    stack.append((i, t))
                    #print(f"filling stack: {stack}")
        return results