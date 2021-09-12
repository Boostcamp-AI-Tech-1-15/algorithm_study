def return_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def check_distance(place, plist):
    plen = len(plist)
    for p1 in range(0, plen):  # p index 1
        for p2 in range(p1 + 1, plen):  # p index 2
            pdis = return_distance(plist[p1], plist[p2])

            if pdis > 2:  # 거리두기 지켜짐
                continue
            elif pdis == 2:  # 확인해봐야함
                # 일자로 이어진 경우
                # 가로
                if plist[p1][0] == plist[p2][0]:
                    if place[plist[p1][0]][(plist[p1][1] + plist[p2][1]) // 2] == 'X':  # 둘 사이가 파티션이면
                        continue
                    else:  # 파티션 아님
                        return 0

                # 세로
                elif plist[p1][1] == plist[p2][1]:
                    if place[(plist[p1][0] + plist[p2][0]) // 2][plist[p1][1]] == 'X':  # 둘 사이가 파티션이면
                        continue
                    else:  # 파티션 아님
                        return 0

                # 대각선인 경우
                else:
                    if place[plist[p1][0]][plist[p2][1]] == 'X' and place[plist[p2][0]][plist[p1][1]] == 'X':
                        continue
                    else:
                        return 0

            else:  # pdis==1
                # 다 pass하고 answer에 0 추가
                return 0
    return 1


def solution(places):
    """
    상하좌우 1칸 -->바로X
    상하좌우 2칸 -->사이에 X(파티션)있으면 괜찮음
    대각선 1칸-->양쪽으로 X(파티션) 있어야함
    """
    answer = []

    for place in places:
        # p 위치 저장
        plist = []
        for i in range(5):  # 가로
            for j in range(5):  # 세로
                if place[i][j] == 'P':
                    plist.append([i, j])

        result = check_distance(place, plist)
        answer.append(result)

    return answer
