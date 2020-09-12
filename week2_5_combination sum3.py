from itertools import combinations

class Solution:
    def combinationSum3(self, k, n):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ans = []
        for c in combinations(nums, k):
            if n == sum(c):
                print(c)
                ans.append(list(c))

        return ans
# Status: Accepted
# Algorithm: Brute Force
# Time Complexity: O(nCk)
# Runtime: 32ms (top 31.2%)
# Note: 오잉 그냥 브루트포스로 했는데도 충분한 런타임이 나온다. 오늘은 너무 힘들어서 여기까지만