class Solution:
    def search(self, nums: List[int], target: int) -> int:

        N = len(nums)
        if ((N == 1 and nums[0] != target) or N == 0): return -1 # edge cases
        if target > nums[-1] or target < nums[0]: return -1
        
        dist = min(nums[0]-target, nums[-1]-target)
        index = 0
        l, r = False, False

        if dist == nums[0]-target or nums[0]-target == nums[-1]-target:
            l = True
            index = 0  

            while nums[index] < target:
                    index += 1
            
            if nums[index] == target:
                return index
            else:
                return -1

        elif dist == nums[-1]-target:
            r = True
            index = N-1

            while nums[index] > target:
                    index -= 1
            
            if nums[index] == target:
                return index
            else:
                return -1

        
        return -1






               