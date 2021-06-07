# 2019 KAKAO BLIND RECRUITMENT
# 문제명 : 오픈채팅방

# 제출 답 ( 2021-06-07 )

def solution(record):
    
    ans = []
    nick = {}
    
    for i in record:
        sp = i.split()
        if sp[0] == 'Enter':
            ans.append(f'{sp[1]}님이 들어왔습니다.')
            nick[sp[1]] = sp[2]
        elif sp[0] == 'Leave':
            ans.append(f'{sp[1]}님이 나갔습니다.')
        else :
            nick[sp[1]] = sp[2]
    
    answer = []
    for i in ans:
        answer.append(i.replace(i[:i.find('님')],nick[i[:i.find('님')]]))

    
    return answer

## enter, change 했을 때의 닉네임만 필요하다. 

# 들어온 기록은 모두 저장하고 닉네임은 제일 최종의 닉네임으로 표기.
