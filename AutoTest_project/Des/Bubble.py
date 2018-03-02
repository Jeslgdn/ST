


li = [56,54,3,674,674,864,34,15,51]

lis=[23,24,31,2,5,32,55]

def bubble(list):
    for i in range(len(list)-1,0,-1):
        for j in range(0,i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list


print(bubble(li))