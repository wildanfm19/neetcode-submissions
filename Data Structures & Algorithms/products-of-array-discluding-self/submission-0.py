class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = {}  
        
        
        for i , n in enumerate(nums):
            count[i] = count.get(i , 0) + n

        res = []
        k = 0
        for i in range(len(nums)):
            prefix = 1
            for  j in range(len(nums)):
                if j == i:
                    continue
                prefix *= count[j]
            res.append(prefix)
        return res


            

        
            

    
        