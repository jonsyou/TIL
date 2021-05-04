# Sklearn의 cross_val_score 메서드에서 Custom Scoring 적용하기

```Sklearn``` 모듈의 ```cross_val_score()``` 메서드를 사용할 때 이미 존재하는 다양한 ```Scoring``` 방법을 사용할 수 있다.
하지만 때로는 본인이 생성한 ```Scoring``` 기준이 필요할 경우가 있다.

그럴때는 아래와 같이 ```Custum Scoring```을 만들어 적용할 수 있다.

<b>Custum Scoring 함수 만들기 코드 :</b>
```python

def scoring_method(y_test, y_pred):
    ...
    return ...

def custom_scoring(y_test, y_pred):
    scoring_value = scoring_method(y_test, y_pred)
    return scoring_value
```
이렇게 비교 기준 식을 정의하여 추후 매개변수에 적용가능하다.

<b>cross_val_score 메서드에서 Custum Scoring 함수 사용하기 코드 :</b>
```python
from sklearn.model_selection import cross_val_score

# cross_val_score 진행
scores = cross_val_score(...,scoring=make_scorer(custom_scoring,greater_is_better=False))
```

```cross_val_score``` 파라메터 중 ```make_scorer``` 객체인 ```scoring```의 세부 옵션
  - ```custom_scoring``` : ```custom scoring``` 함수 (위에서 정의한 함수)
  - ```greater_is_better``` : ```False```는 ```score``` 값이 낮은게 좋음을 의미

