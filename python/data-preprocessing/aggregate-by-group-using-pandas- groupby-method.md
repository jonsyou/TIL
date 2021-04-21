# Pandas 의 groupby 메서드를 활용한 그룹별 집계하기

<b>Python</b> ```pandas``` 모듈의 ```groupby()``` 메서드를 활용하여 그룹 객체를 만들 수 있다. 
만들어진 그룹 객체에 집계함수를 적용하게 되면 나누어진 각 그룹에 각각 집계가 적용된다. 
이어서 그룹별 집계 결과를 합치는 단계를 거치게 되고 우리는 손쉽게 그룹별로 집계된 결과를 한번에 얻을 수 있다.

사용 예시 코드 :
```python
## customer # 데이터 프레임

# cust_country 변수로 그룹화
cust_group = customer.groupby('cust_country') 

# 그룹 연산 결과 저장할 데이터 프레임 생성
cust_agg = pd.DataFrame()

# 위 코드에서 cust_country 변수로 그룹화 하였고
# 그룹 마다의 grade 변수의 계산 값 도출 가능
cust_agg['sum_grade'] = cust_group['grade'].sum() # 합계
cust_agg['max_grade'] = cust_group['grade'].max() # 최대값

# 인덱스 초기화 
cust_agg = cust_agg.reset_index()
```

손쉽게 그룹별로 집계결과를 얻어 볼 수 있으며, 코드를 많이 단축시킬 수 있는 장점이 있다.
