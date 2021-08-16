def solution(a):
    ret = [False for _ in range(len(a))]  # 최후까지 남을 수 있는지 저장 
    
    # i번쨰 풍선을 기준으로 왼쪽(1 ~ i-1) 와 오른쪽(i+1 ~ n) 둘다 풍선보다 
    # 작은 값이 있으면 최후의 풍선이 될 수 없음. 
    
    # 순방향
    m = a[0]                              # 처음 값으로 시작     
    for i in range(len(a)):               # 처음부터 하나씩 확인
        if a[i] <= m:                     # 기준값보다 작으면  
            ret[i] = True                 # 최후까지 남을 수 있음 
            m = a[i]                      # 기준값 재정의
            
    # 역방향
    m = a[-1]                             # 마지막 값으로 시작 
    for i in range(len(a)-1, -1, -1):     # 끝부터 하나씩 확인 
        if a[i] <= m:                     # 기준 값 보다 작으면 
            ret[i] = True                 # 최후까지 남을 수 있음
            m = a[i]                      # 기준값 재정의
    
    return sum(ret)