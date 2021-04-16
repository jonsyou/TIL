# Matplotlib를 활용한 한번에 다수의 Plot 그리기 및 레이아웃 설정

한 화면 속에 여러 그래프를 동시에 그릴 때 사용하는 코드이다.

우선 ```figure```함수를 활용해 <b>Figure</b> 객체를 만들고 ```.add_subplot()``` 메서드를 활용하면 여러 ```subplot```들을 생성할 수 있다. ```.add_subplot()``` 메서드에 원하는 레이아웃의 형태를 인자로 입력할 수 있다.

한번에 여러 ```subplot```을 그리는 코드 예시 :
```python
import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

x = range(0, 100)
y = [v*v for v in x]

ax1.plot(x, y)
ax2.bar(x, y)

plt.show()
```

또는 <b>Figure</b> 객체 생성 없이 바로 여러 ```subplot```을 생성하는 것도 가능하다.

```python
ax1= plt.subplot(121)
graph1= plt.plot([1,2,3])

ax2= plt.subplot(122)
graph2= plt.bar(x=[1,2,3], height=[1,2,3])

plt.show()
```
---

- <b>자동 레이아웃 설정</b>

 생성된 여러 ```subplot```중 어느 하나의 그래프가 다른 레이아웃 속의 그래프를 가려버리는 경우에는 ```.tight_layout()```함수를 사용하여 자동으로 레이아웃을 설정해 줄 수 있다.
```python
...
plt.tight_layout()
...
```
