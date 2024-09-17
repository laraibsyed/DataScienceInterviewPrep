import numpy as np

def euclidean(x,y):
    x = np.array(x)
    y = np.array(y)

    distance = np.sqrt(np.sum((x - y)**2))
    return distance

x = [1, 2, 3]
y = [4, 5, 6]

result = euclidean(x, y)
print(result)