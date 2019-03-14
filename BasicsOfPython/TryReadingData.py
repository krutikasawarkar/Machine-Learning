import scipy as sp
import matplotlib.pyplot as plt

#Reading data
data = sp.genfromtxt("./Data/web_traffic.tsv.txt", delimiter="\t")
print(data[:10])
print(data.shape)

#Preprocessing and cleaning data
x= data[:,0]
y= data[:,1]

print(sp.sum(sp.isnan(y)))

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
print(x)
print(y)

#plotting data
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],
	['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()