def solution(n, t, m, timetable):
    timetable_min = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timetable]) # 분 단위로 변환
    buses = [[540+i*t, []] for i in range(n)] # 버스 타임테이블 
    
    i = 0                                 # bus index 
    for crew in timetable_min:
        while (crew > buses[i][0] or      # 크루가 정류장에 버스 출발시간보다 늦게 도착하거나
               len(buses[i][1]) == m):    # 버스가 만원이면 (while : 크루가 바로 다음버스보다 늦게 도착할 수도 있어서)

            i += 1                        # 다음 버스로 넘어감
            if i == n:                    # 마지막 버스까지 다 넘어가면 멈춤
                break
        else:                             # break를 만나지 않으면 
            buses[i][1].append(crew)      # 크루를 버스에 태운다. 
            continue                      # 아래의 break를 만나지 않게하려고 continue
        
        break                             # while의 break를 만났을때 for문도 break  
    
    ret = buses[-1][0] if len(buses[-1][1]) < m else buses[-1][1][-1] - 1
    # 막차가 만원이 아니면 막차 시간에 나오고 그렇지 않으면 마지막 사람보다 1분 일찍 나온다. 

    return '%02d:%02d' %(ret // 60, ret%60)  