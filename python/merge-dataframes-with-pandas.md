# Pandas를 활용한 데이터프레임 병합하기

<b>Pandas</b>의 ```merge```메서드를 활용하면 두 데이터 프레임의 공통 열 혹은 인덱스를 기준으로 두 개의 테이블을 합칠 수 있다.
이때 기준이 되는 열, 행의 데이터를 키(key)라고 한다.

```merge``` 명령으로 두 데이터프레임 을 합치면 공통 열을 기준으로 데이터를 찾아서 합쳐준다.
이때 기본적으로는 양쪽 데이터프레임에 모두 키가 존재하는 데이터만 보여주는 ```inner join``` 방식을 사용한다.

<b>예시 코드:</b>
```python
df1 = pd.DataFrame({'고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
                    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']},
                   columns=['고객번호', '이름'])
df2 = pd.DataFrame({'고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
                    '금액': [10000, 20000, 15000, 5000, 100000, 30000]},
                   columns=['고객번호', '금액'])
df3 = pd.merge(df1, df2)
print(df3)
```

```outer join``` 방식은 키값이 한쪽에만 있어도 데이터를 보여준다.
```python
pd.merge(df1, df2, how='outer')
```

```left``` 방식은 첫 번째, ```right``` 방식은 두 번째 데이터프레임의 키값을 모두 보여준다.
```python
pd.merge(df1, df2, how='left')
pd.merge(df1, df2, how='right')
```

테이블에 키값이 같은 데이터가 여러 개 있는 경우에는 가능한 모든 조합을 만들어 낸다.
```python
 df1 = pd.DataFrame({'품종': ['setosa', 'setosa', 'virginica', 'virginica'],
                     '꽃잎길이': [1.4, 1.3, 1.5, 1.3]}, columns=['품종', '꽃잎길이'])
 
 df2 = pd.DataFrame({'품종': ['setosa', 'virginica', 'virginica', 'versicolor'],
                     '꽃잎너비': [0.4, 0.3, 0.5, 0.3]}, columns=['품종', '꽃잎너비'])
 df3 = pd.merge(df1, df2)
 print(df3)
```

이름이 같아도 키가 되면 안 되는 열이 있다면 ```on``` 인수로 기준 열을 명시해야 한다.
기준 열이 아니면서 이름이 같은 열에는 ```_x``` 또는 ```_y``` 와 같은 접미사가 붙는다.
```python
df1 = pd.DataFrame({ '고객명': ['춖향', '춖향', '몽룡'],
                    '날짜': ['2018-01-01', '2018-01-02', '2018-01-01'],
                    '데이터': ['20000', '30000', '100000']})
df2 = pd.DataFrame({ '고객명': ['춖향', '몽룡'],
                    '데이터': ['여자', '남자']})
df3 = pd.merge(df1, df2, on='고객명')
print(df3)
```

일반 데이터 열이 아닌 인덱스를 기준 열로 사용하려면 ```left_index``` 또는 ```right_index``` 인수를 ```True```로 설정한다.
```python
df1 = pd.DataFrame({ '도시': ['서울', '서울', '서울', '부산', '부산'],
                    '연도': [2000, 2005, 2010, 2000, 2005],
                    '인구': [9853972, 9762546, 9631482, 3655437, 3512547]})
df2 = pd.DataFrame(np.arange(12).reshape((6, 2)),
                   index=[['부산', '부산', '서울', '서울', '서울', '서울'],
                          [2000, 2005, 2000, 2005, 2010, 2015]],
                   columns=['데이터1', '데이터2'])
df3 = pd.merge(df1, df2, left_on=['도시', '연도'], right_index=True)
print(df3)
```
또 다른 예시로는 
```python
df1 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                   columns=['서울', '부산'])
df2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'],
                   columns=['대구', '광주'])

df3 = pd.merge(df1, df2, how='outer', left_index=True, right_index=True)
print(df3)
```
