# value_counts 로 pie그래프 그리기

데이터프레임에서 바로 ```pie chart``` 그릴때 유용한 코드이다.

```python
plt.figure(figsize=(7,7))

plt.title('Title_', fontsize = 15)

p1['Col_1'].value_counts().plot.pie(autopct = '%.2f%%',
                                     textprops = {'fontsize' : 12,
                                                  'weight' : 'bold'})
plt.show()
```
```pie chart```는 해당 원소의 빈도 비율을 표시할 때 유용하다.
