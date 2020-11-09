### numpy 属性
```python
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```
- 维度
    ```
    print(array.ndim)
    
    >> 2
    ```
- 形状
    ```
    print(array.shape)
    >> (3, 3)
    ```
- 大小
    ```
    print(array.size)
    >> 9
    ```

- 元素类型
    ```
    print(array.dtype)
    >> int64
    ```
  
### numpy 创建数组
- 创建一维数组
    ```
    a = np.array([1, 2, 3], dtype=np.int32)
    print(a)
    >> [1 2 3]
    ```
- 创建二维数组
    ```
    b = np.array([[1, 2, 3], [4, 5, 6]])
    print(b)
    >> [[1 2 3]
    >>  [4 5 6]]
    ```

- 创建2行3列全为0的数组
    ```
    zero = np.zeros((2, 3))
    print(zero)
    >> [[0. 0. 0.]
    >>  [0. 0. 0.]]
    ```

- 生成三行四列全为1的矩阵
    ```
    one = np.ones((3, 4))
    print(one)
    >> [[1. 1. 1. 1.]
    >>  [1. 1. 1. 1.]
    >>  [1. 1. 1. 1.]]
    ```

- 生成3行2列全都接近于0但不是0的数
    ```
    empty = np.empty((3, 2))
    print(empty)
    >> [[0. 0.]
    >>  [0. 0.]
    >>  [0. 0.]]
    ```

- 生成从0到10不包含10的一维数组
    ```
    e = np.arange(10)
    print(e)
    >> [0 1 2 3 4 5 6 7 8 9]
    ```

- 生成从4到10不包含10的一维数组
    ```
    f = np.arange(4, 10)
    print(f)
    >> [4 5 6 7 8 9]
    ```

- 生成从1到20不包含20,间隔为3的一维数组
    ```
    g = np.arange(1, 20, 3)
    print(g)
    >> [ 1  4  7 10 13 16 19]
    ```

- 重新定义矩阵形状
    ```
    h = np.arange(8).reshape(2, 4)
    print(h)
    >> [[0 1 2 3]
    >>  [4 5 6 7]]
    ```

### numpy 随机数
- 生成3行2列从0到1的随机数
    ```
    sample = np.random.random((3, 2))
    print(sample)
    >> [[0.94800964 0.91867228]
    >>  [0.3680591  0.14434706]
    >>  [0.33398542 0.50719141]]
    ```

- 生成3行2列符合标准正态分布的随机数
    ```
    sample2 = np.random.normal(size=(3, 2))
    print(sample2)
    >> [[ 0.22708609 -0.79131841]
    >>  [ 0.66393757 -0.18234665]
    >>  [ 0.98113021  0.93463262]]
    ```

- 生成3行2列从0到10的随机整数
    ```
    sample3 = np.random.randint(0, 10, size=(3, 2))
    print(sample3)
    >> [[4 7]
    >>  [5 9]
    >>  [6 2]]
    ```

### numpy 运算
#### 基本运算

```
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)
>> [[1 2 3]
>>  [4 5 6]]

arr2 = np.array([[1, 1, 2], [2, 3, 3]])
print(arr2)
>> [[1 1 2]
>>  [2 3 3]]
```

- 矩阵加法，按位加
    ```
    print(arr1 + arr2)
    >> [[2 3 5]
    >>  [6 8 9]]
    ```

- 减法， 按位减
    ```
    print(arr1 - arr2)
    >> [[0 1 1]
    >>  [2 2 3]]
    ```
- 矩阵乘法， 按位乘
    ```
    print(arr1 * arr2)
    >> [[ 1  2  6]
    >>  [ 8 15 18]]
    ```

- 幂运算， 按位
    ```
    print(arr1 ** arr2)
    >> [[  1   2   9]
    >>  [ 16 125 216]]
    ```

- 除法， 按位相除
    ```
    print(arr1 / arr2)
    >> [[1.         2.         1.5       ]
    >>  [2.         1.66666667 2.        ]]
    ```

- 取余，按位
    ```
    print(arr1 % arr2)
    >> [[0 0 1]
    >>  [0 2 0]]
    ```

- 取整，按位
    ```
    print(arr1 // arr2)
    >> [[1 2 1]
    >>  [2 1 2]]
    ```

