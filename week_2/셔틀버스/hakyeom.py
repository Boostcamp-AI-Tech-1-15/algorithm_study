from collections import deque


def solution(n, t, m, timetable):
    # n -> 셔틀 운행 횟수
    # t -> 셔틀 운행 간격
    # m -> 셔틀에 탈 수 있는 최대 인원
    # timetable - > 크루가 대기열에 도착하는 시간

    def str_time_to_sec(str_time):
        time = str_time.split(':')
        return int(time[0]) * 3600 + int(time[1]) * 60

    def sec_to_str_time(sec):
        h = str(sec//3600)
        m = str((sec % 3600) // 60)
        return f'{h.zfill(2)}:{m.zfill(2)}'

    timetable = list(map(str_time_to_sec, timetable))
    timetable.sort()
    # 대기열을 초단위로 바꾸고 정렬
    q = deque(timetable)
    # q에 넣어준다.

    arrival_time = str_time_to_sec('09:00')  # 버스의 도착시간
    time_interval = t * 60  # 버스의 도착 간격
    wait_start_time = q[0]  # 탑승객이 대기를 시작한 시간

    for i in range(n):  # 버스는 n회 도착한다
        is_full = False  # 각 버스가 도착했을때 탑승인원이 꽉 차는지 체크하는 변수
        for j in range(m):  # 버스는 m명을 태운다.
            if q:  # 대기인원이 있으면
                if q[0] <= arrival_time:  # 해당하는 사람이 버스 도착 시간전에 대기를 시작했으면
                    wait_start_time = q.popleft()  # 그 사람은 탑승한다.
                    if j == m - 1:  # 만약 q.popleft()를 m회 시도할수 있으면... 즉 전부 탑승했다면
                        is_full = True  # is_full을 True로 변경
        if i != n - 1:  # 마지막 버스가 아니면 다음 도착시간을 갱신
            arrival_time += time_interval

    if is_full:  # 마지막 버스가 만석이면 마지막 인원보다 1분 먼저 도착해야함
        answer = sec_to_str_time(wait_start_time - 60)
    else:  # 마지막 버스가 만석이 아니면 도착시간에 맞춰 오면 된다.
        answer = sec_to_str_time(arrival_time)
    return answer


solution(1,	1,	5,	["08:00", "08:01", "08:02", "08:03"])
solution(2,	10,	2,	["09:10", "09:09", "08:00"])
solution(2,	1,	2,	["09:00", "09:00", "09:00", "09:00"])
solution(1,	1,	5,	["00:01", "00:01", "00:01", "00:01", "00:01"])
solution(1,	1,	1,	["23:59"])
solution(10,	60,	45,	["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
         "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])
