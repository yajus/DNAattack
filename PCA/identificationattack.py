import numpy as np
def Archimedes(a,b,number,index):
    point = 99999
    for i in range(len(b)):
        # print("a shape")
        # print(a.shape)
        # print("b[i]  shape")
        # print(b[i].shape)
        result=np.linalg.norm(a-b[i])
        #print(result)
        if (result<point):
            num=number[i]
            point=result
    # print("num:")
    # print(num)
    # print("index")
    # print(index)
    if(num==int(index)):
        # print(True)
        return True
    else:
        return False
