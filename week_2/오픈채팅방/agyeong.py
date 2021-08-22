def solution(record):
    answer = []
    
    # 마지막에 들어온 아이디가 진짜 아이디이기 때문에
    # 유저 아이디와 아이디 저장하는 딕셔너리 생성
    user = {}
    for r in record:
        rs = r.split(" ")
        if len(rs) == 3: 
            user[rs[1]] = rs[2]
    
    # 채팅방 로그 확인하면서 그에 맞는 결과 생성
    for r in record:
        rs = r.split(" ")
        if rs[0] == "Enter":
            answer.append(user[rs[1]] + "님이 들어왔습니다.")
        elif rs[0] == "Leave":
            answer.append(user[rs[1]] + "님이 나갔습니다.")
        else: 
            pass
        
    return answer