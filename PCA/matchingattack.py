import numpy as np
mindistance=9999999
def Archimedes(a,b,number1,number2):
   # point = 99999
    length1=len(a)
    length2=len(b)
    #apoint = np.array([])
    #bpoint = np.array([])
    #resultpoint=np.array([])

    #globals(mindistance)
    outputpoint=np.array([])
    #distance=0
    if(length1>=length2):
        length=length1
    else:
        length=length2
    resultpoint=np.array(number1)
    apoint=np.array(number2)
    # for i in range(length):
    #     apoint=np.append(apoint,i)
    #     bpoint=np.append(apoint,0)
    #     resultpoint=np.append(resultpoint,i)
    surpluse=0
    #mdp(surpluse)
    def mdp(surplus,):
        global mindistance
        global outputpoint
        if(surplus==length):
            distance=0
            for i in range(len(apoint)):
                distance=+np.linalg.norm(b[apoint[i]]-a[resultpoint[i]])
            if(distance<mindistance):
                mindistance=distance
                outputpoint=np.array(resultpoint)
            return mindistance,outputpoint

        else:
            for i in range(length-surplus):
                deliver=resultpoint[surplus]
                resultpoint[surplus]=resultpoint[surplus+i]
                resultpoint[surplus+i]=deliver
                mdp(surplus+1)
                #surplus
                deliver = resultpoint[surplus]
                resultpoint[surplus] = resultpoint[surplus+i]
                resultpoint[surplus+i] = deliver
                return mindistance,outputpoint
    return mdp(surpluse)

