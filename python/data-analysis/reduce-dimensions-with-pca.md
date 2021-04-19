# 주성분 분석(PCA)을 활용한 차원 축소

<b>주성분 분석</b>, 영어로는 <b>PCA(Principal Component Analysis)</b>이다.

<b>주성분 분석</b>이란 기존 다차원이었던 데이터의 정보량을 최대한 유지한 채 비교적 최소한의 정보량 손실로 데이터의 <b>차원을 축소시켜 분석</b>하는 방법이다.

아래의 코드로 주성분 분석이 가능하다.
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2) # 주성분을 몇개로 할지 결정
printcipalComponents = pca.fit_transform(x)
```
변수마다의 단위가 다를 때는 주성분 분석을 실시하기 전에 데이터 스케일링을 해주면 값의 크기에 따라 설명 가능한 분산량이 왜곡되지 않게끔 할 수 있다.


아래와 같이 ```StandardScaler``` 메소드를 활용하여 데이터 스케일링이 가능하다.
```python
from sklearn.preprocessing import StandardScaler  # 표준화 패키지 라이브러리 
x = StandardScaler().fit_transform(x)
```
차원 축소를 통해 <b>차원의 저주 탈피</b>, 그리고 <b>시각화의 용이성</b>이라는 이점을 얻을 수 있다.

---
## <b>차원의 저주 및 차원 축소의 개념</b>

우선 변수의 수가 늘어나 차원이 커지면서 발생하는 문제를 <b>차원의 저주</b>라고 한다. 
차원을 축소시키는 방법의 종류를 크게 2가지로 나눌 수 있다.

<br>

- <b>Feature Selection</b>(변수 선택)  
  - 기존 변수들 가운데 중요한 변수 몇 가지만 <b>선택</b>하여 차원을 축소시키는 개념
- <b>Feature Extraction</b>(변수 추출)  
  - 변수들의 관계를 활용하여 정보량을 <b>추출</b>하는 방법
