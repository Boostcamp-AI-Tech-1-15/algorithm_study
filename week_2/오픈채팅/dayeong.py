def solution(record):
    log = [r.split() for r in record]
    data = {}
    answer = []
    for l in log:
        if l[0] == "Enter":
            data[l[1]] = l[2]
        elif l[0] == "Change":
            data[l[1]] = l[2]

    for l in log:
        if l[0] == "Enter":
            answer.append(data[l[1]] + "님이 들어왔습니다.")
        elif l[0] == "Leave":
            answer.append(data[l[1]] + "님이 나갔습니다.")

    return answer
