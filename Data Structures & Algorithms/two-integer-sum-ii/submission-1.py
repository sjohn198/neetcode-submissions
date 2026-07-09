class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1

        while True:
            s = numbers[head] + numbers[tail]

            if s > target:
                tail -= 1
            elif s < target:
                head += 1
            else:
                return [head + 1, tail + 1]