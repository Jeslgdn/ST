
# sign_infomation={}
#
#
# def putInfoToDict(fileName):
#     fp=open(fileName)
#     sign_infomation=fp.readlines()

def putInToDict(fileName):
    retDict={}
    with open(fileName) as f:
        lines=f.read().splitlines()

    for line in lines:
        line = line.replace('(','').replace(')','').replace(';','').strip()

        parts = line.split(',')
        ciTime = parts[0].strip().replace("'",'')
        lessonid = int(parts[1].strip())

        uesrid   = int(parts[2].strip())

        toAdd = {'lessonid':lessonid,'checktime':ciTime}
        if uesrid not in retDict:
            retDict[uesrid]=[]
            retDict[uesrid].append(toAdd)

    retDict

ret= putInToDict('01.txt')

import pprint

pprint.pprint(ret)