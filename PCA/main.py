import pandas as pd
import dataprocess as dp
import numpy as np
import identificationattack as idf
import matchingattack as mta
data = pd.read_csv("./data.csv")


#indentification attack 计算过程
length = len(data.T)
#print(length)
#print(data.shape)
clname=data.columns

#时间种类
list_=np.array([])
for i in clname:
    i=i[11]
    list_=np.append(list_,i)
list_=np.unique(list_)
#list_=np.delete(list_,'0')
print(list_)

total=0
resultnum=0
#print(clname[0][-1])
for j in range(len(clname)):
    a=np.array(data)[:,j]
    a = a.reshape(1, -1)
    # print("a.shape before")
    # print(a.shape)
    a = dp.PCA.transform(a)
    # print("a.shape after")
    # print(a.shape)
    #print(a)
    for i in range (len(list_)):
        if(i!=int(clname[j][11])):
            name=list_[i]
            line,number=dp.process(name)
            if(len(clname[j])>13):
                #print(clname[j])
                #print(idf.Archimedes(a,line,number,int(0)))
                if (idf.Archimedes(a, line, number, int(clname[j][13:]))):
                        resultnum += 1
            else:
                #print(0)
                #print(clname[j])
                # print(idf.Archimedes(a,line,number,int(0)))
                if(idf.Archimedes(a,line,number,int(0))):
                    resultnum+=1
            total+=1
print(total)
print("identificationattack结果是：")
print(resultnum/total)

#matchingattack过程
fenzi = 0
fenmu = 0
for i in range(1,len(list_)+1):
    for j in range(i+1,len(list_)+1):
        # print("i")
        # print(i)
        a,number1=dp.process(i)
        b,number2=dp.process(j)
        if(len(number2)>len(number1)):
            for ll in range(len(number2)-len(number1)):
                arr = np.empty(( len(b[0])))
                arr=arr.reshape(1,-1)
                # for l in range(len(number1) - len(number2)):
                for k in range(len(b[0])):
                    arr[0][k] = -99999
                a = np.append(a, arr, axis=0)
                number1 = np.append(number1,number2[-(ll+1)])
        elif(len(number2)<len(number1)):
            for ll in range(len(number1)-len(number2)):
                arr = np.empty(( len(a[0])))
                arr=arr.reshape(1,-1)
                # for l in range(len(number1) - len(number2)):
                for k in range(len(a[0])):
                    arr[0][k] = -99999
                b = np.append(b, arr, axis=0)
                number2 = np.append(number2,number1[-(ll+1)])

        x1,x2=mta.Archimedes(a,b,number1,number2)
        for k in range(max(len(number2),len(number1))):
            if(number2[k]==number1[k]):
                fenzi+=1
                fenmu+=1
            else:
                fenmu+=1
print("分子")
print(fenzi)
print("分母")
print(fenmu)
print("matchingattack结果是：")

print(fenzi/fenmu)

