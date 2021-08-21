# https://leetcode.com/problems/n-queens/
# https://ko.wikipedia.org/wiki/%EC%9C%A0%EC%A0%84_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
import random


class Solution:

    def make_queens(self, board_size, genetic_pool):
        '''
        genetic_pool 만큼의 해를 생성
        '''
        boards = []
        for i in range(genetic_pool):
            board = []
            for j in range(board_size):
                line = ['']*board_size
                line[random.randint(0, board_size-1)] = 'Q'
                board.append('.'.join(line))
            boards.append(board)
        return boards

    def get_score(self, board):
        '''
        해당 해의 점수 산정
        '''
        score = 0
        q_pos = list(map(lambda x: x.find('Q'), board))
        for y, x in enumerate(q_pos):
            for ny in range(y+1, len(q_pos)):
                nx = q_pos[ny]
                if self.check(x, nx, y, ny):
                    score += 1
        return score

    def check(self, x, nx, y, ny):
        '''
        q1과 q2가 서로 공격할 수 없으면 True
        '''
        if x == nx or y == ny:
            return False
        if abs(x - nx) == abs(y - ny):
            return False
        return True

    def mate(self, b1, b2):  # 교배
        child = []
        for i in range(len(b1)):
            if b1[i] == b2[i]:  # 두 부모의 성질이 같으면
                child.append(b1[i])
            else:
                if random.random() < 0.5:
                    child.append(b1[i])
                else:
                    child.append(b2[i])
        return child

    def transfer(self, b, transfer_rate):
        if random.random() < transfer_rate:  # 10%의 확률로
            y = random.randint(0, len(b) - 1)
            line = ['']*len(b)
            line[random.randint(0, len(b)-1)] = 'Q'
            line = '.'.join(line)
            b[y] = line
        return b

    def solveNQueens_by_gentic(self, board_size, genetic_pool, generation_number, transfer_rate: int):
        loop_count = 0

        gen = self.make_queens(board_size, genetic_pool)  # 생성

        while loop_count < generation_number:

            gen.sort(key=self.get_score, reverse=True)  # 선택
            #print(sum(list(map(self.get_score, gen))))
            limit_mating, limit_target = len(gen)//2, len(gen)//2

            children = []
            # 교배, 상위 50%만, 자식들은 tranfer rate의 비율로 변이됨
            for i in range(limit_mating):
                if loop_count < generation_number - 1:
                    child = self.transfer(
                        self.mate(gen[i], gen[i+1]), transfer_rate)
                else:
                    child = self.mate(gen[i], gen[i+1])
                children.append(child)

            # 대치 -> 열등한 해를 버림
            while limit_target != 0:
                limit_target -= 1
                gen.pop()

            gen.extend(children)
            loop_count += 1

        gen.sort(key=self.get_score, reverse=True)

        return gen


genetic_pool = 1000
solution = Solution()
boards = solution.solveNQueens_by_gentic(generation_number=1000,
                                         board_size=10, genetic_pool=genetic_pool, transfer_rate=0.1)


f = 0
s = 0
for b in boards:
    q_pos = list(map(lambda x: x.find('Q'), b))
    for y, x in enumerate(q_pos):
        is_fail = False
        for ny in range(y + 1, len(b)):
            nx = q_pos[ny]
            if not solution.check(x, nx, y, ny):
                is_fail = True
                break
        if is_fail:
            f += 1
            break
    else:
        s += 1

print('total_answer: ', genetic_pool, 'correct: ', s, 'wrong: ', f)
