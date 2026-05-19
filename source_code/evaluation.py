from board import EMPTY, HUMAN, AI, DIRECTIONS


SCORES = {
    4: 100000,
    3: 1000,
    2: 100,
    1: 10,
}


def evaluate_board(board):
    
    winner = board.check_winner()
    if winner == AI:
        return 1000000
    if winner == HUMAN:
        return -1000000
    if winner == "DRAW":
        return 0

    total = 0
    n = board.size

    for r in range(n):
        for c in range(n):
            for dr, dc in DIRECTIONS:
                cells = []
                for k in range(4):
                    nr, nc = r + k * dr, c + k * dc
                    if not board.is_inside(nr, nc):
                        break
                    cells.append(board.grid[nr][nc])

                if len(cells) == 4:
                    total += score_window(cells)

    return total


def score_window(cells):
    ai_count = cells.count(AI)
    human_count = cells.count(HUMAN)
    empty_count = cells.count(EMPTY)

    if ai_count > 0 and human_count > 0:
        return 0

    if ai_count == 4:
        return SCORES[4]
    if human_count == 4:
        return -SCORES[4]

    if ai_count == 3 and empty_count == 1:
        return SCORES[3]
    if human_count == 3 and empty_count == 1:
        return -1500

    if ai_count == 2 and empty_count == 2:
        return SCORES[2]
    if human_count == 2 and empty_count == 2:
        return -SCORES[2]

    if ai_count == 1 and empty_count == 3:
        return SCORES[1]
    if human_count == 1 and empty_count == 3:
        return -SCORES[1]

    return 0
