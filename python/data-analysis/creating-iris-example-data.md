# iris 예제 데이터 생성하기

```iris``` 데이터는 Sir R.A. Fisher에 의해 처음 사용되었다. 
이후 R 프로그램의 내장된 데이터로써 분석가들 사이에서 더 잘 알려지게 되었다.

```iris``` 데이터는 총 150개의 레코드와 (인덱스를 제외한) 5개의 변수로 이루어져 있으며 붓꽃의 꽃잎과 꽃받침에 대해 각각 측정된 너비와 길이 값이 담겨있다.

Python에서는 ```sklearn.datasets``` 패키지를 사용하여 데이터 로드가 가능하며 아래의 코드를 통해 데이터에 대한 속성과 설명을 확인할 수 있다.
```python
from sklearn.datasets import load_iris

iris = load_iris()
print(iris.DESCR)
```

우리가 분석에 사용하기 쉽게 ```DataFrame``` 형태로 만들고자 할 때는 아래의 코드를 사용할 수 있다.
```python
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris() 

iris_ = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_['target'] = iris.target
iris_['target'] = iris_['target'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

iris_
```

새로운 코드를 익힌 코드를 예제 데이터에 바로 적용해보는 것은 중요한 연습 단계라고 생각한다. 
지금 바로 자신이 익힌 코드를 예제 데이터에 적용해보자.
