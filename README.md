#1 Prerequisites
* 1.Linux , windows or mac os
* 2.Python 3
* 3.Tensorflow with CPU only or NVIDIA GPU + CUDA CuDNN

#2 Easy Installation
* 1.Copy this file into your computer
* 2.Install python3 & pip3 & numpy & tflearn
* 3.Install tensorflow with cpu only  --sudo pip3 install tensorflow

#3 Get word2vec
* you can download Pre-trained word2vec model in this url and then copy it into './WordVector'
* https://github.com/3Top/word2vec-api
* better to download word2vec with 300 dimensions

#4 Make Dataset
* Movie Review Data: http://www.cs.cornell.edu/people/pabo/movie-review-data/
* you can download other Dataset as SST,Subj or even make your own Dataset
* make sure your same type txt in same file
* using makedataset.py to build your own Dataset(it may produce dataset['train.res','dev.res','test.res']
* change "--dataset" into your datasets' path


#5 Test and run the program
# Fast test 
* you can easily test this program in this way 

********** HS_LSTM***********
cd 'AAAI18-code/HS_LSTM'
python3 main.py  --maxlenth 10 --epoch 10 --batchsize 1 --lr 0.001 --dataset '../Datasets/Fasttest'

********** ID_LSTM ***********
cd 'AAAI18-code/ID_LSTM' 
python3 main.py  --maxlenth 10 --epoch 10 --batchsize 1 --lr 0.001 --dataset '../Datasets/Fasttest'


# Run Dateset:MR
* it may cost more than one day without GPU

********** HS_LSTM***********
cd 'AAAI18-code/HS_LSTM'
python3 main.py --maxlenth 30 --epoch 10 --batchsize 10 --lr 0.0005

********** ID_LSTM ***********
cd 'AAAI18-code/ID_LSTM'
python3 main.py --maxlenth 30 --epoch 10 --batchsize 10 --lr 0.0005

#6 Make some changes  from the original program (https://github.com/keavil/AAAI18-code)
* turn this program into python3 from python2
* debug some errors
* refactor 'datamanager.py' to adapt Datasets

README @Hypo Updata 2018-06-05