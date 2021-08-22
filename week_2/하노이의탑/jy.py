def solution(n):
    answer = []
    def hanoi(a, b, c, n):
        if n==1:
            answer.append([a, c])
            return
        hanoi(a, c, b, n-1)
        hanoi(a, b, c, 1)
        hanoi(b, a, c, n-1)
        
    hanoi(1, 2, 3, n)
    return answer