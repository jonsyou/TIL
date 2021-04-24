# read_csv 함수 활용 시 날짜/시간 파싱 하기

<b>Pandas</b>의 ```read_csv()``` 함수를 사용하여 ```DataFrame``` 객체를 생성할 때 날짜/시간 정보가 존재한다면 ```DateTime``` 형태에 맞도록 파싱 하여 읽어오는 방법이다.

날짜/시간 포맷 지정 없이 ```read_csv()```를 활용하여 날짜/시간 데이터를 읽어오는 경우에는 자동으로 지정되는 것이 아니라 ```object``` 형태로 불러오게 된다.
이러한 경우에는 ```Datetime``` 포맷으로 설정하기 위해 한 번 더 전처리를 해야 하기 때문에 코드가 좀 더 복잡해질 수 있다.

그렇기 때문에 몇 가지 간단한 옵션을 활용하여 데이터를 불러올 때부터 ```Datetime``` 형태로 지정해 주는 것이 더 편리할 수 있다.  

<b>예시 코드 :</b>
```python
import pandas as pd

df_date = pd.read_csv("sample.csv", parse_dates=['date_col'], dayfirst=True, infer_datetime_format=True)
```
위와 같이 ```parse_dates```, ```dayfirst```, ```infer_datetime_format``` 옵션을 사용하여 날짜/시간 데이터를 상황에 맞게 ```Datetime``` 포맷 형태로 읽어올 수 있다.
- ```parse_dates``` : ```Datetime``` 포맷 형태로 불러올 변수 지정
- ```dayfirst``` : 만약 일이 월보다 먼저 위치하는 형태일 때 ```True```로 설정
- ```infer_datetime_format``` : ```True```로 옵션을 활성화하면 날짜 시간 포맷을 자동으로 추정

또는 ```date_parser=Parser``` 옵션을 활용하여 직접 날짜/시간 파싱의 포맷을 지정해 줄 수도 있다.

<b>예시 코드 :</b>
```python
import pandas as pd
from datetime import datetime

dt_parser = lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M:%S")
df_date = pd.read_csv("sample.csv", parse_dates=['date_col'], date_parser=dt_parser)
```
