# 데이터프레임 컬럼 및 인덱스 이름 바꾸기

<b>Pandas</b>의 ```rename()``` 메서드를 사용하면 손쉽게 컬럼 및 인덱스의 이름을 바꿀 수 있다.

<b>예시 코드 :</b>
```python
# 컬럼명 바꾸기
df.rename(columns = {'col_old' : 'col_new'}, inplace = True)

# 인덱스명 바꾸기
df.rename(index = {'old_ind': 'new_ind'}, inplace = True)
```
```inplace``` 매개변수를 이용하면 따로 데이터프레임을 선언해 줄 필요 없이 바로 기존의 데이터프레임에 적용된다.
