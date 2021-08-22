def solution(a):
    ## 최솟값 저장할 2차원 배열 선언
    len_a = len(a)  # 배열 길이 저장
    min_list = [[-float('inf') for _ in range(len_a)] for _ in range(2)]  # 2*len_a size 2차원 배열 생성

    ## 최솟값 저장 (좌->우)
    min_list[0][0] = a[0]  # 초기값

    for i in range(1, len_a):
        min_list[0][i] = min(min_list[0][i - 1], a[i])  # 왼쪽부터 순차적으로 최소인 값 저장

    ## 최솟값 저장 (좌<-우)
    min_list[1][-1] = a[-1]  # 초기값

    for j in range(len_a - 2, -1, -1):
        min_list[1][j] = min(min_list[1][j + 1], a[j])  # 오른쪽부터 순차적으로 최소인 값 저장

    ## 최후에 남을 수 있는 풍선 개수 count
    answer = len_a

    for k in range(1, len_a - 1):
        if max(min_list[0][k - 1], min_list[1][k + 1], a[k]) == a[k]:  # i의 좌측 최솟값, 우측 최솟값, i 비교
            answer -= 1  # i가 최대일 경우 최후에 남을 수 없음

    return answer