- 矩阵每一个元素加2
    ```
    print(arr1 + 2)
    >> [[3 4 5]
    >>  [6 7 8]]
    ```

- 矩阵每一个元素乘10
    ```
    print(arr1 * 10)
    >> [[10 20 30]
    >>  [40 50 60]]
    ```

- 判读矩阵中每个元素是否大于3
    ```
    print(arr1 > 3)
    >> [[False False False]
    >>  [ True  True  True]]
    ```

#### 其他运算

- 矩阵的乘法
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    sample2 = np.ones((2, 3))
    print(sample2)
    >> [[1. 1. 1.]
    >>  [1. 1. 1.]]
    print(np.dot(sample, sample2))
    >> [[11. 11. 11.]
    >>  [14. 14. 14.]
    >>  [ 8.  8.  8.]]
    
    print(sample.dot(sample2))
    >> [[11. 11. 11.]
    >>  [14. 14. 14.]
    >>  [ 8.  8.  8.]]
    ```
  
- 矩阵的转置
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(sample.T)
    >> [[4 5 6]
    >>  [7 9 2]]
    print(np.transpose(sample))
    >> [[4 5 6]
    >>  [7 9 2]]
    ```

- 求和
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(np.sum(sample))
    >> 33
    ```

- 列求和
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(np.sum(sample, axis=0))
    >> [15 18]
    ```

- 行求和
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(np.sum(sample, axis=1))
    >> [11 14  8]
    ```
  
- 最小值
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(np.min(sample))
    >> 2
    ```

- 最大值
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(np.max(sample))
    >> 9
    ```

- 最小值的索引
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(np.argmin(sample))
    >> 5
    print(sample.argmin())
    >> 5
    ```
  
- 最大值的索引
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(np.argmax(sample))
    >> 3
    print(sample.argmax())
    >> 3
    ```

- 所有元素的平均值
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(np.mean(sample))
    >> 5.5
    print(sample.mean())
    >> 5.5
    ```

- 所有元素的中位数
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(np.median(sample))
    >> 5.5
    ```

- 所有元素开方
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(np.sqrt(sample))
    >> [[2.         2.64575131]
    >>  [2.23606798 3.        ]
    >>  [2.44948974 1.41421356]]
    ```
- 排序(行)
    ```
    sample = np.array([[4, 7], [5, 9], [6, 2]])
    print(np.sort(sample))
    >> [[4 7]
    >>  [5 9]
    >>  [2 6]]
    ```

- 小于2的变成2，大于7的变成7， 控制数字范围
    ```
    sample = np.random.randint(0, 10, size=(1, 10))
    print(sample)
    >> [[7 4 1 1 7 6 3 3 7 2]]
    print(np.clip(sample4, 2, 7))
    >> [[7 4 2 2 7 6 3 3 7 2]]
    ```

### numpy 索引
```
import numpy as np

arr1 = np.arange(2, 14)
print(arr1)
>> [ 2  3  4  5  6  7  8  9 10 11 12 13]
arr2 = arr1.reshape(3, 4)
print(arr2)
>> [[ 2  3  4  5]
>>  [ 6  7  8  9]
>>  [10 11 12 13]]
```

- 第二个位置的数据
    ```
    print(arr1[2])
    >> 4
    ```

- 第一到第四个位置的数据
    ```
    print(arr1[1:4])
    >> [3 4 5]
    ```

- 从第二个位置到倒数第一个位置的数据
    ```
    print(arr1[2:-1])
    >> [ 4  5  6  7  8  9 10 11 12]
    ```

- 前5个数据
    ```
    print(arr1[:5])
    >> [2 3 4 5 6]
    ```

- 后两个数据
    ```
    print(arr1[-2:])
    >> [12 13]
    ```

- 第二个位置的数据
    ```
    arr2 = arr1.reshape(3, 4)
    print(arr2)
    ```

- 第二行第二列元素
    ```
    print(arr2[1][1])
    >> 7
    print(arr2[1, 1])
    >> 7
    ```

- 所有行的第二列
    ```
    print(arr2[:, 2])
    >> [ 4  8 12]
    ```
  
