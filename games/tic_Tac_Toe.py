def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def is_draw(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

def play_game():
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a cell (1-9): ")

        if move not in [str(i) for i in range(1, 10)]:
            print("❌ Invalid input. Try again.")
            continue

        # Find cell
        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    board[i][j] = current_player
                    if check_winner(board, current_player):
                        print_board(board)
                        print(f"🎉 Player {current_player} wins!")
                        return
                    elif is_draw(board):
                        print_board(board)
                        print("🤝 It's a draw!")
                        return
                    current_player = "O" if current_player == "X" else "X"
                    break
            else:
                continue
            break
        else:
            print("⚠️ Cell already taken. Try again.")

if __name__ == "__main__":
    play_game()