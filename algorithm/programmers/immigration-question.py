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

# 제출 답안 (2021-06-09)
# 이분탐색 적용

def solution(n, times):    
    
    left = 1
    right = min(times) * n 
    mid = (left + right)/2
    
    def cal_n(t):
        return sum([t//i for i in times])
    
    while True:
        if cal_n(mid) >= n :
            right = mid - 1
            if cal_n(right) == n-1:
                return int(right) + 1
                
            mid = (left + right)//2
            
        if cal_n(mid) < n :
            left = mid + 1
            if cal_n(left) >= n:
                return int(left)
            
            mid = (left + right)//2
            
        if right ==left:
            return right

        ## 정답 처리 됨
