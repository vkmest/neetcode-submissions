from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=defaultdict(set)
        for i in range(9):
            for j in range(9):
                cur=board[i][j]
                if cur==".": continue
                if cur in rows[i]:
                    return False
                rows[i].add(cur)
                if cur in cols[j]:
                    return False
                cols[j].add(cur)
                x=i//3
                y=j//3
                if cur in boxes[2**x*3**y]:
                    return False
                boxes[2**x*3**y].add(cur)
        return True