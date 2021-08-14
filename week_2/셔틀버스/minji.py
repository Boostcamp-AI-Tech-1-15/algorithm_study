from collections import deque

def change_to_min(timetable): # timetable의 시간을 분으로 바꾸는 함수
    timetable_min = [] # timetable을 분으로 바꿔서 저장할 배열
    
    for time in timetable:
        minute = int(time[0:2]) * 60 + int(time[3:]) # 전체 시간을 분으로 변경
        timetable_min.append(minute)
        
    timetable_min.sort() # 정렬
    timetable_min = deque(timetable_min) # 형변환
    return timetable_min


def min_to_time(min): # 분으로 된 것을 HH:MM string으로 바꿔주는 함수 
        hour = str(min//60) # 시간
        minute = str(min%60) # 분
        
        if len(hour) == 1: # 시간이 1자리라면
            hour = '0' + hour
            
        if len(minute) == 1: # 분이 1자리라면
            minute = '0' + minute
            
        time = f'{hour}:{minute}'
        return time
    
    
def solution(n, t, m, timetable):
    '''
    n: 셔틀 운행 횟수
    t: 셔틀 운행 간격 (분)
    m: 한 셔틀에 탈 수 있는 최대 크루 수
    timetable: 크루가 대기열에 도착하는 시각을 모은 배열
    '''
    timetable_min = change_to_min(timetable) # 분으로 변경, 정렬된 deque
    last_bus_time = 540 + (n-1) * t # 마지막 버스 시간
    
    ## 한 버스에 현재 크루가 모두 탈 수 있는 경우
    if m > len(timetable_min): 
        answer = min_to_time(last_bus_time) # 마지막 버스 타면 됨
        
    ## 마지막 버스를 타려고 기다리는 인원 계산
    else: 
        bus_time = 540 # 시작 버스 시간: 9시
        
        for _ in range(n-1): # 현재 버스 이전 사람들을 태워야 하므로 n-1
            for _ in range(m):
                if timetable_min[0] <= bus_time : # 이전 버스를 탔음
                    timetable_min.popleft()
                else :
                    break # 정렬되어 있으므로 이번 버스를 탈 수 있는 시간이 아님
            bus_time += t
        
        ## 마지막으로 타는 사람만 제치면 됨
        timetable_last_bus = [] # 마지막 버스를 탈 수 있는 사람
        
        for _ in range(m): 
            ## 버스 대기 인원 존재, 마지막 버스를 탈 수 있는 경우
            if timetable_min and timetable_min[0] <= bus_time: 
                timetable_last_bus.append(timetable_min.popleft())
            else:
                break

        wait_last_num = len(timetable_last_bus) # 마지막 버스를 타려고 기다리는 사람 명수
        
        if m > wait_last_num: # 제치지 않고도 마지막 버스를 탈 수 있음
            answer = min_to_time(last_bus_time)
            
        else: # m == wait_last_num, # 마지막 버스를 타기엔 탈 수 있는 마지막 사람을 제쳐야함
            answer = min_to_time(timetable_last_bus[-1]-1) # 마지막 사람보다 1분 빨라야함
        
    return answer
