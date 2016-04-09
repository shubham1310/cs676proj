# import csv
import numpy as np

f = open('rank.txt', 'r')
# reader = csv.reader(f, delimiter = ',')
Rank = f.read()
Rank = eval(Rank)
# trueRank = list(reader)
# print a
trueRank = np.asarray(a)
# print (trueRank)
f = open('nlabel.txt', 'r')
labels = [line.strip() for line in f]

n_att = 10
n = len(labels)
### Rank to be loaded from rank.txt
Rank = np.asarray(Rank)
print (Rank.shape())
for i in range(n_att):
    a = trueRank[:,i]
    y_p = Rank[:,i]
    # print (y_p)
    y_t = np.zeros(n)
    for j in range(n):
        y_t[j] = a[int(labels[j])-1]
    # print (y_t)
    tot = 0
    acc = 0
    for m in range(n):
        [a1,p1] = [y_t[m],y_p[m]]
        # a1,p1 = float(a1),float(p1)
        for k in range(m+1,n):
            tot += 1
            [a2,p2] = [y_t[k],y_p[k]]
            # a2,p2 = float(a2),float(p2)
            if a2-a1 != 0:
                if((a2-a1)*(p2-p1) > 0):
                    acc += 1
            elif abs(p2-p1)<1:
                acc += 1
    print ('Attribute:',i,':')
    print (acc, 'out of', tot, 'correct ranking pairs.')
    print ('Percentage Accuracy: ', acc*100./tot)
