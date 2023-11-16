
def display_board(board):
    for row in board:
        print(row)
    print()


def return_valid_moves(x, y, board):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    valid_moves = []
    for move in moves:
        next_x, next_y = x + move[0], y + move[1]
        if is_valid_move(next_x, next_y, board):
            count = 0
            for m in moves:
                check_x, check_y = next_x + m[0], next_y + m[1]
                if is_valid_move(check_x, check_y, board):
                    count += 1
            valid_moves.append((next_x, next_y, count))
    return sorted(valid_moves, key=lambda x: x[2])


def is_valid_move(x, y, board):
    return 0 <= x < 8 and 0 <= y < 8 and board[y][x] == -1


def main():
    board = [[-1 for _ in range(8)] for _ in range(8)] # populate board with default values (-1)

    start_x, start_y = 0, 0
    board[start_y][start_x] = 0

    x, y, step = start_x, start_y, 1

    while step < 64:
        next_moves = return_valid_moves(x, y, board)
        if not next_moves:
            break

        next_x, next_y, _ = next_moves[0]
        board[next_y][next_x] = step
        x, y, step = next_x, next_y, step + 1

    if step == 64:
        board[start_y][start_x] = 0  # Mark the starting point again
        display_board(board)
        return True  # Tour was a success

    print("No solution found.")
    return False  # Could not complete the tour


if __name__ == '__main__':
    main()
