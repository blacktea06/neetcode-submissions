class Solution:
    def trap(self, height: List[int]) -> int:

        N = len(height)

        p1, p2 = 0, N-1
        maxL, maxR = 0, 0
        water = 0

        while p1 < p2:
            if ((maxL == maxR or maxL < maxR) and maxL - height[p1] > 0):
                water += maxL - height[p1]
                # print(f"water added to p1({p1}) is {maxL - height[p1]}")
            elif maxR < maxL and maxR - height[p2] > 0:
                water += maxR - height[p2]
                # print(f"water added to p2({p2}) is {maxR - height[p2]}")

            # print(f"When p1 is {p1} and p2 is {p2}, water is {water}")

            
            
            maxL = max(maxL, height[p1])
            maxR = max(maxR, height[p2])

            if maxL == maxR or maxL < maxR:
                p1 += 1
            else:
                p2 -= 1
        return water

                
        




    
        