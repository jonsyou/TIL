# tqdm 모듈을 활용하여 반복문 진행상황 표시하기

반복문 실행 시 진행상황을 표시하기 위하여 ```tqdm``` 모듈을 활용할 수 있다. ```Progress Bar``` 형태로 보여주기 때문에 비교적 직관적이다.

<b>기본적인 활용법</b>

반복이 가능한(```iterable```) 대상이라면 ```tqdm``` 함수에 넣고 실행하면 된다.
```python
import time
from tqdm import tqdm

for i in tqdm(range(10)):
    time.sleep(0.1)
```

리스트에도 사용할 수 있다. 
```python
empty_list = []
for word in tqdm(['apple', 'ball', 'cat', 'doll', 'egg'], desc='iterate list'):
    time.sleep(0.1)
    empty_list.append(word)
```
```desc```를 이용하여 설명을 추가할 수도 있다.

반복문 밖에서 별도의 ```tqdm``` 객체를 생성하여 실행시키는 것도 가능하다.
```python
pbar = tqdm(['apple', 'ball', 'cat', 'doll', 'egg'])
for word in pbar :
    time.sleep(0.1)
    pbar.set_description(f'Processing {word}')
    empty_list.append(word)
```
