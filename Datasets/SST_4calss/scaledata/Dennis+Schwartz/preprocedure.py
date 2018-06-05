import os
import random
# import
classpath = './label.4class.Dennis+Schwartz' 
datapath = './subj.Dennis+Schwartz'
outpath = './rating'
classlist=[]
datalist=[]
outlist=[]
for line in open(classpath):
    line=line.strip()
    classlist.append(line)
for line in open(datapath):
    line=line.strip()
    datalist.append(line)
for rating,data in zip(classlist,datalist):
    data='rating:'+rating+' '+data+'\n'
    outlist.append(data)
    # print(data)
random.shuffle(outlist)

f = open('./train.res',"w+")  
f.writelines(outlist[0:800])

f = open('./dev.res',"w+")  
f.writelines(outlist[600:800])

f = open('./test.res',"w+")  
f.writelines(outlist[800:1000])

# print(outlist[999])



# print(classlist)