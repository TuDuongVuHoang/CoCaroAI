import time
from board import HUMAN, AI
from evaluation import evaluate_board


class AIResult:
    def __init__(self, move, score, states, elapsed_ms):
        self.move = move
        self.score = score
        self.states = states
        self.elapsed_ms = elapsed_ms


class CaroAI:
    def __init__(self, depth=2, algorithm="alphabeta", candidate_radius=1):
        self.depth = depth
        self.algorithm = algorithm
        self.candidate_radius = candidate_radius
        self.states = 0

    def choose_move(self, board):
        self.states = 0
        start = time.perf_counter()

        if self.algorithm == "minimax":
            score, move = self._minimax_root(board)
        elif self.algorithm == "alphabeta":
            score, move = self._alphabeta_root(board)
        else:
            raise ValueError("algorithm must be 'minimax' or 'alphabeta'.")

        elapsed_ms = (time.perf_counter() - start) * 1000
        return AIResult(move, score, self.states, elapsed_ms)

    def _minimax_root(self, board):
        best_score = float("-inf")
        best_move = None

        for move in board.get_candidate_moves(self.candidate_radius):
            r, c = move
            board.make_move(r, c, AI)
            score = self._minimax(board, self.depth - 1, maximizing=False)
            board.undo_move(r, c)

            if score > best_score:
                best_score = score
                best_move = move

        return best_score, best_move

    def _minimax(self, board, depth, maximizing):
        self.states += 1

        winner = board.check_winner()
        if winner is not None or depth == 0:
            return evaluate_board(board)

        moves = board.get_candidate_moves(self.candidate_radius)

        if maximizing:
            best = float("-inf")
            for r, c in moves:
                board.make_move(r, c, AI)
                best = max(best, self._minimax(board, depth - 1, False))
                board.undo_move(r, c)
            return best
        else:
            best = float("inf")
            for r, c in moves:
                board.make_move(r, c, HUMAN)
                best = min(best, self._minimax(board, depth - 1, True))
                board.undo_move(r, c)
            return best

    def _alphabeta_root(self, board):
        best_score = float("-inf")
        best_move = None
        alpha = float("-inf")
        beta = float("inf")

        for move in board.get_candidate_moves(self.candidate_radius):
            r, c = move
            board.make_move(r, c, AI)
            score = self._alphabeta(board, self.depth - 1, alpha, beta, maximizing=False)
            board.undo_move(r, c)

            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)

        return best_score, best_move

    def _alphabeta(self, board, depth, alpha, beta, maximizing):
        self.states += 1

        winner = board.check_winner()
        if winner is not None or depth == 0:
            return evaluate_board(board)

        moves = board.get_candidate_moves(self.candidate_radius)

        if maximizing:
            value = float("-inf")
            for r, c in moves:
                board.make_move(r, c, AI)
                value = max(value, self._alphabeta(board, depth - 1, alpha, beta, False))
                board.undo_move(r, c)

                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            value = float("inf")
            for r, c in moves:
                board.make_move(r, c, HUMAN)
                value = min(value, self._alphabeta(board, depth - 1, alpha, beta, True))
                board.undo_move(r, c)

                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value
