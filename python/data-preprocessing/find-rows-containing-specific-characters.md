# 특정 문자가 포함된 행 찾기

<b>Pandas</b>의 데이터프레임에서 특정 문자가 포함된 행만 골라내는 것은 ```contains()``` 메서드를 활용하면 가능하다. 분석을 하다보면 해당 코드를 써야할 경우가 종종 생기므로 잘 알아두자.

<b>특정 문자 포함된 행 찾기 예시 코드:</b>
```python
# 해당 문자가 포함된 행
df[df['content'].str.contains('해당 문자')]

# 해당 문자가 포함되지 않은 행
df[~df['content'].str.contains('해당 문자')]
```

<b>두 문자중 하나라도 포함된 행 찾기 예시 코드:</b>
```python
df_seoul[df_seoul['상호명'].str.contains('배스킨|던킨')].copy()
```
