import numpy as np
from time import *
import tracemalloc

def penalty_mismatch(b1, b2):
    Str= 'ACGT'
    index_1= Str.find(b1)
    index_2= Str.find(b2)
    penalty_metrix = [[0, 110, 48, 94],
                      [110, 0, 118, 48],
                      [48, 118, 0, 110],
                      [94, 48, 110, 0]]
    return penalty_metrix[index_1][index_2]

gap=30
P= []
def space_efficient_alignment(X,Y):

    B = np.zeros((len(X)+1, 2))
    for i in range(1,len(X)+1):
        B[i][0]=i*gap
    for j in range(1,len(Y)+1):
        B[0][1]=j*gap
        for i in range(1,len(X)+1):
            B[i][1]=min(B[i-1][0] + penalty_mismatch(X[i-1], Y[j-1]),
                        B[i-1][1]+ gap,
                       B[i][0] + gap)
        for i in range(0,len(X)+1):
            B[i][0] = B[i][1]
    return (B.T)[1]

def backward_efficient_alignment(X,Y):

    B = np.zeros((len(X)+1, 2))
    for i in range(1,len(X)+1):
        B[len(X)-i][1]=i*gap
    for j in range(len(Y)-1,-1,-1):
        B[len(X)][0]=(len(Y)-j)*gap
        for i in range(len(X)-1, -1, -1):
            B[i][0]=min(B[i+1][1] + penalty_mismatch(X[i], Y[j]),
                        B[i+1][0]+ gap,
                       B[i][1] + gap)
        # if j==1:
        #     for i in range(0,len(X)+1):
        #         B[i][1] = B[i][0]
        for i in range(0,len(X)+1):
            B[i][1] = B[i][0]
    return (B.T)[0]

# the pair when n<=2 &m<=2
def get_path(OPT,s1,s2,x_ori, y_ori):
    s1_length = len(s1)
    s2_length = len(s2)
    #save path
    i= s1_length
    j= s2_length
    path=[[0 for col in range(s2_length+1)] for row in range(s1_length+1)]
    path[i][j]=1
    path[0][0]=1
    while i!=0 or j!=0:
        if  OPT[i][j]==OPT[i-1][j]+gap:
            path[i-1][j]=1
            i=i-1
        elif  OPT[i][j]==OPT[i][j-1]+gap:
            path[i][j-1] = 1
            j=j-1
        else:
            path[i-1][j - 1] = 1
            i=i-1
            j=j-1
    # path=np.array(path)
    for x_index,x in enumerate(path):
        for y_index in range(len(path[0])):
            if x[y_index] == 1:
                P.append([x_index+x_ori , y_index+y_ori])

    return P

def Alignment(X,Y, x_index, y_index):
    B = np.zeros((len(X)+1, len(Y)+1))
    for i in range(1,len(X)+1):
        B[i][0]=i*gap
    for j in range(1,len(Y)+1):
        B[0][j]=j*gap
        for i in range(1,len(X)+1):
            B[i][j]=min(B[i-1][j-1] + penalty_mismatch(X[i-1], Y[j-1]),
                        B[i-1][j]+ gap,
                       B[i][j-1] + gap)
    get_path(B,X,Y,x_index,y_index)
    return 0

def Divide_and_Conquer_Alignment(X,Y,x_index,y_index):
    m = len(X)
    n = len(Y)
    if m<=2 or n<=2:
        Alignment(X, Y, x_index, y_index)
    else:
        f = np.array(space_efficient_alignment(X, Y[0:n//2]))
        g = np.array(backward_efficient_alignment(X, Y[n//2+1:n]))
        sum_list= f+g
        min_sum=sum_list[0]
        min_index=0
        for index,one in enumerate(sum_list):
            if one < min_sum:
                min_sum= one
                min_index=index
        P.append([min_index + x_index, n//2+ y_index])
        Divide_and_Conquer_Alignment(X[0:min_index], Y[0:n//2], x_index, y_index)
        Divide_and_Conquer_Alignment(X[min_index:m], Y[n//2:n], min_index+x_index, n//2+ y_index)
    return P


def get_two_string(P,s1,s2):
    s1_length = len(s1)
    s2_length = len(s2)

    path = [[0 for col in range(len(s2) + 1)] for row in range(len(s1) + 1)]
    for one in P:
        path[one[0]][one[1]] = 1
    # B = np.zeros((33, 33)
    for one in path:
        print(one)

    s1_final = ''
    s2_final = ''
    i = 0
    j = 0
    while i != s1_length and j != s1_length:
        if i != s1_length and path[i + 1][j] == 1:
            s1_final = s1_final + s1[i]
            s2_final = s2_final + '_'
            i = i + 1
        elif j != s2_length and path[i][j + 1] == 1:
            s1_final = s1_final + '_'
            s2_final = s2_final + s2[j]
            j = j + 1
        else:
            s1_final = s1_final + s1[i]
            s2_final = s2_final + s2[j]
            i = i + 1
            j = j + 1
    print(s1_final)
    print(s2_final)


def get_string_DC(P,s1,s2):
    index=0
    s1_final = ''
    s2_final = ''
    i = 0
    j = 0
    while index < len(P)-1:
        if P[index][0]<P[index+1][0] and P[index][1]==P[index+1][1] :
            s1_final = s1_final + s1[i]
            s2_final = s2_final + '_'
            i = i + 1
        elif P[index][0]==P[index+1][0] and P[index][1]<P[index+1][1] :
            s1_final = s1_final + '_'
            s2_final = s2_final + s2[j]
            j = j + 1
        elif P[index][0]==P[index+1][0] and P[index][1]==P[index+1][1] :
            pass
        else:
            s1_final = s1_final + s1[i]
            s2_final = s2_final + s2[j]
            i = i + 1
            j = j + 1
        index = index+1
    if len(s1_final) < 100:
        print(s1_final)
        print(s2_final)
        wf = [s1_final, s2_final]
    else:
        print(s1_final[0:50], s1_final[-50:])
        print(s2_final[0:50], s2_final[-50:])
        wf = [s1_final[0:50] + " " + s1_final[-50:], s2_final[0:50] + " " + s2_final[-50:]]
    return wf

with open("String_generator.txt", 'r') as fin:
    start = time()
    tracemalloc.start(25)
    s1 = fin.readline().strip()
    s2 = fin.readline().strip()
    P = Divide_and_Conquer_Alignment(s1, s2, 0, 0) # 17.53s

    # aa=space_efficient_alignment(s1,s2) # 8.44s
    # print(aa[-1])
    # get_two_string(P,s1,s2)
    P.sort(key = lambda x:(x[0],x[1]))

    wf = get_string_DC(P,s1,s2)
    size, peak = tracemalloc.get_traced_memory()
    end = time()
    run_time = end - start
    print(run_time)
    print(peak / 1024, "KiB")
    print("input size:", len(s1) + len(s2))

    wf.append(str(run_time))
    wf.append(str(peak))
    f = open("output_efficient.txt", 'wt')
    f.write('\n'.join(wf))
    f.close()