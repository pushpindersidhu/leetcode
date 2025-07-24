from typing import List, Set


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(self.validateColumns(board))

        return (
            self.validateRows(board)
            and self.validateColumns(board)
            and self.validateSubgrids(board)
        )

    def validateRows(self, board: List[List[str]]) -> bool:
        for row in board:
            hashset = set()
            for cell in row:
                if not self.validateCell(cell, hashset):
                    return False

        return True

    def validateColumns(self, board: List[List[str]]) -> bool:
        for col in range(9):
            hashset = set()
            for row in range(9):
                cell = board[row][col]
                if not self.validateCell(cell, hashset):
                    return False

        return True

    def validateSubgrids(self, board: List[List[str]]) -> bool:
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                hashset = set()
                for subrow in range(row, row + 3):
                    for subcol in range(col, col + 3):
                        cell = board[subrow][subcol]
                        if not self.validateCell(cell, hashset):
                            return False

        return True

    def validateCell(self, cell: str, hashset: Set[str]) -> bool:
        if cell == ".":
            return True

        if cell in hashset:
            return False

        hashset.add(cell)

        return True
