EMPTY = "."
HUMAN = "X"
AI = "O"

DIRECTIONS = [(1, 0), (0, 1), (1, 1), (1, -1)]


class Board:
    def __init__(self, size=9):
        if size < 9:
            raise ValueError("Board size must be at least 9.")
        self.size = size
        self.grid = [[EMPTY for _ in range(size)] for _ in range(size)]

    def clone(self):
        new_board = Board(self.size)
        new_board.grid = [row[:] for row in self.grid]
        return new_board

    def is_inside(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def is_empty(self, row, col):
        return self.is_inside(row, col) and self.grid[row][col] == EMPTY

    def make_move(self, row, col, player):
        if not self.is_empty(row, col):
            return False
        self.grid[row][col] = player
        return True

    def undo_move(self, row, col):
        if self.is_inside(row, col):
            self.grid[row][col] = EMPTY

    def is_full(self):
        return all(self.grid[r][c] != EMPTY for r in range(self.size) for c in range(self.size))

    def has_any_move(self):
        return any(self.grid[r][c] != EMPTY for r in range(self.size) for c in range(self.size))

    def check_winner(self):
        for r in range(self.size):
            for c in range(self.size):
                player = self.grid[r][c]
                if player == EMPTY:
                    continue
                for dr, dc in DIRECTIONS:
                    count = 1
                    nr, nc = r + dr, c + dc
                    while self.is_inside(nr, nc) and self.grid[nr][nc] == player:
                        count += 1
                        if count >= 4:
                            return player
                        nr += dr
                        nc += dc
        if self.is_full():
            return "DRAW"
        return None

    def get_candidate_moves(self, radius=1):
        """
        Sinh nước đi gần các quân đã đánh để giảm không gian tìm kiếm.
        Nếu bàn cờ trống, chọn ô trung tâm.
        """
        if not self.has_any_move():
            mid = self.size // 2
            return [(mid, mid)]

        moves = set()
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] != EMPTY:
                    for dr in range(-radius, radius + 1):
                        for dc in range(-radius, radius + 1):
                            nr, nc = r + dr, c + dc
                            if self.is_empty(nr, nc):
                                moves.add((nr, nc))

        center = self.size // 2
        return sorted(moves, key=lambda pos: abs(pos[0] - center) + abs(pos[1] - center))

    def display(self):
        print("   " + " ".join(str(i) for i in range(self.size)))
        for i, row in enumerate(self.grid):
            print(f"{i:2} " + " ".join(row))

    @classmethod
    def from_lines(cls, lines):
        size = len(lines)
        board = cls(size)
        for r, line in enumerate(lines):
            cells = line.strip().split()
            if len(cells) == size:
                board.grid[r] = cells
            else:
                board.grid[r] = list(line.strip())
        return board
