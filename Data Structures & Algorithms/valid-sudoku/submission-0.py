from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        N = len(board)

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        cube = collections.defaultdict(set)

        for r in range(N):
            for c in range(N):
                cell = board[r][c]

                if cell == ".":
                    continue
                    
                if (cell in rows[r] or
                    cell in cols[c] or
                    cell in cube[(r//3, c//3)]): # cubes index from 0-3 so if r = 9, and c = 3 the cell is at index (3, 1)
                    return False # can't have same num in any row, col, or 3x3
                
                rows[r].add(cell)
                cols[c].add(cell)
                cube[(r//3, c//3)].add(cell)
        
        return True
                


        