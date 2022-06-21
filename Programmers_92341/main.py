import datetime, math
from datetime import datetime

def total_time(t): # t : "HH:MM" <type:string>
    tmp = str(t).split(':')
    return int(tmp[0]) * 60 + int(tmp[1])

def calculate_fee(t, fee): # t : total time <type:int>
    base_time, base_fee, unit_time, unit_fee = fee
    if t < base_time: return base_fee
    t = math.ceil((t - base_time) / unit_time)
    return base_fee + (t * unit_fee)

def solution(fees, record): # fee = 기본시간, 기본요금, 단위시간, 단위요금
    db = [] # [in_time, car_number, inout_flag, total_time]
    for rec in record:
        inout_time, car_num, flag = rec.split()
        if flag == 'IN':
            recorded = False
            for i in range(len(db)): # 기존 출입기록 check
                if db[i][1] == car_num:
                    recorded, db[i][0], db[i][2] = True, inout_time, 1
                    break
            if not recorded: # 출입기록 없으면 새롭게 db추가
                db.append([inout_time, car_num, 1, 0])
        else: # 출차기록
            for i in range(len(db)):
                if db[i][1] == car_num:
                    in_time = datetime.strptime(db[i][0], "%H:%M")
                    out_time = datetime.strptime(inout_time, "%H:%M")
                    db[i][3] += total_time(out_time - in_time)
                    db[i][2] = 0
                    break

    for i in range(len(db)): # 당일 출차하지 않은 차 check
        if db[i][2] == 1:
            in_time = datetime.strptime(db[i][0], "%H:%M")
            out_time = datetime.strptime("23:59", "%H:%M")
            db[i][3] += total_time(out_time - in_time)

    db.sort(key=lambda x: x[1]) # car_number 기준 sort
    res = []
    for data in db:
        res.append(calculate_fee(data[-1], fees))
    return res
