# Seaborn을 이용한 라인 차트 그리기

```seaborn```은 ```matplotlib```를 기반으로 하는 대표적인 시각화 라이브러리이다.
우리에게 매력적이고 유익한 통계 그래픽을 그리기 위한 높은 수준의 인터페이스를 제공해준다.

해당 글에서는 ```seaborn```에서 제공하는 ```.lineplot()```기능을 이용하여 라인 차트 그리는 법을 작성해 보았다.

우선 다음과 같은 형태의 ```DataFrame```이 필요하다.
예시로 각 노래마다의 글로벌 스트리밍 수 데이터를 사용하였다.
```python
# Path of the file to read
spotify_filepath = "../input/spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)
```
```index_col``` 옵션을 사용하여 ```index```로 사용할 컬럼을 지정해 주고 ```parse_dates=True``` 옵션을 사용하여 날짜 형식에 대한 형식을 활성화 해주었다.

읽어온 예시 데이터 :
```python
# Print the first 5 rows of the data
spotify_data.head()
```
||Shape of You|Despacito|Something Just Like This|HUMBLE.|Unforgettable|  
|--|--|--|--|--|--|					  
|Date||||||
|2018-01-05|4492978|3450315.0|2408365.0|2685857.0|2869783.0|  
|2018-01-06|4416476|3394284.0|2188035.0|2559044.0|2743748.0|  
|2018-01-07|4009104|3020789.0|1908129.0|2350985.0|2441045.0|  
|2018-01-08|4135505|2755266.0|2023251.0|2523265.0|2622693.0|  
|2018-01-09|4168506|2791601.0|2058016.0|2727678.0|2627334.0|  

예시 데이터는 보는 바와 같이 ```index```에 저장된 날짜별로 각 변수값들이 저장되어있다. 
간단한 라인 차트 시각화를 위해 데이터 형식을 위와 같이 만들어줄 필요가 있다.

이제 해당 코드를 통해 라인 차트를 그릴 수 있다.
```python
# Line chart showing daily global streams of each song 
sns.lineplot(data=spotify_data)
```
![image](https://user-images.githubusercontent.com/74973306/114709029-0ec64800-9d67-11eb-9e96-c842453a2f7a.png)

위와 같은 간단한 코드를 통해 각 변수 마다의 날짜별 라인 차트를 생성할 수 있다.

아래는 ```.figure()```과 ```.title()```을 이용해 크기와 제목을 수정한 라인 차트이다.
```python
# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Line chart showing daily global streams of each song 
sns.lineplot(data=spotify_data)
```
![image](https://user-images.githubusercontent.com/74973306/114709528-a7f55e80-9d67-11eb-8324-920a2f1a7ebd.png)

위와 같이 모든 변수에 해당하는 라인 차트를 손쉽게 그릴 수 있지만 상황에 따라 일부에 해당하는 라인 차트를 그리고 싶을 때가 있다.
그럴때는 아래와 같이 출력 하고싶은 몇가지의 정보만 라인 차트로 그릴 수도 있다.
```python
# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")

# Line chart showing daily global streams of 'Despacito'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")

# Add label for horizontal axis
plt.xlabel("Date")
```
![image](https://user-images.githubusercontent.com/74973306/114709871-0de1e600-9d68-11eb-9f9e-44df145c6bda.png)
