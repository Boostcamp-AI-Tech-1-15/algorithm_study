def solution(a):
    ans = 2
    l = len(a)
    if l<=3:
        return l
    left_min = [None]*l
    right_min = [None]*l
    left_min[1] = a[0]
    right_min[-2] = a[-1]
    for i in range(2, l-1): # i를 기준으로 왼쪽의 min과 오른쪽의 min을 계산
        left_min[i] = min(a[i-1], left_min[i-1])
        right_min[-i-1] = min(a[-i], right_min[-i])
    for i in range(1, l-1):
        if a[i]>left_min[i] and a[i]>right_min[i]:
            continue
        ans += 1
    return ans