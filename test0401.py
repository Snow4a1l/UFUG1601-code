import numpy as np

# 模拟两个 2D 数组（2行3列）
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

# 默认 axis=0 (纵向堆叠 -> 变成 4x3)
res_v = np.concatenate((arr1, arr2)) 

# 显式 axis=1 (横向拼接 -> 变成 2x6)
res_h = np.concatenate((arr1, arr2), axis=1)

print(res_h) # (4, 3)
print(res_v) # (2, 6)