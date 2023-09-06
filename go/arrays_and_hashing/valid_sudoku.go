package main

type Key struct {
    r int
    c int
}

func isValidSudoku(board [][]byte) bool {
    rows := [9]map[byte]bool{}
    columns := [9]map[byte]bool{}
    cells := map[Key]map[byte]bool{}

    for r, _ := range board {
        for c, _ := range board[r] {
            val := board[r][c]

            if val == '.' {
                continue
            }

            _, rowExists := rows[r][val]
            _, columnExists := columns[c][val]
            _, cellExists := cells[Key{r / 3, c / 3}][val]

            if rowExists || columnExists || cellExists {
                return false
            }

            if rows[r] == nil {
                rows[r] = map[byte]bool{}
            }
            rows[r][val] = true

            if columns[c] == nil {
                columns[c] = map[byte]bool{}
            }
            columns[c][val] = true

            key := Key{r / 3, c / 3}
            if cells[key] == nil {
                cells[key] = map[byte]bool{}
            }
            cells[key][val] = true
        }
    }

    return true
}

