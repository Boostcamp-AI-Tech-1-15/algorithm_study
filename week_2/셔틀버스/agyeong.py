def solution(n, t, m, timetable):
    
    timetable_min = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timetable]) # 분 단위로 변환
    
    crew_num = len(timetable)  # 총 크루 수 			
    bus_crew = n * m # 버스에 탈 수 있는 크루 수  		
    
    last_crew = timetable_min[-1] # 마지막에 타는 크루 
    
    # 지금 타는 차가 마지막 차라면 
    if bus_crew - crew_num == 1: # 마지막으로 버스 탈 때 
        if last_crew < 540: # 모두 9시 전에 나오면
            time = 540
        else: # 9시 이후에 나오는 크루가 있으면
            time = last_crew - 1        
        
    elif bus_crew == crew_num: # 마지막 크루보다 일찍 나와야할 때
        if last_crew == 1439:
            time = 540
        else:
	        time = last_crew - 1
    
    # 마지막 차가 아니라면 막차 타는 시간에 나오면 됨.
    else:
        time = 540 - 60 + n * t
    
    return '%02d:%02d' % (time//60, time%60)