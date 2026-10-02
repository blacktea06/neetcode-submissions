class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for i in range(len(nums)):
            # if map contains result of target - value output pair is found
            if (target - nums[i]) in map: # if key exists in map
                if i > map[target - nums[i]]:
                    return [map[target - nums[i]], i]
                else:
                    return [i, map[target - nums[i]]]
            else:
                map[nums[i]] = i # add num and index to obtain in future
