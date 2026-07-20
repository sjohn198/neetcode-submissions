class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, cur):
            #print(cur)
            if i == len(nums):
                res.append(cur.copy())
                return
            
            for j in range(len(cur)):
                #print(i,j)
                if cur[j] == "":
                    temp = cur[:j] + [nums[i]] + cur[j+1:]
                    dfs(i + 1, temp)

        dfs(0, [""] * len(nums))
        return res
    