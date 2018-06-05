import numpy as np  
import matplotlib.pyplot as plt  

epoch=np.arange(0,20,1)
LSTMonly_acc = np.array([0.88, 0.89, 0.86, 0.86, 0.86, 0.87, 0.87])

train_acc=np.array([0.893, 0.896, 0.896, 0.906, 0.905, 0.905, 0.902, 0.9, 0.902, 0.901, 0.906, 0.902, 0.908, 0.91, 0.907, 0.909, 0.908, 0.904, 0.904, 0.907])
test_acc=np.array([0.902, 0.912, 0.915, 0.914, 0.916, 0.918, 0.921, 0.92, 0.924, 0.922, 0.914, 0.92, 0.917, 0.912, 0.919, 0.917, 0.916, 0.916, 0.913, 0.915])
loss=np.array([0.29, 0.35, 0.3, 0.29, 2.15, 0.25, 0.29, 0.26, 0.24, 0.3, 0.28, 0.23, 0.22, 0.23, 0.22, 0.24, 0.2, 0.19, 0.22, 0.2])


fig = plt.figure()
y_acc = fig.add_subplot(111)

l1, = y_acc.plot(epoch,train_acc,color = 'black')
l2, = y_acc.plot(epoch,test_acc)
l3, = y_acc.plot(epoch[0:7],LSTMonly_acc)
plt.xlim((0, 20))
plt.ylim((0.8, 1))
plt.xlabel('Epoch',fontsize='large',fontweight='bold')
plt.ylabel('acc',fontsize='large',fontweight='bold')

y_loss = y_acc.twinx()
l4, = y_loss.plot(epoch,loss,color='red') 
plt.ylabel('loss',fontsize='large',fontweight='bold')

plt.title('Subj_HS_LSTM',fontsize='large',fontweight='bold')
plt.legend([l1,l2,l3,l4], ['RLtrain_acc', 'RLtest_acc','LSTMonly_acc','RLloss'], loc = 'upper right')   
plt.show()