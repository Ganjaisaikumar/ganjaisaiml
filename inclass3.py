import matplotlib.pyplot as plt
import numpy as np

main_arr = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
labels_data = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
myexplode_data = [0.2, 0, 0, 0,0,0]
plt.pie(main_arr,labels=labels_data, explode = myexplode_data,autopct='%1.1f%%')
plt.show()
