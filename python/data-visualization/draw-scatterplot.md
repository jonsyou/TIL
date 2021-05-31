# 산점도 그리기

산점도를 그리기 위하여 ```matplotlib``` 라이브러리를 활용할 수 있다.
```python
import matplotlib.pyplot as plt 
```

아래와 같이 ```x축```과 ```y축```의 기준으로 삼을 컬럼을 설정하고 ```'.'``` 를 활용하여 산점도로 표현하는 기능을 활성화 시킨다. 
```python
plt.plot(data_['col_1'],data_['col_2'], '.', markersize=1 )
plt.show()
```
산점도는 두 변수사이의 상관관계를 파악하는데 유용하다.
