# Pandas 의 groupby 메서드를 활용한 그룹별 집계하기

<b>Python</b> ```pandas``` 모듈의 ```groupby()``` 메서드를 활용하여 그룹 객체를 만들 수 있다. 
만들어진 그룹 객체에 집계 함수를 특정 변수에 대해 적용해 주면 나누어진 각 그룹에 각각 집계 결과가 도출된다. 
이어서 그룹별 집계 결과가 합쳐지는 단계를 거치게 되고 우리는 손쉽게 그룹별로 특정 변수의 집계 결과를 얻을 수 있다.

<b>사용 예시 코드 :</b>
```python
# 사용 데이터 프레임
df

# col_1 변수로 그룹화
df_group = df.groupby('col_1') 

# 그룹 연산 결과 저장할 데이터 프레임 생성
df_agg = pd.DataFrame()

# 위 코드에서 col_1 변수로 그룹화 하였고
# 그룹 마다의 col_2 변수의 계산 값 도출 가능
df_agg['sum_col_2'] = df_group['col_2'].sum() # 합계
df_agg['max_col_2'] = df_group['col_2'].max() # 최대값

# 인덱스 초기화 
df_agg = df_agg.reset_index()
```

손쉽게 그룹별로 집계 결과를 얻어 볼 수 있으며, 코드를 많이 단축시킬 수 있는 장점이 있다.

---
- <b>Pandas 에 내장된 기본 집계 함수</b>
  - ```mean()```, ```max()```, ```min()```, ```sum()```, ```count()```, ```size()```, ```var()```, ```std()```, ```describe()```, ```info()```, ```first()```, ```last()``` 등
