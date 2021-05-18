# timedelta를 활용한 날짜 연산

날짜 연산이 필요할 때 ```timedelta```를 활용하면 수월하게 가능하다.

```timedelta```는 ```datetime``` 모듈안에 포함되어있다.

<b>예시 코드:</b>
```python
>>> import pandas as pd
>>> from datetime import datetime, timedelta

>>> type(temp)
pandas._libs.tslibs.timestamps.Timestamp

>>> temp_ = temp[0] + timedelta(days=1)
```
여기서 ```temp``` 객체는 <b>Pandas</b> 데이터프레임의 ```datetime``` 타입의 어느 컬럼이라고 가정한다.

연산은 ```days```, ```seconds```, ```microseconds```, ```milliseconds```, ```minutes```, ```hours```, ```weeks``` 단위로 가능하다.
