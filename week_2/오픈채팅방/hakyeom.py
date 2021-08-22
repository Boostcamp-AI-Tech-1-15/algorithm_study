from collections import defaultdict


def solution(record):

    uid_nick_dict = defaultdict(str)  # uid와 nick을 저장하는 dict
    messages = []

    for rec in record:
        rec_info = rec.split()
        state, uid = rec_info[0], rec_info[1]
        # state가 Leave가 아니면 닉네임이 포함된 record
        if state != 'Leave':
            # Enter, Change 모두 닉네임이 포함되어 있다.
            # dict을 업데이트
            nick = rec_info[2]
            uid_nick_dict[uid] = nick

        # 출력되는 메시지를 저장, Change는 메시지에 포함되지 않는다.
        if state != 'Change':
            messages.append([state, uid])

    def convert_message(message):
        behavior = '들어왔습니다.' if message[0] == 'Enter' else '나갔습니다.'
        return f'{uid_nick_dict[message[1]]}님이 {behavior}'

    answer = list(map(convert_message, messages))

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
