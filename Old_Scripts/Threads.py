import threading 
import random

def NegSum(vec):
    negSum=vec[0]
    for i in range (1, len(vec)):
        if vec[i]<0:
            negSum = negSum + vec[i]
    print(negSum)


def PosSum(vec):
    posSum=vec[0]
    for i in range (1, len(vec)):
        if vec[i]>0:
            posSum = posSum + vec[i]
    print(posSum)


vec=[]
for i in range(0,40):
    vec.append(random.randint(-100,100))

t1= threading.Thread(target=NegSum(vec))
t2= threading.Thread(target=PosSum(vec))

t1.start()
t2.start()
t1.join()
t2.join()
