def solution(n):
    answer = 0
    chess_board = [0 for _ in range(n)]

    def is_valid(row, column):
        for i in range(row):
            if chess_board[i] == column or \
                    chess_board[i] + i == row + column or \
                    i - chess_board[i] == row - column:
                return False
        return True

    def backtracking(row=0):
        nonlocal answer

        if row == n:
            answer += 1
            return

        for column in range(n):
            if is_valid(row, column):
                chess_board[row] = column
                backtracking(row + 1)
            column += 1

    backtracking()
    return answer


print(solution(1))
