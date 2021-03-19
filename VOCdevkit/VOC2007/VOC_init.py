import os
import random

# train + validation = 1
train_percent = 0.8 # 只有這個參數有效
validation = 0.2

xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets\Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml) # 總樣本數 ex 100
list = range(num)    # 總樣本數數列 ex [0 ... 99]
print("num of sample:", num)

num_of_train = int(num * train_percent)
train = random.sample(list,num_of_train)

ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('ImageSets/Main/test.txt', 'w')
ftrain = open('ImageSets/Main/train.txt', 'w')
fval = open('ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in train:
        ftrain.write(name)
    else:
        fval.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()