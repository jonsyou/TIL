# 리스트나 튜플에서 Counter 함수를 활용해 빈도수 세기

데이터프레임에서는 ```value_counts()``` 메소드를 활용하는 것이 가능하지만 리스트와 튜플에서는 다른 방법을 활용해야한다. 

```Counter()```는 사전(```dict```) 클래스의 하위 클래스이며 빈도 계산 결과를 딕셔너리 형태로 반환해준다.

```python
from collections import Counter
tempList =  ['a','b','a','a','c','f']

result = Counter(tempList)
print(result)

for key in result:
    print(key, result[key])

# 값만 출력도 가능
result = Counter(tempList).values()
print(result)
```
이렇게 리스트나 튜플에서 빈도를 세기위하여 ```collections``` 모듈의 ```Counter``` 함수를 활용할 수 있다.
출력된 ```result``` 객체는 딕셔너리 형태로 반환이 된다.
