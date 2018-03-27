#-*- coding:utf-8 -*-
import sys
import random
import math
import time

def insertSort(arr):
    a = arr
    for j in range(len(a)):
        for i in range(j):
            if a[i]>a[j]:
                a[i], a[j] = a[j], a[i]
    return a

def fastSort(arr):
    a = arr
    def sortOption(a):
        if len(a) <= 1:
            return a
        # 左子数组
        less = []
        # 右子数组
        greater = []
        # 基准数
        base = a.pop() #remove one element and return the value (default the last one)
        # 对原数组进行划分
        for x in a:
            if x < base:
                less.append(x)
            else:
                greater.append(x)
                # 递归调用
                return sortOption(less) + [base] + sortOption(greater)
    return sortOption(a)

def shellSort(arr):    #希尔排序
    a = arr
    n = len(a)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while (i - gap) >= 0:
                if a[i] < a[i - gap]:
                    a[i], a[i - gap] = a[i - gap], a[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return a

def heapSort(arr):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    heap = arr

    def MAX_Heapify(heap,HeapSize,root):#在堆中做结构调整使得父节点的值大于子节点
        left = 2*root + 1
        right = left + 1
        larger = root
        if left < HeapSize and heap[larger] < heap[left]:
            larger = left
        if right < HeapSize and heap[larger] < heap[right]:
            larger = right
        if larger != root:#如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
            heap[larger],heap[root] = heap[root],heap[larger]
            MAX_Heapify(heap, HeapSize, larger)

    def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
        HeapSize = len(heap)#将堆的长度当独拿出来 - 方便
        for i in xrange((HeapSize -2)//2,-1,-1):#从后往前出数
            MAX_Heapify(heap,HeapSize,i)

    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0)
    return heap

def findPrimeNum(max):
    list = []
    def prime(n):
        if n%2 == 0:
            return n==2
        elif n%3 == 0:
            return n==3
        elif n%5 == 0:
            return n==5
        else:
            for p in xrange(7,n,2):    #只考虑奇数作为可能因子
                if n%p == 0:
                    return 0
            return 1

    for n in xrange(2,max+1):
        if prime(n):
            list.append(n)
    return list

def findPrimeFast(n):
    list = []
    flag = [1]*(n+2)
    p=2
    while(p<=n):
        list.append(p)
        for i in xrange(2*p,n+1,p):
            flag[i] = 0
        while 1:
            p += 1
            if(flag[p]==1):
                break
    return list

def test(n):
    arr = random.sample(range(n),n)
    #print(arr)
    start_time = time.time()
    insertSort(arr)
    print("insertSort(%d): %.15f seconds " % (n,(time.time() - start_time)) )
    start_time = time.time()
    shellSort(arr)
    print("shellSort(%d):  %.15f seconds " % (n,(time.time() - start_time)) )
    start_time = time.time()
    heapSort(arr)
    print("heapSort(%d):   %.15f seconds " % (n,(time.time() - start_time)) )
    start_time = time.time()
    fastSort(arr)
    print("fastSort(%d):   %.15f seconds " % (n,(time.time() - start_time)) )
    print("----------------------------------------------------")
    start_time = time.time()
    findPrimeNum(n)
    print("findPrimeNum(%d):  %.15f seconds " % (n,(time.time() - start_time)) )
    start_time = time.time()
    findPrimeFast(n)
    print("findPrimeFast(%d): %.15f seconds " % (n,(time.time() - start_time)) )


if __name__ == '__main__':
    test(input('Please input large integer: '))
