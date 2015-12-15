#coding: UTF-8

import random

def loadDataSet(filename):
    dataMat = []
    with open(filename) as fp:
        for line in fp.readlines():
            curLine = line.strip().split()
            # floatLine = list(map(float, curLine))
            dataMat.append(curLine)
    return dataMat

def random_sampling(dataSet, num):
    try:
        samples = random.sample(dataSet, num)
        return samples
    except:
        print('sample larger than population')

def systematic_sampling(dataMat, num):
    k = int(len(dataMat)/num)
    samples = [random.sample(dataMat[i*k:(i+1)*k], 1) for i in range(num)]
    return samples

def repetition_random_sampling(dataMat, num):
    samples = [random_sampling(dataMat, 1) for i in range(num)]
    return samples

def main():
    dataMat = loadDataSet('./data.txt')
    # print(random_sampling(dataSet, 3))
    # random_sampling(dataSet, 7)
    # print(systematic_sampling(dataMat, 2))
    print(repetition_random_sampling(dataMat, 3))
if __name__ == '__main__':
    main()