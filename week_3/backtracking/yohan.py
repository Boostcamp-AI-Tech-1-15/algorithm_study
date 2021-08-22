def solution(n):
    answer = 0

    # 체스판을 일차원 배열로 선언
    chess_board = [0 for _ in range(n)]

    def is_valid_position(row, column):
        for i in range(row):
            # 같은 행과 열, 대각선에 이미 퀸이 있는지 검사
            if chess_board[i] == column or \
                    chess_board[i] + i == row + column or \
                    i - chess_board[i] == row - column:
                return False
        return True

    def backtracking(row=0):
        # nonlocal 안하면 answer에 값 못더해줌
        nonlocal answer

        # 마지막 체스판까지 돌았을 때 반환
        if row == n:
            answer += 1
            return

        for column in range(n):
            # 퀸이 들어갈 수 있는 자리면 해당 포지션에 값을 올려줌.
            if is_valid_position(row, column):
                # 체스판[행] = 열
                chess_board[row] = column
                backtracking(row + 1)
            column += 1

    backtracking()
    return answer


print(solution(1))
