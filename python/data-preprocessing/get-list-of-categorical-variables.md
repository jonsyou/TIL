# 범주형 변수명 리스트로 가져오기

데이터의 많은 변수 중 범주형 변수명만을 선택하여 리스트로 저장하는 코드이다.

```python
# Get list of categorical variables
s = (X_train.dtypes == 'object')
object_cols = list(s[s].index)

print("Categorical variables:")
print(object_cols)
```
위의 간단한 코드를 통해 범주형 변수 선택가능하다.

위의 코드 실행시 출력되는 값 예시:
```python
[out]
'''
Categorical variables:
['Categorical_1', 'Categorical_2', 'Categorical_3']
'''
```  

---

- <b>저차원 범주형 변수명 리스트로 가져오기</b>

만약 범주형 변수에서 조건을 더 강화하여 변수 내 고유 값의 수가 적은 변수만을 선택할 수도 있다.  

아래의 코드를 통해 저차원 범주형 변수 선택이 가능하다.
```python
low_cardinality_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and 
                        X_train_full[cname].dtype == "object"]
```
