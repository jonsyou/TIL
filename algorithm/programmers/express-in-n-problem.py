# 코딩테스트 연습 > 동적계획법(Dynamic Programming) > N으로 표현
# 2021-06-14

# 제출 답안 (2021-06-14)

def solution(N, number):
    from itertools import product
    
    m = [' ','+','-','/','*']
    for step in range(1,9):
        
        list_ = []
        for i in range(step) :
            list_.append([str(N)])
            if i != step-1:
                list_.append(m)

        for i in list(product(*list_)):
            temp = ''
            for j in i:
                temp += j
            temp = temp.replace(' ','')
            
            temp_num, temp_n = [] , ''
            
            for k in temp:
                if k == str(N):
                    temp_n += k
                else :
                    temp_num.append(temp_n)
                    temp_num.append(k)
                    temp_n = ''
                    
            temp_num.append(temp_n)
            
            temp_num1 = ['//' if i =='/' else i for i in temp_num]
            temp_num2 = temp_num1[::-1]

            while len(temp_num1) != 1:
                nn1 = str(eval(temp_num1[0] + temp_num1[1] + temp_num1[2]))
                nn2 = str(eval(temp_num2[0] + temp_num2[1] + temp_num2[2]))
                
                temp_num1 = [nn1] + temp_num1[3:]
                temp_num2 = [nn2] + temp_num2[3:]
                
            if temp_num1[0] == str(number) or temp_num2[0] == str(number):
                return step
                
            
    return -1
  
# 테스트 케이스 1,8 실패
