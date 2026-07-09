class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, l_count, r_count):
            if r_count > l_count or (len(cur) > 0 and cur[0] == ")") or (len(cur) == 2 * n and l_count != r_count):
                return
            if len(cur) == 2 * n and l_count == r_count:
                res.append(cur)
                return

            dfs(cur + "(", l_count + 1, r_count)
            dfs(cur + ")", l_count, r_count + 1)

        dfs("", 0, 0)
        return res