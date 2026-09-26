from sklearn.neighbors import KNeighborsClassifier

X = [
   [1, 50],
    [2, 60],
    [3, 65],
    [5, 80],
    [6, 85],
    [7, 90],
    [8, 95]
]
y = [0, 0, 0, 1, 1, 1, 1]

modle =KNeighborsClassifier(n_neighbors=3)

modle.fit(X,y)

newstudent = [[7,75]]

result = modle.predict(newstudent)
print(result[0])