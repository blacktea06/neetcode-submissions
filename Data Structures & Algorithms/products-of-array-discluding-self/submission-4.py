class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        N = len(nums)
        prefix = [-1] * N
        product = 1

        for i in range(N):
            prefix[i] = product
            product *= nums[i]
        # print(f"input: {nums}")   
        # print(f"prefix : {prefix}")

        postfix = [-1] * N
        product = 1

        for i in range(N-1, -1, -1):
            postfix[i] = product
            product *= nums[i]
        
        # print(f"postfix: {postfix}")
        
        # Input :           [1, 2, 4, 6]
        # expected prefix:  [1, 1, 2, 8]
        # expected postfix: [48, 24, 6, 1]
        # expected output:  [48, 24, 12, 8]

        # calculations

        output = [-1] * N

        for i in range(N):
            output[i] = prefix[i] * postfix[i]

        return output
    

        
