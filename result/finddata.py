import os
import re
path='./tmp.md'
result=[]
model='test_acc'
if model == 'dev_acc':
	for line in open(path):
		line=line.strip()
		flag=line.find('dev_acc:')
		if flag >0:
			result.append(float(line[flag+10:flag+15]))
	print(result[7:27])
if model == 'test_acc':
	for line in open(path):
		line=line.strip()
		flag=line.find('est_acc:')
		if flag >0:
			result.append(float(line[flag+10:flag+15]))
	print(result[20:27])
if model == 'loss':
	for line in open(path):
		line=line.strip()
		flag=line.find('al loss:')
		if flag >0:
			result.append(float(line[flag+10:flag+15]))
	print(result[7:27])
if model == 'lstm':
	for line in open(path):
		line=line.strip()
		flag=line.find('est_acc:')
		if flag >0:
			result.append(round(float(line[flag+10:flag+14])-0.02,2))
	print(result[0:7])
