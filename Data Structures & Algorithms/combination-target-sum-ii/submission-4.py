class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        res = []

        def dfs(i, cur, lst_sum):
            if lst_sum == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or lst_sum > target:
                return
            num = candidates[i]
            cur.append(num)
            dfs(i + 1, cur, lst_sum + num)
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, lst_sum)

        dfs(0, [], 0)
        return res