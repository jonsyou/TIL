# 케라스 Sequential 모델 시작하기

수많은 딥러닝 프레임워크들 중에서 <b>Keras</b>는 업계와 학계 양쪽에서 모두 폭넓게 사용되고 있다.

```Sequential``` 모델은 레이어를 선형으로 연결하여 구성한다. 레이어의 인스턴스를 생성자에게 넘겨줌으로써 ```Sequential``` 모델을 구성할 수 있다.

```python
from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential([
    Dense(32, input_shape=(784,)),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])
```
또한, ```.add()``` 메소드를 통해서 쉽게 레이어를 추가할 수 있다.

```python
model = Sequential()
model.add(Dense(32, input_dim=784))
model.add(Activation('relu'))
```

[source](https://keras.io/ko/getting-started/sequential-model-guide/)
