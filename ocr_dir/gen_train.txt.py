import os

path = './data/Img'

data_list = []
list_ = os.listdir(path)
for i in range(len(list_)):
    for j in os.listdir(path + '/' + list_[i]):
        data_list.append(path + '/' + list_[i]+ '/'+ j + ' ' + '{}'.format(i))

with open('./data/train.txt','a',encoding='utf-8') as fw:
    for data in data_list:
        fw.writelines(data)
        fw.write('\n')