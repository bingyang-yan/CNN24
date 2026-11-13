import sys
import torch
from yby import *
from Net import *

root_train = Path(r"E:\Data\Paper_1\Data_v3\Y_split\20230801_201145\train")

net = [Y_cnn_relu, Y_cnn_leakyrelu, Y_cnn_sigmoid_leakyrelu]
batch_size = [128, 512]
optimizer = [torch.optim.SGD, torch.optim.Adam]
optim_info = ['SGD', 'Adam']

step = 0
for i,v in enumerate(optimizer):
    for n in net:
        for b in batch_size:
            step+=1
            dataset = Y_dataset(root_train, the_glob='*')
            dataloader = Y_dataloader(dataset, batch_size=b, shuffle=True, drop_last=True)
            info = 'batch_{}_optim_{}'.format(b, optim_info[i])
            res = Y_train(dataloader, net=n, optimizer=v, info=info)
            print('Process {}/{}'.format(step, 12))
            
    


