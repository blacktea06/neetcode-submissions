class Solution:
    def maxArea(self, heights: List[int]) -> int:

        N = len(heights)
        index1 = 0
        index2 = N-1
        maxA = 0

        while index1 < index2: #10
            bar1 = heights[index1]
            bar2 = heights[index2]

            width = index2 - index1
            height = min(bar1, bar2)
            maxA = max(maxA, height*width)

            if bar1 == height:
                index1 += 1
            else:
                index2 -= 1
        
        return maxA






        