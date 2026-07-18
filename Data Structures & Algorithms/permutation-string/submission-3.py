class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or s2 == "":
            return False
        if s1 == "":
            return True
        if len(s1) == 1:
            return s1[0] in s2
        head = 0
        tail = 1

        ch2find = set(list(s1))
        #print(ch2find)
        while tail < len(s2):
            print(head, tail, s2[head], s2[tail])
            if s2[tail] not in ch2find or s2[head] not in ch2find:
                head += 1
                tail += 1
            else:
                # print("letters match!")
                # print(tail - head + 1)
                # print(len(s1))
                if tail - head + 1 < len(s1):
                    tail += 1
                elif tail - head + 1 == len(s1):
                    # print("lengths match")
                    # print(f"Perm: {s2[head:tail+1]}, Source: {s1}")
                    if sorted(s2[head:tail+1]) == sorted(s1):
                        return True
                    else:
                        head += 1
                        tail += 1
        return False