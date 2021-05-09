```python

# 랜덤포레스트를 이용한 영향력 도출
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=10).fit(X_train_scaled, y_train)
cross_val_score(rf, X_train_scaled, y_train, cv=3)
rf.score(X_test_scaled, y_test)
print(classification_report(y_test, rf.predict(X_test_scaled)))

feature_importance_rf = pd.DataFrame(zip(X.columns.values, rf.feature_importances_))
feature_importance_rf.columns = ['feature', 'importance']
feature_importance_rf.sort_values("importance", ascending=False, inplace=True)

```
