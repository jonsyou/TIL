```python
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.5, min_samples=10)
db.fit(iris_data_pd.iloc[:, 2:4])
y_pred = db.fit_predict(iris_data_pd.iloc[:, 2:4])
plt.scatter(iris_data_pd.iloc[:, 2], iris_data_pd.iloc[:, 3], c=y_pred)
plt.title('Density Clustering')
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.show()
```
