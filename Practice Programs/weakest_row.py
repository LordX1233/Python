import operator
mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
k = 3

z = []
dicts = {
}
keys2 =[]

for i in range (len(mat)):
    m = mat[i].count(1)
    z.append(m)
for i in range (len(mat)):
    dicts[i] = z[i]
sorted_dict = dict(sorted(dicts.items(), key=operator.itemgetter(1)))
keys = list(sorted_dict.keys())
for i in range(k):
    keys2.append(keys[i])