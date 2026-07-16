class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        freq_sorted = sorted(list(freq.items()), key=lambda x: x[1])[::-1]
        most_common = [x[0] for x in freq_sorted]
        return most_common[:k]