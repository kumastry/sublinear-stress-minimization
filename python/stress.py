import numpy as np
import csv

from numpy.lib.function_base import delete 



n = 100
def stress(X):
    res = 0
    for i in range(n):
        for j in range(n):
            if( i != j ):
                res += w[i][j]*(np.linalg.norm(X[i]-X[j])-d[i][j])**2
    return res

#データ読み込み

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

Xt = np.full((n, 2), 0)
for i in range(n):
    for j in range(2):
        Xt[i][j] = 9*np.random.rand()+1
Lz = np.zeros((n, n))
print("####################")
print(Xt)
for i in range(n):
    for j in range(n):
        if(i != j ):
            if( np.linalg.norm(Xt[i]-Xt[j]) != 0):
                Lz[i][j] = -delta[i][j]  / np.linalg.norm(Xt[i]-Xt[j])
            else:
                Lz[i][j] = 0

cnt = 0
while True:
    Xt1 = np.linalg.solve(Lw, np.dot(Lz, Xt))
    print("!!!!!")
    print(Xt1.shape)
    #print(Xt1)
    print(np.dot(Lz, Xt))
    print("stress")
    print(stress(Xt))
    print(stress(Xt1))
    if(( stress(Xt)-stress(Xt1) ) / stress(Xt) < 0.001):
        print("stress")
        print(stress(Xt))
        print(stress(Xt1))
        break
    Xt = Xt1

    for i in range(n):
        for j in range(n):
            if( i != j):
                Lz[i][j] = -delta[i][j]
    print(cnt)
    cnt += 1
    #if(cnt == 1):
    #    break
print("finish")
print(Xt)
print(Xt1)

print(stress(Xt))
print(stress(Xt1))
print(cnt)



