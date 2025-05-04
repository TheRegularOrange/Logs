def is_safe(board, r, c, n):
    for i in range(r):
        if board[i][c] or (c - r + i >= 0 and board[i][c - r + i]) or (c + r - i < n and board[i][c + r - i]):
            return False
    return True

def solve(board, r, n):
    if r == n:
        return True
    for c in range(n):
        if is_safe(board, r, c, n):
            board[r][c] = 1
            if solve(board, r + 1, n):
                return True
            board[r][c] = 0
    return False

def main():
    n = int(input("Enter number of Queens: "))
    board = [[0]*n for _ in range(n)]
    if solve(board, 0, n):
        for row in board:
            print(" ".join(map(str, row)))

if __name__ == '__main__':
    main()
