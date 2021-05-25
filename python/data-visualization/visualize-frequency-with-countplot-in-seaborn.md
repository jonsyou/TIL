# seaborn의 countplot로 빈도 시각화

```countplot``` 메소드를 활용하여 간단하게 특정 컬럼의 빈도 시각화가 가능하다.
```python
import matplotlib.pyplot as plt
import seaborn as sns
...
sns.countplot(x='col1', data=df, hue='col2')
plt.show()
```
```hue``` 설정도 가능하다.
