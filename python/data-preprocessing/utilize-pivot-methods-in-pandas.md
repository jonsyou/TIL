# Pandas의 pivot 메소드 활용

데이터 테이블을 재배치하기 위하여 <b>Pandas</b> 의 ```pivot``` 메소드를 활용할 수 있다. 
행으로 사용할 컬럼을 ```index``` 매개변수에 입력하고 열로 사용할 컬럼은 ```columns```, 그리고 각 셀에 저장할 값에 해당하는 컬럼을 ```values``` 에 입력한다. 

```python
df_.pivot(index=None, columns=None, values=None)
```

더 나아가 ```pivot_table``` 메서드를 활용하면 본인이 지정해준 설정에 의해 테이블의 요약된 정보를 출력해준다.

```python
df_.pivot_table(values=None, index=None, columns=None, aggfunc='mean',
                fill_value=None, margins=False, dropna=True, margins_name='All')
```

- ```index``` : ```index``` 색인으로 사용될 컬럼
- ```columns``` : ```column``` 색인으로 사용될 컬럼
- ```aggfunc``` : 데이터 축약 시 사용할 함수 (```mean```, ```sum```, ```count``` ...) *default는 ```mean```
- ```margins``` : 행/열별 총 합
