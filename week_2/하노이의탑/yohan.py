def solution(n):
    answer = []

    def hanoi(n, source, helper, target):
        if n > 0:
            hanoi(n - 1, source, target, helper)
            answer.append([source, target])
            hanoi(n - 1, helper, source, target)

    hanoi(n, 1, 2, 3)

    return answer
