class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        most_freq = sorted(list(freq.items()), key=lambda x: x[1])[::-1]
        return [x[0] for x in most_freq[:k]]