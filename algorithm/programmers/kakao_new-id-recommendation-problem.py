# 2021 KAKAO BLIND RECRUITMENT
# 문제명 : 신규 아이디 추천

# 제출 답 ( 2021-06-13 )

def solution(new_id):

    # step1
    new_id = new_id.lower()

    # step2    
    u1 = [chr(i) for i in range(ord('a'),ord('z')+1)]
    u2 = [str(i) for i in range(10)]
    u3 = ['-','_','.']

    u = u1+u2+u3

    new_id = [i for i in new_id if i in u]

    # step3
    temp, temp_ = '', ''
    for i in new_id :
        if i == '.' and temp_ == '.':
            continue
        else:
            temp += i
            temp_ = i
    new_id = temp

    # step4
    while True:
        if new_id == '':
            break
        elif new_id[0] == '.':
            new_id = new_id[1:]
        elif new_id[-1] == '.':
            new_id = new_id[:-1]
        else:
            break

    # step5
    if new_id == '':
        new_id = 'a'

    # step6
    if len(new_id) >= 16:
        new_id = new_id[:15]

    while True:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
        else:
            break

    # step7
    while len(new_id) <= 2:
        new_id += new_id[-1]

    answer = new_id
    return answer
  
# 정답이긴 하지만 코드가 길어서 비효율적이다.
# 정규식을 이용한 풀이를 목표로 공부하자.
