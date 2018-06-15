# Prerequisites
* 1.Linux , windows or mac os
* 2.Python 3
* 3.Tensorflow with CPU only or NVIDIA GPU + CUDA CuDNN

# Easy Installation
* 1.Copy this file into your computer
* 2.Install python3 & pip3 & numpy & tflearn
* 3.Install tensorflow with cpu only
```shell
sudo pip3 install tensorflow
```
# Get word2vec
* you can download Pre-trained word2vec model in this url and then copy it into './WordVector'
* https://github.com/3Top/word2vec-api
* better to download word2vec with 300 dimensions

# Make Dataset
* Movie Review Data: http://www.cs.cornell.edu/people/pabo/movie-review-data/
* you can download other Dataset as SST,Subj or even make your own Dataset, but make sure your same type txt in same file
* using makedataset.py to build your own Dataset(it may produce dataset['train.res','dev.res','test.res']
* change "--dataset" into your datasets' path

# Test and run the program
* Fast test , you can easily test this program in this way

HS_LSTM
```shell
cd 'AAAI18-code/HS_LSTM'
python3 main.py  --maxlenth 10 --epoch 10 --batchsize 1 --lr 0.001 --dataset '../Datasets/Fasttest'
```
ID_LSTM
```shell
cd 'AAAI18-code/ID_LSTM' 
python3 main.py  --maxlenth 10 --epoch 10 --batchsize 1 --lr 0.001 --dataset '../Datasets/Fasttest'
```

* Run Dateset:MR, it may cost more than one day without GPU

HS_LSTM
```shell
cd 'AAAI18-code/HS_LSTM'
python3 main.py --maxlenth 30 --epoch 10 --batchsize 10 --lr 0.0005
```
ID_LSTM
```shell
cd 'AAAI18-code/ID_LSTM'
python3 main.py --maxlenth 30 --epoch 10 --batchsize 10 --lr 0.0005
```

# Some changes from the original program 
* https://github.com/keavil/AAAI18-code
* turn this program into python3 from python2
* debug some errors
* refactor 'datamanager.py' to adapt Datasets

README @Hypo Update 2018-06-06

# Original README

*Learning Structured Representation for Text Classification via Reinforcement Learning
Tianyang Zhang*, Minlie Huang, Li Zhao

Representation learning is a fundamental problem in natural language processing. This paper studies how to learn a structured representation for text classification. Unlike most existing representation models that either use no structure or rely on pre-specified structures, we propose a reinforcement learning (RL) method to learn sentence representation by discovering optimized structures automatically. We demonstrate two attempts to build structured representation: Information Distilled LSTM (ID-LSTM) and Hierarchically Structured LSTM (HS-LSTM). ID-LSTM selects only important, task-relevant words, and HS-LSTM discovers phrase structures in a sentence. Structure discovery in the two representation models is formulated as a sequential decision problem: current decision of structure discovery affects following decisions, which can be addressed by policy gradient RL. Results show that our method can learn task-friendly representations by identifying important words or task-relevant structures without explicit structure annotations, and thus yields competitive performance.

@inproceedings{zhang2018learning,

  title={Learning Structured Representation for Text Classification via Reinforcement Learning},
  
  author={Zhang, Tianyang and Huang, Minlie and Zhao, Li},
  
  booktitle={AAAI},
  
  year={2018}
  
}
