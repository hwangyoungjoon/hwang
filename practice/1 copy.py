import datetime
from collections import deque

# def timetotime(time):

def logtime(logs):
    renewtimes = []
    for log in logs:
        times = log.split("-")
        start_time = times[0].split(":")
        end_time = times[1].split(":")
        h_s = int(start_time[0]) ; h_e = int(end_time[0])
        m_s = int(start_time[1]) ; m_e = int(end_time[1])
        s_s = int(start_time[2]) ; e_s = int(end_time[2])
        
        renew_start_time = datetime.timedelta(hours=h_s,minutes=m_s, seconds=s_s)
        renew_end_time = datetime.timedelta(hours=h_e,minutes=m_e, seconds =e_s)
        print(renew_end_time-renew_start_time)

        renewtimes.append([renew_start_time,renew_end_time])
    return renewtimes


def solution(play_time, adv_time, logs):
    
    re_logs = logtime(logs)
    re_logs.sort()
    
    start_time = deque([])
    end_time = dequeue([])

    for start,end in re_logs:
        start_time.append(start)
        end_time.append(end)

    cnt = 0
    answer = []
    while start_time:
        st = start_time.popleft()
        if st < end_time[0]:
            count += 1
        else:
            answer.append(1)

    return time.strftime('%H:%M:%S',time.gmtime(answer))

    # lst.append([0,dur])
    # lst.sort()
    
    # slst = deque([])
    # elst = deque([])
    # for s,e in lst:
    #     slst.append(s)
    #     elst.append(e)

    # count = 0
    # ans = []
    # while slst:
    #     start = slst.popleft()
    #     if start < elst[0]:
    #         count += 1
    #     else:
    #         ans.append()
    # return time.strftime('%H:%M:%S',time.gmtime(ans))
    return re_logs
print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))