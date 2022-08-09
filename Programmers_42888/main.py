def printf(log, users):
    result = []
    for status, uid in log:
        if status == "Enter":
            result.append(users[uid] + "님이 들어왔습니다.")
        elif status == "Leave":
            result.append(users[uid] + "님이 나갔습니다.")
    return result


def solution(record):
    log = []
    users = {}
    for rec in record:
        rec = rec.split()
        status, uid = rec[0], rec[1]
        log.append([status, uid])

        if status == "Enter" or status == "Change":
            users[uid] = rec[2]
    return printf(log, users)