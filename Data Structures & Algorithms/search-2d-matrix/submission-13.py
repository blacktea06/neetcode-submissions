class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0

        while r+1 < len(matrix) and target > matrix[r][-1]: # while target isn't in row # target = 12
            r += 1

        row = matrix[r]
        p1, p2 = 0, len(matrix[r])-1
        
        while p1 <= p2:
            mid = (p1+p2)//2
            print(f"mid: {mid}")
            if row[mid] == target:
                return True
            if row[mid] < target:
                p1 = mid + 1
            else:
                p2 = mid - 1
        return False



        




        