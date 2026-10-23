class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        N = len(nums)
        nums.sort()
        final = []

        #print(nums)

        for i in range(N):
            cur = nums[i]
            pointer1 = i+1
            pointer2 = N-1

            # if i == pointer1:
            #     break

            while pointer1 < pointer2:
                sum = cur + nums[pointer1] + nums[pointer2]
                if sum == 0 and [cur, nums[pointer1], nums[pointer2]] not in final:
                    final.append([cur, nums[pointer1], nums[pointer2]])
                    pointer1 += 1
                elif sum > 0:
                    pointer2 -= 1
                else:
                    pointer1 += 1
        
        return final



                    









        
        