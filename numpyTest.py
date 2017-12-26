#encoding=utf-8
import numpy as np
def main():
    '''y = np.array(0.5)
    print(y)
    lst=[[1,3,5],[2,4,6]]
    t=np.array([[[[1], [2]], [[3], [4]], [[5], [6]]], [[[7], [8]],[[9],[10]], [[11], [12]]],
              [[[13], [14]], [[15], [16]], [[17], [17]]]])
    v = np.array([1, 2, 3, 4])
    x=v.reshape(4,1)
    print(v.shape)
    print(x)
    print(t.shape)
    print (type(lst))
    np_list=np.array(lst)
    print (type(np_list))
    np_list=np.array(lst,dtype=np.float)
    #bool,int,int8,int16,int32,int64,int128,uint8,uint16,uint32,uint64,uint128,float,folat64
    print(np_list[1][1])
    print(np_list.shape)
    print(np_list.ndim)
    print(np_list.dtype)
    print(np_list.itemsize)
    print(np_list.size)
    print(np.zeros([3,4]))
    print(np.ones([3, 4]))
    print("Rand")
    print(np.random.rand(2,4))
    print("Randint")
    print(np.random.randint(2, 4,10))
    print ("Randn")
    print(np.random.randn(2,4))
    print ("Choice")
    print(np.random.choice([10,20,2,4,30]))
    print ("distribute")
    #print(np.random.beta(1,10,100))
    print(np.arange(1,11).reshape([2,-1]))
    print(np.exp(lst))

  from numpy.linalg import *
    print(np.eye(3))
    lst=np.array([[1.,2.,],[3.,4.]])
    print( lst.shape)
    n_records, n_inputs = lst.shape
    # Number of hidden units

    # 隐藏层节点个数
    n_hidden = 2
    print(2 **-0.5)
    weights_input_to_hidden = np.random.normal(0, n_inputs ** -0.5, size=(n_inputs, n_hidden))
    print('np.random.seed 2==')
    np.random.seed(2)
    num = 0
    while (num < 5):
        if num>=3:
            np.random.seed(5)
            print(np.random.random())
        else:
            np.random.seed(10)
            print(np.random.random())
        num += 1
    print(np.random.random())
    np.random.seed(5)
    print(np.random.random())
    np.random.seed(10)
    print(np.random.random())
    x = [1, 2, 3]
    y = [4, 5, 6]
    for m, n in zip(x, y):
        print(m)
        print(n)
    arr = [False,False]
    maen=np.mean(arr)
    print(maen)'''
    w1 = np.array([[1, 2,6], [3, 4,4],[3,4.5,90]])
    w2 = np.array([[5, 6], [7, 8]])

    # flatten
    w1_flat = np.reshape(w1, -1)
    print(w1_flat)
    w2_flat = np.reshape(w2, -1)
    print(w1.reshape(-1,1))
    w = np.concatenate((w1_flat, w2_flat))
    print(w)
if __name__ == '__main__':
    main()
