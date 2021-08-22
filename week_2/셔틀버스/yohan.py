from collections import deque


def solution(n, t, m, timetable):
    answer = ''

    # 정렬한 뒤 타임테이블의 시간을 분으로 통일
    timetable.sort()
    timetable_to_minutes = deque()
    for time in timetable:
        hour, minute = time.split(':')
        # 분으로 변환한 시간들을 deque에 삽입
        timetable_to_minutes.append(int(hour) * 60 + int(minute))

    last_time = 60 * 9 + t * (n - 1)

    for i in range(n):
        departure_time = 60 * 9 + t * i
        # 모든 승객이 탈 수 있으면 바로 마지막 출발시간 반환
        if len(timetable_to_minutes) < m:
            return "%02d:%02d" % (last_time // 60, last_time % 60)

        # 마지막 배차일 때 가장 앞순번 승객이 시간 내에 탈 수 있고 타야하는 승객들이 있을 경우
        # 가장 마지막에 탈 수 있는 승객보다 1분 빠른 시간을 반환
        if i == n - 1:
            if timetable_to_minutes[0] <= last_time and len(timetable_to_minutes) >= m:
                last_time = timetable_to_minutes[m - 1] - 1
            return "%02d:%02d" % (last_time // 60, last_time % 60)

        # 수용할 수 있는 승객의 수만큼 반복을 돌면서 대기중인 승객들을 승차시킴. (deque에서 pop)
        for i in range(m):
            if timetable_to_minutes[0] <= departure_time:
                timetable_to_minutes.popleft()
            else:
                break

    return "%02d:%02d" % (last_time // 60, last_time % 60)
