class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l] ,  res)
                break
            
            m = l + (r - l) // 2
            res = min(res , nums[m])
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r -= 1
        return res
            
       

             
        