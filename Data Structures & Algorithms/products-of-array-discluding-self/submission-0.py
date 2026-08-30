class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        counter = 1
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            prefix[i] = counter
            counter = counter * nums[i]

        counter = 1
        postfix = [0] * len(nums)
        for i in range(len(nums))[::-1]:
            print(counter)
            postfix[i] = counter
            counter = counter * nums[i]
        
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = postfix[i] * prefix[i]
    
            
        
        return result