from board import Board, HUMAN, AI
from ai import CaroAI


def choose_algorithm():
    print("Chọn chế độ AI:")
    print("1. Minimax")
    print("2. Alpha-Beta")
    choice = input("Nhập lựa chọn: ").strip()
    return "minimax" if choice == "1" else "alphabeta"


def choose_depth():
    try:
        depth = int(input("Nhập độ sâu tìm kiếm, ví dụ 1, 2, 3: "))
        return max(1, depth)
    except ValueError:
        return 2


def main():
    board = Board(size=9)
    algorithm = choose_algorithm()
    depth = choose_depth()
    ai_player = CaroAI(depth=depth, algorithm=algorithm, candidate_radius=1)

    print("\nKý hiệu: Người chơi = X, Máy = O")
    print("Nhập nước đi theo dạng: row col, ví dụ: 4 4\n")

    while True:
        board.display()

        try:
            row, col = map(int, input("Bạn đi: ").split())
        except ValueError:
            print("Vui lòng nhập đúng dạng: row col")
            continue

        if not board.make_move(row, col, HUMAN):
            print("Ô không hợp lệ hoặc đã có quân. Hãy chọn ô khác.")
            continue

        winner = board.check_winner()
        if winner:
            board.display()
            print_result(winner)
            break

        result = ai_player.choose_move(board)
        if result.move is None:
            print("Không còn nước đi hợp lệ.")
            break

        ai_row, ai_col = result.move
        board.make_move(ai_row, ai_col, AI)

        print("\nMáy chọn:", result.move)
        print("Thuật toán:", algorithm)
        print("Giá trị đánh giá:", result.score)
        print("Độ sâu:", depth)
        print("Số trạng thái đã xét:", result.states)
        print(f"Thời gian chạy: {result.elapsed_ms:.2f} ms\n")

        winner = board.check_winner()
        if winner:
            board.display()
            print_result(winner)
            break


def print_result(winner):
    if winner == HUMAN:
        print("Bạn thắng!")
    elif winner == AI:
        print("Máy thắng!")
    else:
        print("Hòa!")


if __name__ == "__main__":
    main()
