#簡単
import numpy as np
import csv
from numpy.lib.function_base import delete 


class LocalStressMajorization:
    n = 4
    d = np.full((n, n), np.inf)
    w = np.zeros((n, n))

    def __init__(self):
        pass

    def stress(self, X):
        res = 0
        for i in range(n):
            for j in range(n):
                if( i != j ):
                    res += w[i][j]*(np.linalg.norm(X[i]-X[j])-d[i][j])**2
        return res

    #データ読み込み
    
    with open('assets\sample.csv') as f:
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
    
    def ready():
        for i in range(len(d)):
            for j in range(len(d)):
            if(i == j):
                d[i][j] = 0
        print("隣接行列")
        print(d)
        
    #最短経路計算
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][k]!= np.inf and d[k][j]!=np.inf:
                        d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        print("最短経路行列")
        print(d)

    #dijをwijに変換
        for i in range(n):
            for j in range(n):
                if(d[i][j] == np.inf):
                    f = 1
                if(i != j):
                    w[i][j] = 1 / (d[i][j] * d[i][j])

    print("wij")
    print(w)

    def run():

        Xt = np.full((n, 2), 0, dtype=np.float)
        for i in range(n):
            for j in range(2):
                Xt[i][j] = 19*np.random.rand()+1.0
        print("######")
        print(w)
        cnt = 0
        while True:

            for i in range(n):
                for a in range(2):
                    up = 0
                    down = np.sum(w)
                    for j in range(n):
                        if(i == j):
                            continue
                        #print(w[i][j])
                        #print(d[j][a])
                        #print(Xt[i][a]-Xt[j][a])
                        #print(np.linalg.norm(Xt[i]-Xt[j]))
                        if(np.linalg.norm(Xt[i]-Xt[j]) != 0):
                            up += w[i][j]*(Xt[j][a] + d[i][j]*(Xt[i][a]-Xt[j][a]) / np.linalg.norm(Xt[i]-Xt[j]) )
                        else:
                            up += w[i][j]*(Xt[j][a])
            
                    #print(up)
                    #print(down)
                    #print(up)
                    #print(down)
                    Xt[i][a] = up / down 
                    #print(Xt[i][a])
                    #print(up)
                    #print(down)
            print("#####")
            #print(Xt)
            print(stress(Xt))
            #if(cnt == 1):
            #    break


        print(cnt)



