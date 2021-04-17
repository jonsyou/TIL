# Pandas에서 데이터 프레임 열을 Datetime 유형으로 변환하기

```to_datetime()``` 함수는 <b>Pandas</b> ```DataFrame```에 존재하는 특정 변수의 타입을 ```datetime``` 타입으로 변환시키는 메서드이다.

아래의 코드와 같이 적용 가능하다.

```python
import pandas as pd
df['col_'] = pd.to_datetime(df['col_'], format='%Y-%m-%d %H:%M:%S', errors='raise')

```

```to_datetime( )``` 함수에 첫 번째 파라미터로 ```list``` 타입의 변수를 입력하면 ```datetimeIndex``` 타입의 객체가 반환된다.
대신에 ```Pandas```의 ```Series``` 타입 변수를 입력하면 ```datetime64```형태의 ```Series``` 타입 객체가 반환된다.

```format``` 파라미터에서 지정한 시간 포맷 :
```python
%Y: Year, ex) 2019, 2020
%m: Month as a zero-padded, ex) 01~12
%d: Day of the month as a zero-padded ex) 01~31
%H: Hour (24-hour clock) as a zero-padded ex) 01~23
%M: Minute as a zero-padded ex) 00~59
%S: Second as a zero-padded ex) 00~59
ex) 2019-09-01 19:30:00 =(Directivs)=> %Y-%m-%d %H:%M:%S
```

만약 ```format``` 파라미터 입력값을 정해주지 않으면 ```to_datetime()``` 함수가 문자열 패턴을 자동으로 읽어 ```datetime``` 형태로 변환해 준다. 
