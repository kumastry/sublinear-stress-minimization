import numpy as np
import csv 




def stress():
    return 0git

#データ読み込み
n = 100
d = np.full((100, 100), np.inf)
with open('assets\qiita.csv') as f:
    csvreader = csv.reader(f)
    flag = True
    for row in csvreader:
        if(flag):
            flag = False
            continue
        i = int(row[0])-1
        j = int(row[1])-1 
        c = int(row[2])
        if(i != j):
            if(c != 0):
                d[i][j] = c
                d[j][i] = c
        else:
            d[i][j] = 0


for i in range(len(d)):
    for j in range(len(d)):
        if(i == j):
            d[i][j] = 0
print(d)


#最短経路計算
for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][k]!= np.inf and d[k][j]!=np.inf:
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


#dijをwijに変換
w = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if(i != j):
            w[i][j] = 1 / (d[i][j] * d[i][j])

#deltaの作成
delta = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if(i != j):
            delta[i][j] = w[i][j] * d[i][j]


#重み付けラプラシアン行列
Lw = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if(i != j):
            Lw[i][j] = - w[i][j]
col_sum = np.sum(w, axis=1)
print(col_sum)
for i in range(n):
    Lw[i][i] = col_sum[i]
print(Lw)

#Lwは定数の行列で
#Lzは反復で再計算される．


