class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n # answer[i] will hold the left product first

        # Step 1: calculate left products
        left_prod = 1
        for i in range(n):
            answer[i] = left_prod
            left_prod *= nums[i]

        # Step 2: multiply by right products  
        right_prod = 1
        for i in range(n-1,-1,-1):
            answer[i] *= right_prod
            right_prod *= nums[i]
            
        return answer    

