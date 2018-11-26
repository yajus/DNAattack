import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
    #fit
data = pd.read_csv("./data.csv")
datatrain = data.T
PCA = PCA(n_components=120)
PCA.fit_transform(datatrain)
print(data.columns)
def process(dnum):
    #选出同一时间的所有fit后数据
    x=np.array(data["timepoint: "+str(dnum)])
    x=x.reshape(1,-1)
    #print(x.shape)
    i=1
    number=np.array([0])
    while(True):
           try:
               deliver=np.array(data["timepoint: "+str(dnum)+'.'+str(i)])
               number=np.append(number,i)
               #print("i:")
               #print(i)
               #print("delivershape")
               #print(deliver.shape)
               deliver=deliver.reshape(1,-1)

               x = np.append(x, deliver,axis=0)
               i += 1
           except:
                break

    #print('dnum:')
    #print(dnum)
    result=PCA.transform(x)
    #print(result)

    #输出覆盖率
    rate=PCA.explained_variance_ratio_
    sum=0
    for i in rate:
        sum+=i
    # print("sum:")
    # print(sum)
    #print("number")
    #print(number)
    return result,number