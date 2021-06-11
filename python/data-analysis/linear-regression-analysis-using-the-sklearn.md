# sklearn을 활용한 선형회귀분석

```python
from sklearn.linear_model import LinearRegression
mlr = LinearRegression()
mlr.fit(x_train, y_train) 

my_apartment = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 1, 1, 0]] # 모델 예측값을 추출하고자 하는 데이터

my_predict = mlr.predict(my_apartment)
y_predict = mlr.predict(x_test)

mlr.score(x_train, y_train)
```
