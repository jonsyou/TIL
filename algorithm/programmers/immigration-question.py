# 코딩테스트 연습 > 이분탐색 > 입국심사
# 2021-06-08

# 제출 답안 (2021-06-08)

def solution(n, times):
    
    min_ = sorted(times)[0]
    answer = n * min_
    
    while True:
        if sum([answer//i for i in times]) == n:
            break
        else : 
            answer -= min_ 
    
    return answer 
  
  ## 시간 초과 실패
