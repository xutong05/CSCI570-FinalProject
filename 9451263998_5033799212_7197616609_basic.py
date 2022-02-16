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

def alignment(s1,s2):
    s1_length = len(s1)
    s2_length = len(s2)
    OPT = [[0 for col in range(s2_length + 1)] for row in range(s1_length + 1)]
    for i in range(s1_length+1):
        OPT[i][0]=gap*i

    for j in range(s2_length+1):
        OPT[0][j]=gap*j

    for i in range(1,s1_length+1):
        for j in range(1,s2_length+1):
            if s1[i-1]==s2[j-1]:
                min_value=min(OPT[i-1][j-1],
                              OPT[i-1][j]+ gap,
                              OPT[i][j-1]+gap)
                OPT[i][j]=min_value
            else:
                min_value= min(OPT[i - 1][j - 1]+penalty_mismatch(s1[i-1], s2[j-1]),
                                OPT[i - 1][j] + gap,
                                OPT[i][j - 1] + gap)
                OPT[i][j]=min_value
    return OPT

def get_path(OPT,s1,s2):
    s1_length = len(s1)
    s2_length = len(s2)
    #储存路径
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
    #读取路径
    s1_final=''
    s2_final=''
    i=0
    j=0
    while i!=s1_length and j!=s1_length:
        if i!=s1_length and path[i+1][j]==1:
            s1_final=s1_final+s1[i]
            s2_final = s2_final + '-'
            i=i+1
        elif j!=s2_length and path[i][j+1]==1:
            s1_final = s1_final + '-'
            s2_final = s2_final + s2[j]
            j=j+1
        else:
            s1_final = s1_final + s1[i ]
            s2_final = s2_final + s2[j]
            i=i+1
            j=j+1
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

    OPT = alignment(s1, s2)
    print(OPT[len(s1)][len(s2)])
    wf= get_path(OPT, s1, s2)
    end = time()
    run_time = end - start
    size, peak = tracemalloc.get_traced_memory()

    print(run_time)
    print(peak / 1024, "KiB")
    print("input size:", len(s1) + len(s2))

    wf.append(str(run_time))
    wf.append(str(peak))
    f = open("output_basic.txt", 'wt')
    f.write('\n'.join(wf))
    f.close()