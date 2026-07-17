class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1

        while True:
            total = numbers[head] + numbers[tail]
            if total == target:
                return [head+1, tail+1]
            if total > target:
                tail -= 1
            else:
                head += 1
                