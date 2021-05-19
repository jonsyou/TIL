# enumerate를 활용한 반복문 인덱스 부여하기

반복문 사용 시 각 반복의 번호를 부여하기 위해 ```enumerate```함수를 사용할 수 있다.

함수 사용 시 인덱스 번호와 컬렉션의 원소를 ```tuple``` 형태로 반환해준다.

```python
>>> t = [1, 5, 7, 33, 39, 52]
>>> for p in enumerate(t):
...     print(p)
... 
(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)
```

아래와 같이 반환하여 사용하는 것도 가능하다.
```python
>>> for i, v in enumerate(t):
...     print("index : {}, value: {}".format(i,v))
... 
index : 0, value: 1
index : 1, value: 5
index : 2, value: 7
index : 3, value: 33
index : 4, value: 39
index : 5, value: 52
```
