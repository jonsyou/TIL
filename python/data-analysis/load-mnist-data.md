# MNIST 데이터 읽어오기

```python
from keras.datasets import mnist

# MNIST 데이터 읽어 들이기 --- (※1)
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 데이터를 float32 자료형으로 변환하고 정규화하기 --- (※2)
X_train = X_train.reshape(60000, 784).astype('float32')
X_test = X_test.reshape(10000, 784).astype('float')

X_train /= 255
X_test /= 255

# 레이블 데이터를 0-9까지의 카테고리를 나타내는 배열로 변환하기 --- (※2a)
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)
```
