import numpy as np
import matplotlib.pyplot as plt

#Declare array 
a = np.array([(1,2,3),(4,5,6)])
b = np.array([(7,8,9),(10,11,12)])
#print(a)

#Get the size of an array
#D = np.arange(1000)
#print(D.size * D.itemsize)

#Sum of 2 numpy array
#SIZE = 1000
#A1 = np.arange(SIZE)
#A2 = np.arange(SIZE)
#result = A1 + A2
#print(result)

#To find dimention of array
#print(a.ndim)

#To find byte size of array
#print(a.itemsize)

#To find data type of array
#print(a.dtype)

#To find size of array
#print(a.size)

#To find shape of array
#print(a.shape)

#To reshape an array
#a = a.reshape(3,2)
#print(a)

#slicing
#this will print 2nd index of every row
#print(a[0:,2])
#this will print 2nd index of every row expect that which is mentioned acfter colon
#print(a[0:1,2])

#this will print 5 values which are eqally spaced between 1 and 3.
#a = np.linspace(1,3,5)
#print(a)

#to find max and min value
#amax = a.max()
#amin = a.min()
#print(amax)
#print(amin)

#axis concept
#print(a.sum(axis=0))

#standard deviation: find out mean of all the elements in your array,
#and fing how much each element deviates from this mean value
#print(np.sqrt(a))
#print(np.std(a))

#addition, multiplication, subtraction and division
#print(a + b)
#print(a * b)
#print(a / b)
#print(a - b)

#concatination of aray
#two types: vertical stacking and horizontal stacking
#print(np.vstack((a,b)))
#print(np.hstack((a,b)))

#convert a into single column
#print(a.ravel())

#matplot example with numpy
#x = np.arange(0, 3*np.pi, 0.1)
#y = np.sin(x)
#plt.plot(x,y)
#plt.show()

#numpy exponential and logx function
print(np.log10(a))