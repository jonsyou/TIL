# 프로그래머스 > 동적계획법(Dynamic Programming) > 정수 삼각형
# 문제명 : 정수 삼각형

# 제출 답 ( 2021-06-13 ) 시간초과 이슈

def solution(triangle):
    from itertools import combinations
    
    f = len(triangle)
    
    def cal_sum(j):
        right, temp_ans = 0, 0
        for step, k in enumerate(triangle):
            if step-1 in j:
                right += 1
            temp_ans += k[right]
        return temp_ans
        
    aa = []
    for i in range(f):
        a = combinations(range(f),i)
        aa += list(a)
             
    return max(list(map(cal_sum,aa)))
  
# 시간이 너무 오래 걸림


### 제출 답 ( 2021-06-13 ) 정답!

def solution(triangle):
    ans = triangle[0]
    
    for i in triangle[1:]:
        temp_ans = []
        
        for index, j in enumerate(i):
            if index == 0 :
                temp_ans.append(ans[0] + j)
            elif index == len(i)-1:
                temp_ans.append(ans[-1] + j)
            else :
                if ans[index-1] >= ans[index]:
                    temp_ans.append(ans[index-1] + j)
                else :
                    temp_ans.append(ans[index] + j)
        ans = temp_ans
        
    return max(ans)

## 스스로 풀었다는 점에서 의미가 있음.
