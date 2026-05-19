import csv
from board import Board
from ai import CaroAI


TEST_CASES = {
    "empty_board": [
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
        ".........",
    ],
    "ai_can_win": [
        ".........",
        ".........",
        ".........",
        "...OOO...",
        "...XX....",
        ".........",
        ".........",
        ".........",
        ".........",
    ],
    "human_must_be_blocked": [
        ".........",
        ".........",
        ".........",
        "...XXX...",
        "...OO....",
        ".........",
        ".........",
        ".........",
        ".........",
    ],
    "mid_game": [
        ".........",
        ".........",
        "...X.....",
        "...XO....",
        "...OXO...",
        "....X....",
        ".........",
        ".........",
        ".........",
    ],
    "both_attack": [
        ".........",
        ".........",
        "..OO.....",
        "...XX....",
        "....XO...",
        ".....O...",
        ".........",
        ".........",
        ".........",
    ],
}


def run_benchmark(depths=(1, 2, 3), output_file="benchmark_results.csv"):
    rows = []

    for state_name, lines in TEST_CASES.items():
        for depth in depths:
            board = Board.from_lines(lines)

            for algorithm in ["minimax", "alphabeta"]:
                ai = CaroAI(depth=depth, algorithm=algorithm, candidate_radius=1)
                result = ai.choose_move(board)

                rows.append({
                    "state": state_name,
                    "algorithm": algorithm,
                    "depth": depth,
                    "best_move": result.move,
                    "score": result.score,
                    "states": result.states,
                    "time_ms": round(result.elapsed_ms, 2),
                })

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["state", "algorithm", "depth", "best_move", "score", "states", "time_ms"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved benchmark result to {output_file}")


if __name__ == "__main__":
    run_benchmark()
