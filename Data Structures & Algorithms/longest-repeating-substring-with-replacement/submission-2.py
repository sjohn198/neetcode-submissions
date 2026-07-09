class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_len = 0
        head = 0
        tail = 0

        while head < len(s) and tail < len(s):
            # print("f", freq)
            # print("tail", s[tail], tail)
            # print("head", s[head], head)
            if s[tail] not in freq:
                freq[s[tail]] = 1
            else:
                freq[s[tail]] += 1
            # print("f", freq)

            most_freq_count = sorted(list(freq.items()), key=lambda x: x[1])[::-1][0][1]
            # print(most_freq_count)
            if tail-head + 1 - most_freq_count > k:
                # print("too many different")
                freq[s[head]] -= 1
                head += 1
            else:
                if tail - head + 1 > max_len:
                    # print("new max_len")
                    max_len = tail - head + 1
            tail += 1
        return max_len


