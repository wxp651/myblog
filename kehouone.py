#coding=utf-8
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
#str1 = input("请输入一个人的名字：")#py3
'''str1 =  raw_input("请输入一个人的名字：")#py2
str2 = raw_input("请输入一个国家的名字：")
print "世界那么大,{}想去{}看看!".format(str1,str2)
n=raw_input("请输入整数:")
sum=0
for i in range(int(n)):
    sum+=i+1
print '1到N求和结果:',sum

for i in range(1,10):
    for j in range(1,i+1):
        print ("{}*{}={:2}".format(j,i,i*j)),#py2,在句尾加，#py3加end=''  ("{}*{}={:2}".format(j,i,i*j),end=' ')
    print ''
sum,tmp=0,1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print '运算结果：{}'.format(sum)

n=1#猴子吃桃问题
for i in range(5,0,-1):
    n=(n+1)<<1
print n

diet=['西红柿','花菜','黄瓜','牛排','虾仁']
for x in range(0,5):
    for y in range(0,5):
        if not(x==y):
            print "{}炒{}".format(diet[x],diet[y])
'''
import turtle