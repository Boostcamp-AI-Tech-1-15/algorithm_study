def solution(balloons):

    answer = 0
    # 왼쪽, 오른쪽의 최솟값(터지지 않는 풍선)을 기록하는 리스트를 만듬
    left_min = balloons[0]
    left_min_arr = [left_min]

    for i in range(1, len(balloons)):
        left_min = min(left_min, balloons[i])
        left_min_arr.append(left_min)

    right_min = balloons[len(balloons) - 1]
    right_min_arr = [right_min]

    for i in range(len(balloons) - 2, -1, -1):
        right_min = min(right_min, balloons[i])
        right_min_arr.append(right_min)
    right_min_arr = right_min_arr[::-1]

    # 각각의 풍선이 터지지 않는 경우면 answer + 1
    for i in range(len(balloons)):
        mid = balloons[i]
        if i == 0 or i == len(balloons) - 1:
            answer += 1
        elif not ((mid > left_min_arr[i - 1]) and (mid > right_min_arr[i + 1])):
            answer += 1

    return answer


'''
타임아웃 코드

def solution(balloons):

    if len(balloons) < 3:
        return 2

    answer = 2
    
    for i in range(1, len(balloons) - 1):
        mid_ballon = balloons[i]

        left_ballons = balloons[:i]
        right_ballons = balloons[i + 1:]

        left_min = min(left_ballons)
        right_min = min(right_ballons)

        if not (mid_ballon > left_min and mid_ballon > right_min):
            answer += 1

    return answer

'''
