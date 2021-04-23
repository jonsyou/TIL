# ARIMA 모델을 이용한 시계열 예측 분석

<b>ARIMA</b>(<b>A</b>uto<b>R</b>egressive <b>I</b>ntegrated <b>M</b>oving <b>A</b>verage) 모델은 시계열 데이터를 분석하고 예측하기 위한 통계 모델이다. 한국어로는 <b>자기회귀 누적 이동평균 모델</b>이라고 부른다.

<b>ARIMA</b> 의 약어는 모델 자체의 주요한 정보를 설명해 준다. 

요약하자면 다음과 같다.
- <b>AR</b>: 자기 회귀 모델. 관측치와 일부 지연 관측치 사이의 종속 관계를 사용하는 모형
- <b>I</b>: 차분한 횟수. 시계열을 정상 시계열 상태로 만들기 위해 원시 관측치 차이(예: 이전 시간 단계에서 관측치에서 관측치를 뺀 것)를 사용하는 것
- <b>MA</b>: 이동 평균 모델. 지연된 관측치에 적용된 이동 평균 모형의 관측치와 잔차 오차 사이의 종속성을 사용하는 모형

이러한 각 성분은 모형에 모수로 명시적으로 지정되어 있다.
표준 표기법은 <b>ARIMA(p, d, q)</b>에서 사용되는 특정 <b>ARIMA</b> 모델을 신속하게 나타내기 위해 파라미터가 정숫값으로 대체되는 경우 사용된다.

<b>기본적인 ARIMA 모델 코드 :</b>
```python
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm


model = ARIMA(df_.col_1.values, order = (p,d,q))
model_fit = model.fit(trend = 'c', full_output = True, disp = True)
print(model_fit.summary())
```

<b>학습 데이터에 대한 예측 결과 시각화 :</b>
```python
fig = model_fit.plot_predict()
```

<b>실제값과 예측값의 잔차 시각화 코드 :</b>
```python
residuals = pd.DataFrame(model_fit.resid)
residuals.plot(title = "실제값과 예측값의 잔차")
```

<b>이후 시기를 예측하는 코드:</b>
```python
forecast_data = model_fit.forecast(steps=5) 
```
