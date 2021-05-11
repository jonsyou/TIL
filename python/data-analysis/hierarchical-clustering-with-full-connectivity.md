# 완전연결(complete linkage)을 이용한 계층적 클러스터링

```python
from scipy.spatial.distance import pdist, squareform
distmatrix = pdist(df, metric='euclidean') # 두 점 사이의 거리 계산
row_dist = pd.DataFrame(squareform(distmatrix), columns=labels, index=labels)
print(row_dist) # 두점 사이 거리 계산값 출력
from scipy.cluster.hierarchy import linkage # linkage() : 응집형 계층적 클러스터링 수행
row_clusters = linkage(distmatrix, method='complete')
row_clusters
pd.DataFrame(row_clusters, columns=['클러스터ID_1', '클러스터ID_2', '거리', '클러스터 멤버수'],
 index=['클러스터 %d' % (i+1) for i in range(row_clusters.shape[0])])
from scipy.cluster.hierarchy import dendrogram # dendrogram() : 클러스터의 계층 구조를 표현
row_dendrogram = dendrogram(row_clusters, labels=labels)
plt.rcParams["font.family"] = 'Malgun Gothic'
plt.tight_layout()
plt.ylabel('유클리드 거리')
plt.show()
```
