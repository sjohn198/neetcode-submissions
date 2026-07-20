class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        cur = []
        def dfs(i):
            #print(cur, sum(cur))
            if sum(cur) == target:
                #print(f"found one!, {cur}")
                res.append(cur.copy())
                return
            if i >= len(nums) or sum(cur) > target:
                return
            temp = nums[i]
            cur.append(temp)
            dfs(i)
            cur.pop()
            dfs(i+1)
            #print(res)
        
        dfs(0)
        return res