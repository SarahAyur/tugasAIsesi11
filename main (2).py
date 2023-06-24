import random

# Fungsi untuk menggambar papan permainan
def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" " + board[i][j] + " ", end="|")
        print("\n-------------")

# Fungsi untuk memeriksa apakah ada pemenang
def check_winner(board, player):
    # Memeriksa baris
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Memeriksa kolom
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Memeriksa diagonal
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Fungsi untuk mengatur giliran pemain manusia
def human_turn(board):
    while True:
        row = int(input("Masukkan nomor baris (0-2): "))
        col = int(input("Masukkan nomor kolom (0-2): "))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Input tidak valid. Coba lagi.")
        elif board[row][col] != " ":
            print("Sudah ada tanda di posisi tersebut. Coba lagi.")
        else:
            board[row][col] = "X"
            break

# Fungsi untuk mengatur giliran AI
def ai_turn(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == " ":
            board[row][col] = "O"
            break

# Fungsi utama untuk menjalankan permainan
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    draw_board(board)

    while True:
        human_turn(board)
        draw_board(board)

        if check_winner(board, "X"):
            print("Anda menang! Selamat!")
            break

        if " " not in board[0] and " " not in board[1] and " " not in board[2]:
            print("Permainan berakhir dengan hasil seri.")
            break

        print("Giliran AI...")
        ai_turn(board)
        draw_board(board)

        if check_winner(board, "O"):
            print("AI menang! Anda kalah.")
            break

        if " " not in board[0] and " " not in board[1] and " " not in board[2]:
            print("Permainan berakhir dengan hasil seri.")
            break

# Memulai permainan
play_game()
