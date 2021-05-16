# StandardScaler를 활용한 스케일 조정

평균 0 , 분산 1의 분포로 조정해준다.
보통의 싸이킷런 함수들과 비슷하게 ```fit```, ```transform```, ```fit_transform```을 다 지원한다.

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# 메소드체이닝(chaining)을 사용하여 fit과 transform을 연달아 호출합니다
X_scaled = scaler.fit(X_train).transform(X_train)

# 위와 동일하지만 더 효율적입니다(fit_transform)
X_scaled_d = scaler.fit_transform(X_train)

#해당 fit으로 test데이터도 transform 해줍니다
X_test_scaled = scaler.transform(X_test)

plt.scatter(X_scaled[:,0],X_scaled[:,1])
```
