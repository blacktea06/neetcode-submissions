class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}

        # add each elem to hashmap with counter

        for n in nums:
            if n in map:
                map[n] = map.get(n) + 1 # increase numbers counter by 1
            else:
                map[n] = 1 # add num to map with starting counter of 1

        # sorts map by keys with highest value then I return k keys with highest values

        top = sorted(map.items(), key=lambda x: x[1], reverse=True)
        return [num for num, count in top[:k]] # returns the  k elements in map 
