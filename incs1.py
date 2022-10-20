import numpy as np
arr_np=np.random.randint(1,20,(1,15))
print(arr_np)
arr_np=np.reshape(arr_np,(3,5))
print(arr_np)
for i in arr_np:
    i[np.where(i==i.max())]=0
print(arr_np)
