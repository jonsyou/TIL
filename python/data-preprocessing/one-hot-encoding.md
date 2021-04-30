# 원-핫 인코딩하기

원-핫 인코딩은 다수의 0과 유일한 1을 이용해 특정 클래스를 표현한다.
또한 각 클래스마다 정해져있는 위치에 유일한 1이 위치하도록 인코딩 하는 것을 의미한다.

만일 0부터 9까지 10개의 클래스가 있을 경우 0은 ```[1,0,0,0,0,0,0,0,0,0]```으로 인코딩 되며 6은
```[0,0,0,0,0,0,1,0,0,0]```으로 인코딩 된다.

<b>아래의 예시 코드 참조 :</b>
```python
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit(species.reshape(-1,1))

iris_onehot = enc.transform(species.reshape(-1,1))
iris_onehot

iris_onehot.toarray()
```

예시 코드와 같이 ```sklearn.preprocessing``` 의 ```OneHotEncoder``` 메서드를 사용하여 인코딩 가능하다.
