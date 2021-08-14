def solution(record):
    user = {} # key: user id, value: 닉네임 으로 구성된 딕셔너리
    log = [] # [id, state] 형태로 저장 # Enter:0, Leave:1, Change는 기록을 출력 할 필요 없음
    
    ## 기록 저장
    for r in record:
        if r[0] == 'E': # Enter    
            state, user_id, user_name = r.split()
            log.append([user_id,0]) # log에 Enter 추가
            user[user_id] = user_name # user 딕셔너리에 이름 저장
            
        elif r[0] == 'L': # Leave
            state, user_id = r.split()
            log.append([user_id,1]) # log에 Leave 추가
            
        elif r[0] == 'C': # Change
            state, user_id, user_name = r.split()
            user[user_id] = user_name # user 딕셔너리에 저장된 이름 변경
    
    ## 정답 answer list에 저장
    answer = []
    for record_id, record_state in log:
        name = user[record_id]
        if record_state == 0: # Enter
            answer.append(name+"님이 들어왔습니다.")
        elif record_state == 1: # Leave
            answer.append(name+'님이 나갔습니다.')
    return answer
