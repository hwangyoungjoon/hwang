def solution(record):
    answer = []
    action_list = {'Leave': '님이 나갔습니다.', 'Enter':'님이 들어왔습니다.'}
    name_dic = {}
    case_list = []
    for i in record:
        records = i.split(' ')
        action = records[0]

        if action != 'Leave':
            name_dic[records[1]] = records[2]
        if action != 'Change':
            case_list.append((action,records[1]))
    for action, id in case_list:
        answer.append(name_dic[id]+action_list(action))
    # for idx,data in enumerate(records):
    #     print(data)
    #     cmd = data[0]

    #     if cmd == "Enter":
    #         id_key = data[1]
    #         nick = data[2]
    #         if id_key not in chat_log :
    #             message.append("{}님이 들어왔습니다.".format(nick))
    #             chat_log.append(id_key)

    #             # message.append("{}님이 들어왔습니다.".format(nick))
    #             print(message)
    #             print(chat_log.index(id_key))
    #         else:
    #             print(chat_log.index())
    #             # for i in chat_log.index():
    #             message.append("{}님이 들어왔습니다.".format(nick))
    #             print(message)
                
    #             print(message)
    #     elif cmd == "Leave":
                
    #             message.append("{}님이 나갔습니다.".format(nick))
    #             print(message)
    #     elif cmd =="Change":
    #         print(message)
        
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])