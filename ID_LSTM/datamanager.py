import sys, os
import collections
import numpy as np
import random
#Refactoring @Hypo 2018-05-23
class DataManager(object):
    def __init__(self, dataset):
        #Read the data from dir "dataset" which including 'train.res', 'dev.res', 'test.res'
        self.origin = {}
        for fname in ['train', 'dev', 'test']:
            linelist=[]
            f = open('%s/%s.res' % (dataset, fname))
            for line in f.readlines():
                line=line.strip()
                linelist.append(line)
            f.close()
            self.origin[fname] = linelist

    def getword(self):
        '''
        Get the words that appear in the data.
        Sorted by the times it appears.
        {'ok': 1, 'how': 2, ...}
        '''
        word_list=[]
        for fname in ['train', 'dev', 'test']:
            for line in self.origin[fname]:
                line=line[9:]
                word_list += line.split(' ')

        worddict=str(collections.Counter(word_list))
        worddict=worddict.strip('Counter').strip('(').strip(')')
        worddict=eval(worddict)
        for i,(word,num) in enumerate(worddict.items(),1):
            worddict[word]=i
        self.wordlist=worddict
        # print(self.wordlist)
        print('find word:',len(self.wordlist))
        return self.wordlist

    def getdata(self, grained, maxlenth):
        '''
        Get all the data, divided into (train,dev,test).
        For every line, words:word's appear times, solution:rating, lenth:length of the line
        {'words':[1,3,5,...], 'solution': [0,1,0,0,0...], 'lenth': lens}
        '''
        self.data = {}
        self.getword()
        for fname in ['train', 'dev', 'test']:
            self.data[fname] = []
            wordlist_line=[]
            for line in self.origin[fname]:
                words = np.zeros(maxlenth,int)
                solution = np.zeros(grained, dtype=np.float32)
                solution[int(line[7])]=1.0
                line=line[9:]
                wordlist_line=line.split(' ')
                wordlist_line=wordlist_line[0:maxlenth]
                for i,word in enumerate(wordlist_line,0):
                    words[i]=self.wordlist[word]
                    # print(i)
                    lens=i+1
                now = {'words': np.array(words), \
                    'solution': solution,\
                    'lenth': lens}
                self.data[fname].append(now)
        # print(self.data['train'])
        return self.data['train'], self.data['dev'], self.data['test']
    
    def get_wordvector(self, name):
        '''
        Find words in wordvector, and get the vector
        '''
        print('Begin find words in wordvector......')
        print('it may cost 60 s ,please wait......')
        n = 400000# depend on wordvector
        dim = 300
        fr = open(name)
        self.wv = {}
        for i in range(n - 1):
            vec = fr.readline().split()
            word = vec[0].lower()
            vec = list(map(float, vec[1:]))
            if word in self.wordlist:
                self.wv[self.wordlist[word]] = vec
        self.wordvector = []
        losscnt = 0
        for i in range(len(self.wordlist) + 1):
            if i in self.wv:
                self.wordvector.append(self.wv[i])
            else:
                losscnt += 1
                self.wordvector.append(np.random.uniform(-0.1,0.1,[dim]))
        self.wordvector = np.array(self.wordvector, dtype=np.float32)
        print(losscnt, "words not find in wordvector")
        print(len(self.wordvector), "words in total")
        return self.wordvector
# test
# dataManager = DataManager('../Datasets/MR')
# dataManager.getdata(2,3)
# dataManager.get_wordvector('../WordVector/vector.300dim')
