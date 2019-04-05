import scipy as sp
import matplotlib.pyplot as plt

#Reading data
data = sp.genfromtxt("./Data/web_traffic.tsv.txt", delimiter="\t")
#print(data[:10])
#print(data.shape)

#Preprocessing and cleaning data
x= data[:,0]
y= data[:,1]

#print(sp.sum(sp.isnan(y)))

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
#print(x)
#print(y)

##plotting data
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],
	['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()

##Starting with simple straight line

def error(f,x,y):
	return sp.sum((f(x)--y)**2)

fp1, residuals, rank, sv, rcond = sp.polyfit(x,y,1,full=True)
print ("Model parameters: %s" % fp1)

f1 = sp.poly1d(fp1)
print(error(f1,x,y))

fx = sp.linspace(0,x[-1],1000) #generate x values for plotting
plt.plot(fx, f1(fx), linewidth=4)
plt.legend(["d=%i" % f1.order], loc="upper left")
plt.show()