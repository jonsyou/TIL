# replace 메소드를 활용한 문자열 변경

문자열에서 특정 문자를 일괄적으로 바꾸는 행위는 ```replace()``` 메소드로 구현 가능하다.

```python
>>> a = 'hello-world'
>>> a.replace('-','')
helloworld
```

아래와 같이 세번째 숫자형 매개변수를 지정해주면 해당 숫자만큼 변경이 진행된다. 디폴트 값은 ```-1``` 이며 일괄 변경이라는 뜻이다. 
```python
>>> a = 'hello-world'
>>> a.replace('o','',1)
hell-world
```
