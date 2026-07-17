class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        char_freq = {}
        chars_seen = set()
        head = 0
        tail = 1
        max_len = 0

        chars_seen.add(s[head])
        char_freq[s[head]] = 1

        while tail < len(s):
            char_freq[s[tail]] = char_freq.get(s[tail], 0) + 1
            chars_seen.add(s[tail])

            temp_max = 0
            for ch in chars_seen:
                if char_freq[ch] > temp_max:
                    temp_max = char_freq[ch]
            window_size = tail - head + 1

            if window_size - temp_max <= k:
                tail += 1
                if window_size > max_len:
                    max_len = window_size
            else:
                char_freq[s[head]] -= 1
                if char_freq[s[head]] == 0:
                    chars_seen.remove(s[head])
                head += 1
                tail += 1
        return max_len