class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if max(nums[i], nums[j]) - min(nums[i], nums[j]) <= t:
                    return True

        return False
# Algorithm: Brute Force
# Status: Time Limit Exceeded
# Time Complexity: O(n^2) (when k = n)


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        n = len(nums)
        bucket = {}
        for i in range(n):
            m = nums[i] // (t+1)
            if m in bucket:
                return True
            if m - 1 in bucket and abs(nums[i] - bucket[m - 1]) <= t:
                return True
            if m + 1 in bucket and abs(nums[i] - bucket[m + 1]) <= t:
                return True
            bucket[m] = nums[i]
            if i >= k: del bucket[nums[i - k] // (t+1)]
        return False
# Algorithm: Bucket Sort
# Status: Accepted
# Time Complexity: O(n lg(k))
# Runtime: 60ms (top 15.8%)

