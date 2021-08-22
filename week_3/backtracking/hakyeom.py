# https://leetcode.com/problems/n-queens/

class Solution:
    def check(self, x, nx, y, ny):
        '''
        q1과 q2가 서로 공격할 수 없으면 True
        '''
        if x == nx or y == ny:
            return False
        if abs(x - nx) == abs(y - ny):
            return False
        return True

    def solveNQueens(self, n: int):

        output = []  # 결과

        def dfs(board, num_of_queens):
            q_pos = list(map(lambda x: x.find('Q'), board))  # 퀸을 좌표로 변환

            # 라인별로 n열의 퀸과 n+1의 퀸들과 비교
            for y, x in enumerate(q_pos):
                for ny in range(y + 1, num_of_queens):
                    nx = q_pos[ny]

                    if not self.check(x, nx, y, ny):
                        # 실패하면 return, dfs 종료
                        return

            # 전부 통과했는데 꽉차 있으면 output에 결과 append
            if num_of_queens == n:
                output.append(board)
                return
            else:
                # 아직 통과 못했으면 다음열의 퀸을 착수
                for i in range(n):
                    next_line = [''] * n
                    next_line[i] = 'Q'
                    next_line = '.'.join(next_line)
                    board[num_of_queens] = next_line
                    # print(board)
                    dfs(board[:], num_of_queens + 1)

        # 빈 보드를 초기화
        board = ['.'*n for _ in range(n)]
        # dfs 시작
        dfs(board[:], 0)

        return output


Solution().solveNQueens(4)
