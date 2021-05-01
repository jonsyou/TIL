# 혼동 행렬 (Create Confusion Matrix) 생성

```Confusion Matrix```는 예측값 들 중 얼마나 실제값을 잘 맞혔는지, 또는 틀리게 예측했는지에 대한 정보를 통해 성능을 다각도로 검증해볼 수 있다.

```sklearn.metrics```의 ```confusion_matrix``` 메서드를 통해 계산 가능하다.

<b>Confusion Matrix 생성 코드 :</b>
```python
from sklearn.metrics import confusion_matrix

pred = model.predict(X_test)
confMatrix = confusion_matrix(y_test, pred)
print("Confusion Matrix : \n : ", confMatrix)
```
위의 코드는 텍스트로 혼동 행렬을 표현해 주기 때문에 직관성이 떨어진다.

좀 더 직관적인 이해를 돕기 위해 우리는 ```scikit-plot```을 이용하여 ```confusion matrix```를 ```heatmap```으로 시각화할 수 있다.
```scikit-learn```에서는 가로축과 세로축의 라벨이 없었던 반면에 ```scikit-plot```은 축 라벨이 있어서 결과를 해석하기가 좀 더 용이하다.

<b>Confusion Matrix Heatmap 시각화 코드 :</b>
```python
import scikitplot as skplt
import matplotlib.pyplot as plt

pred = model.predict(X_test)
skplt.metrics.plot_confusion_matrix(y_test, pred)
plt.show()
```
