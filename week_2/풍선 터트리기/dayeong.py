def solution(a):
    n = len(a)
    data = set()
    INF = int(1e9)
    left_min, right_min = INF, INF

    for i in range(n):
        if a[i] < left_min:
            left_min = a[i]
            data |= {a[i]}

        if a[-i-1] < right_min:
            right_min = a[-i-1]
            data |= {a[-i-1]}
    # print(data)
    return len(data)
