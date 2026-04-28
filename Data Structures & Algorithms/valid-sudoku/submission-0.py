from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        zone_map = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                elem = board[row][col]
                if elem != ".":
                    if elem in row_map[row] or elem in col_map[col] or elem in zone_map[(row//3, col//3)]:
                        return False
                    row_map[row].add(elem)
                    col_map[col].add(elem)
                    zone_map[(row//3, col//3)].add(elem)
        return True