- 迭代行
    ```
    for i in arr2:
        print(i)
    >> [2 3 4 5]
    >> [6 7 8 9]
    >> [10 11 12 13]
    ```

- 迭代列
    ```
    for i in arr2.T:
        print(i)
    >> [ 2  6 10]
    >> [ 3  7 11]
    >> [ 4  8 12]
    >> [ 5  9 13]
    ```

- 一个一个元素迭代
    ```
    for i in arr2.flat:
        print(i)
    >> 2
    >> 3
    >> 4
    >> 5
    >> 6
    >> 7
    >> 8
    >> 9
    >> 10
    >> 11
    >> 12
    >> 13
    ```

### numpy 数组合幷
```
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
```
- 垂直合并
    ```
    arr3 = np.vstack((arr1, arr2))
    print(arr3)
    >> [[1 2 3]
    >>  [4 5 6]]
    ```

- 水平合并
    ```
    arr4 = np.hstack((arr1, arr2))
    print(arr4)
    print(arr4.shape)
    >> [1 2 3 4 5 6]
    >> (6,)
    ```

- 垂直合并, 合并array的维度要相同，形状要匹配
    ```
    arr = np.concatenate((arr1, arr1), axis=0)
    print(arr)
    >> [1 2 3 1 2 3]
    ```

- 纵向合并，合并array的维度要相同，形状要匹配, 不能是一维数据
    ```
    arr = np.concatenate((arr3, arr3), axis=1)
    print(arr)
    >> [[1 2 3 1 2 3]
    >>  [4 5 6 4 5 6]]
    ```

- 在前面增加維度
    ```
    arr1_1 = arr1[np.newaxis, :]
    print(arr1_1)
    >> [[1 2 3]]
    ```
  
- 在后面增加維度
    ```
    arr1_2 = arr1[:, np.newaxis]
    print(arr1_2)
    >> [[1]
    >>  [2]
    >>  [3]]
    ```

- 将数据转换成二维数据
    ```
    arr1_3 = np.atleast_2d(arr1)
    print(arr1_3)
    >> [[1 2 3]]
    ```

### numpy 数组拆分
```
import numpy as np

arr1 = np.arange(12).reshape((3, 4))
print(arr1)
>> [[ 0  1  2  3]
>>  [ 4  5  6  7]
>>  [ 8  9 10 11]]
```

- 水平方向分成两份，等分
    ```
    arr2, arr3 = np.split(arr1, 2, axis=1)
    print(arr2)
    >> [[0 1]
    >>  [4 5]
    >>  [8 9]]
    print(arr3)
    >> [[ 2  3]
    >>  [ 6  7]
    >>  [10 11]]
    ```

- 垂直方向分割, 等分
    ```
    arr4, arr5, arr6 = np.split(arr1, 3, axis=0)
    print(arr4)
    >> [[0 1 2 3]]
    print(arr5)
    >> [[4 5 6 7]]
    print(arr6)
    >> [[ 8  9 10 11]]
    ```

- 水平方向分成三份, 不等分
    ```
    arr7, arr8, arr9 = np.array_split(arr1, 3, axis=1)
    print(arr7)
    >> [[0 1]
    >>  [4 5]
    >>  [8 9]]
    print(arr8)
    >> [[ 2]
    >>  [ 6]
    >>  [10]]
    print(arr9)
    >> [[ 3]
    >>  [ 7]
    >>  [11]]
    ```

- 垂直方向分成两份， 不等分
    ```
    arr1, arr2 = np.array_split(arr1, 2, axis=0)
    print(arr1)
    >> [[0 1 2 3]
    >>  [4 5 6 7]]
    print(arr2)
    >> [[ 8  9 10 11]]
    ```

### numpy 浅拷贝和深拷贝
- 浅拷贝
    ```
    arr1 = np.array([1, 2, 3])
    arr2 = arr1
    arr2[0] = 5
    print(arr1)
    >> [5 2 3]
    print(arr2)
    >> [5 2 3]
    ```

- 深拷贝
    ```
    arr1 = np.array([1, 2, 3])
    arr2 = arr1.copy()
    arr2[0] = 6
    print(arr1)
    >> [5 2 3]
    print(arr2)
    >> [6 2 3]
    ```
