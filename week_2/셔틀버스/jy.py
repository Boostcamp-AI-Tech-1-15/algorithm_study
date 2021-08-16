def solution(n, t, m, timetable):
    c_num = len(timetable)
    ans = -1
    buses = dict()
    for i in range(n): # 버스 시간표를 만듦, 모든 시간은 시간이 아닌 정수로 변경
        buses[9*60+i*t] = 0
    last_bus_time = list(buses.keys())[-1]
    def change_time(t):
        hh, mm = map(int, t.split(':'))
        return hh*60+mm
    new_timetable = sorted(list(map(change_time, timetable)))
    c_idx = 0
    c_time = new_timetable[c_idx]
    last_crew = 0
    for bus_time in buses.keys(): # 버스에 태움
        while c_time<=bus_time and buses[bus_time]<m:
            buses[bus_time] += 1
            last_crew = c_time # 마지막에 탄 사람
            c_idx += 1
            if c_idx==c_num:
                break
            c_time = new_timetable[c_idx]
        if c_idx==c_num:
            break
    if buses[last_bus_time]<m:
        ans = last_bus_time
    else:
        ans = last_crew-1
    ans = f'{ans//60:0>2}:{ans%60:0>2}'
    return ans