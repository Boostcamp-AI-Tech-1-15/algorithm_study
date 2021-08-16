import math


def solution(a):
    # 투포인터 배열 초기화
    left_min, right_min = [math.inf] * (len(a) + 1), [math.inf] * (len(a) + 1)
    length = len(a)
    answer, last_index = length, length - 1

    for i in range(len(a)):
        # 투포인터를 이동시키며 최소값 갱신
        left_min[i] = min(a[i], left_min[i - 1])
        right_min[last_index -
                  i] = min(a[last_index - i], right_min[last_index - i + 1])

    for i in range(len(a)):
        # 해당 인덱스의 값이 좌우 인덱스의 값보다 크다면 최후에 남을 수 없으므로 answer에서 하나씩 빼기
        if a[i] > left_min[i] and a[i] > right_min[i]:
            answer -= 1

    return answer
