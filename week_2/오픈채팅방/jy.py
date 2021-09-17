def solution(records):
    ans = []
    id_nname = dict()
    ret_msgs = []
    for record in records:
        msg_splt = record.split()
        msg_type = msg_splt[0]
        _id = msg_splt[1]
        if msg_type!='Leave':
            nname = msg_splt[2]
            id_nname[_id] = nname
        if msg_type=='Enter' or msg_type=='Leave':
            ret_msgs.append((msg_type, _id))
    for ret_msg in ret_msgs:
        msg_type, _id = ret_msg
        t_msg = id_nname[_id]+'님이'
        t_msg += ' 들어왔습니다.' if msg_type=='Enter' else ' 나갔습니다.'
        ans.append(t_msg)
    return ans