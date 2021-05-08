# 서포트 벡터 머신(SVM)을 사용한 다중 클래스 분류
 
<b>SVM</b>은 분류 또는 회귀 문제에 도움이 되는 지도 학습 알고리즘이다. 가능한 출력 간 최적의 경계를 찾는 것을 목표로 한다.

간단히 말해 <b>SVM</b>은 선택한 커널 기능에 따라 복잡한 데이터 변환을 수행하며,
이러한 변환을 기반으로 사용자가 정의한 레이블 또는 클래스에 따라 데이터 지점 간의 분리 경계를 최대화한다.

우리는 ```sklearn``` 모듈을 사용하여 SVM 모델을 사용할 수 있다.

<b>예시 코드:</b>

- 라이브러리 세팅
```python
from sklearn import svm, datasets
import sklearn.model_selection as model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
```

- 예시 데이터 생성
```python
iris = datasets.load_iris()
```

- 데이터 분할
```python
X = iris.data[:, :2]
y = iris.target
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, train_size=0.80, test_size=0.20, random_state=101)
```
- ```svm``` 모델 생성
```python
rbf = svm.SVC(kernel='rbf', gamma=0.5, C=0.1).fit(X_train, y_train)
poly = svm.SVC(kernel='poly', degree=3, C=1).fit(X_train, y_train)
```
```kernel```이 각각 ```rbf```와 ```poly```인 두가지 모델 생성

- 모델 학습
```python
poly_pred = poly.predict(X_test)
rbf_pred = rbf.predict(X_test)
```
- 모델 성능 확인 (```kernel='poly'```)
```python
poly_accuracy = accuracy_score(y_test, poly_pred)
poly_f1 = f1_score(y_test, poly_pred, average='weighted')
print('Accuracy (Polynomial Kernel): ', "%.2f" % (poly_accuracy*100))
print('F1 (Polynomial Kernel): ', "%.2f" % (poly_f1*100))
```
- 모델 성능 확인 (```kernel='rbf'```)
```python
rbf_accuracy = accuracy_score(y_test, rbf_pred)
rbf_f1 = f1_score(y_test, rbf_pred, average='weighted')
print('Accuracy (RBF Kernel): ', "%.2f" % (rbf_accuracy*100))
print('F1 (RBF Kernel): ', "%.2f" % (rbf_f1*100))
```
이렇게 ```sklearn```의 ```SVM``` 모델을 통해 다중 클래스 비교가 가능하다. 
