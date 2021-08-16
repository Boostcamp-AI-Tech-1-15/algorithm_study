import datetime

# 정원이 다 찼으면 마지막 사람 제끼기
# 안 찼으면 버스 시간에 맞춰서


def bus_table(n, t):
    bus = []
    bus.append("09:00")
    hour, minute = 9, 0
    for i in range(n - 1):
        minute += t
        if minute >= 60:
            hour += 1
            minute = 0
        tt = datetime.time(hour, minute)
        bus.append(tt.strftime("%H:%M"))
    return bus


def solution(n, t, m, timetable):
    timetable.sort()
    bus = bus_table(n, t)

    for i in range(n):
        # 대기인원 전체가 셔틀 정원보다 적을 경우 버스 시간표에 맞춰서 막차 태우기
        # 막차보다 첫 번째 대기자가 늦게 올 경우에도 막차 태우기
        if len(timetable) < m or timetable[0] > bus[-1]:
            return bus[-1]

        # 정원이 다 찼으면 마지막 사람 제끼기
        if i == n - 1:
            hour, minute = list(map(int, timetable[m - 1].split(':')))
            print(f'hour: {hour} minute: {minute}')
            minute -= 1
            if minute == -1:
                minute = 59
                hour -= 1
            tt = datetime.time(hour, minute)
            return tt.strftime("%H:%M")

        # 버스 태워 보낸 사람들 제거
        for j in range(m - 1, -1, -1):
            if timetable[j] <= bus[i]:
                print(f'last {timetable[j]}')
                del timetable[j]
