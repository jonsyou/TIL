# Seaborn 을 이용한 상자 그림(Boxplot) 그리기

특정 범주와 관련된 분포를 표시하기 위해서 우리는 ```seaborn``` 모듈의 ```boxplot()``` 메서드를 활용하여 상자 그림(```boxplot```)을 그릴 수 있다. 
상자 그림(```boxplot```)은 범주형 변수의 여러 수준 또는 변수 간의 비교를 용이하게 하는 방식으로 우리에게 <b>정량적 데이터의 분포</b>를 보여준다. 
물론 특정 범주가 아니더라도 어떤 정량적 자료의 분포 형태를 알기 위해서도 사용 가능하다.

상자 그림(```boxplot```)의 자료로부터 얻어낸 통계량인 <b>5가지 요약 수치</b>를 가지고 그린다. 
여기서 5가지 요약 수치란 최솟값, 제 1사분위(Q1), 제 2사분위(Q2), 제 3사분위(Q3), 최댓값을 말한다.
이렇게 5가지 요약 수치를 활용해 그린 그림이기 때문에 우리는 비교적 쉽게 분포를 파악할 수 있게 된다. 

우선 기본적인 ```boxplot``` 그리기 코드는 아래와 같다.
```python
import seaborn as sns

sns.boxplot(x = "col_1", data = data_)
```
해당 상자 그림을 만약 세로 방향으로 그리고 싶다면 ```orient = "v"``` 옵션을 추가해 주면 된다.

좀 더 나아가 각 집단별로 특정 함수에 대한 ```boxplot```을 그리는 코드는 아래와 같다.
```python
# 일변량 질적 자료의 경우
sns.boxplot(x = "col_1", y = "col_2", data = data_)

# 이변량 질적 자료의 경우
sns.boxplot(x = "col_1", y = "col_2", hue = "col_3", data = data_)
```
만약 상자의 색을 변경하고 싶다면 ```palette``` 옵션 값을 수정해 주면 된다. 예를 들어 ```palette = "Set3"```와 같은 옵션을 추가해 줄 수 있다.

```boxplot``` 과 ```swarmplot``` 을 한 번에 그리면 좀 더 정보량이 많은 시각화가 될 수 있다.
```python
sns.boxplot(x="col_1", y="col_2", data=data_)
sns.swarmplot(x="col_1", y="col_2", data=data_, color=".25")
```

마지막으로 ```factorplot``` 메서드를 활용하면 여러 면으로 분할하여 ```boxplot``` 을 그리는 것이 가능하다.
```python
sns.factorplot(x="col_1", y="col_2", hue="col_3", col="col_4", data=data_, kind="box", size=4, aspect=0.7)
```
