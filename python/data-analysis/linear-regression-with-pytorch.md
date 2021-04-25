# Pytorch를 활용한 선형 회귀 분석

```pytorch``` 를 활용하여 선형 회귀 모델을 만드는 간단한 예제 코드이다.

선형 회귀란 우리가 잘 알다시피 학습하는 데이터를 가장 잘 나타내주는 하나의 직선 방정식을 찾는 문제로 풀이될 수 있다.

```pytorch``` 를 활용한 선형 회귀 모델은 기존의 통계학적 선형 회귀 모델과는 조금 다르게 반복적인 학습을 통하여 최적의 직선 방정식을 찾는다.
여기서는 신경망 학습에서 사용되는 비용 함수와 경사 하강법과 같은 개념을 활용한다.

우선 아래의 코드를 실행하여 기본적인 모듈을 셋팅한다.
```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
```

통계학적 방법과는 다르게 신경망 학습처럼 선형 회귀 모델을 구축할 때에는 ```seed``` 를 고정시켜주지 않으면 생성 모델의 계산 결과가 매번 다를 수 있다.
```python
torch.manual_seed(1)
```
우리는 재현성을 얻기 위해 위의 코드를 활용하여 seed를 고정해줄 수 있다.

그 후 변수 선언을 통해 ```x```값과 ```y```값을 지정해 줄 수 있다.
```python
# 데이터
x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[2], [4], [6]])
```
위의 코드에서는 ```x_train``` 과 ```y_train``` 변수를 선언해주었다.

그리고 최적의 선형 회귀식을 찾기위해 가중치와 편향의 초기화를 진행해준다.
```python
# 모델 초기화
W = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)
```
가중치 ```W```를 0으로 초기화 해주었다. ```requires_grad=True``` 라는 인자 설정을 통해 이 변수는 학습을 통해 계속 값이 변경되는 변수임을 설정해 주었다.

경사 하강법을 구현해 줄 수 있다.
```python
# optimizer 설정
optimizer = optim.SGD([W, b], lr=0.01)
```

그리고 원하는 만큼의 반복된 학습을 통하여 모델을 갱신한다.
```python
nb_epochs = 1999 # 원하는만큼 경사 하강법을 반복
for epoch in range(nb_epochs + 1):

    # H(x) 계산
    hypothesis = x_train * W + b

    # cost 계산
    cost = torch.mean((hypothesis - y_train) ** 2)

    # cost로 H(x) 개선
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    # 100번마다 로그 출력
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} W: {:.3f}, b: {:.3f} Cost: {:.6f}'.format(
            epoch, nb_epochs, W.item(), b.item(), cost.item()
        ))
```
