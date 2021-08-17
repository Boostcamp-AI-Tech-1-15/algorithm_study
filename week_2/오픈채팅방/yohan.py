def solution(record):
    user_table = {}
    answer = []

    for r in record:
        r = r.split()
        # r = [action, uid, nickname] # Enter or Change
        # r = [action, uid] # Leave
        if r[0] == 'Enter' or r[0] == 'Change':
            # 해시테이블 초기화 {uid: nickname}
            user_table[r[1]] = r[2]

    for r in record:
        r = r.split()
        # 변경된 닉네임으로 메시지 생성
        if r[0] == 'Enter':
            answer.append(user_table[r[1]] + '님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(user_table[r[1]] + '님이 나갔습니다.')

    return answer
