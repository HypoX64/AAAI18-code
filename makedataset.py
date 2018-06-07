import sys, os
import random

#traversal all file in rootdir and return
def Traversal(rootDir):
    file_list=[]
    for root,dirs,files in os.walk(rootDir): #root:currentfile path , dirs:subfile path , files: filepath
        for file in files:
            file_list.append(os.path.join(root,file)) #combina the path
        for dir in dirs:
            Traversal(dir) #recursion
    return file_list

#turn files into datasets return <class:list>
def getdataset(pathlist,subfile,mode,train,dev):#pathlist:file_path_list,subfile:subfile_name_list,train,dev:choose the train,dev,test part of all files
    datalist=[]
    
    for i,path in enumerate(pathlist,1):
        node=''
        for x,file in enumerate(subfile,0):#get the rating of this file
            if file in path:
                rating=x
        if mode == 0:
            for line in open(path):#add rating into files
                # line='rating:'+str(rating)+' '+line.strip()+'\n'
                # datalist.append(line)
                node += line.strip()+' '
            node = 'rating:'+str(rating)+' '+node+'\n'
            datalist.append(node)
        else:
            for line in open(path):#add rating into files
                line='rating:'+str(rating)+' '+line.strip()+'\n'
                datalist.append(line)
    lens=len(datalist)
    random.shuffle(datalist)
    # datalist[len(datalist)-1].strip()
    return lens,datalist[0:int(train*lens)],datalist[int((train-dev)*lens):int(train*lens)],datalist[int(train*lens):lens]

def main():
    filedir = input("filedir:").strip()
    filedir=str(filedir.replace("'",""))
    mode = int(input("choose the mode 0:article 1:sentence :").strip())
    
    filepathlist = Traversal(filedir)
    random.shuffle(filepathlist)
    # filepathlist=filepathlist[0:maxpiece]
    subfile = os.listdir(filedir)

    lens,trainlist,devlist,testlist = getdataset(filepathlist,subfile,mode,0.8,0.2)
    print('Find:',lens)

    maxpiece = int(input("please input the quantity you want:").strip())
    trainlist = trainlist[0:int(maxpiece*0.8)]
    devlist = devlist[0:int(maxpiece*0.2)]
    testlist = testlist[0:int(maxpiece*0.2)]

    print('train:%d dev:%d test:%d' % (len(trainlist),len(devlist),len(testlist)))
    f = open('./train.res',"w+")  
    f.writelines(trainlist)

    f = open('./dev.res',"w+")  
    f.writelines(devlist)

    f = open('./test.res',"w+")  
    f.writelines(testlist)
    print('Finished!')
if __name__ == '__main__':
    main()
