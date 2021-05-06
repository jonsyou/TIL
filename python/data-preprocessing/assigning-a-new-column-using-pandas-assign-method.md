# Pandas의 assign 메서드를 이용한 새 컬럼 할당하기

```assign()``` 메서드를 이용하여 기존 열과 함께 새 열이 할당 된 ```DataFrame``` 개체를 반환할 수 있다.

```python
import pandas as pd

df = pd.DataFrame({'Cost Price': 
                   [100, 200], 
                   'Selling Price':
                   [200, 400]})

new_df=df.assign(Profit=df["Selling Price"]-
                        df["Cost Price"])
print(new_df)
```

```lambda x``` 를 활용하여 새로운 컬럼을 생성할 수도 있다.
```python
import pandas as pd

df = pd.DataFrame({'Cost_Price': 
                   [100, 200], 
                   'Selling_Price': 
                   [200, 400]})

new_df=df.assign(Profit=lambda x: 
                 x.Selling_Price-
                 x.Cost_Price)

print(new_df)
```
