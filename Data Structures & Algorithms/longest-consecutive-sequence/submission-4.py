class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        N = len(nums)
        count = 1
        nums = sorted(nums)
        prev = nums[0]
        record = set()

        # print(sorted(nums))

        for i in range(N):
            cur = nums[i]

            if prev == cur:
                prev = cur
                continue
            if cur - prev == 1:
                count += 1
            else:
                record.add(count) # store that record to later find highest rec in set
                count = 1 # reset count
            
            prev = cur
        
        record.add(count)
        record = sorted(record)
        return record[-1]


        