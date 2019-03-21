import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

XYZ_web = {'Day':[1,2,3,4,5,6], "Visitors":[1000,700,6000,4200,520,3000], 'Bounce_Rate':[20,21,23,15,24,3]}

##Convert this dictionary into pandas DataFrame.
df= pd.DataFrame(XYZ_web)
#print(df)

##slicing
#get first 2 rows
#print(df.head(2))

#get last 2 rows
#print(df.tail(2))

##Merging
df1 = pd.DataFrame({"HPI":[80,90,70,60], "Int_rate":[2,1,2,3],"ÏND_GDP":[50,45,40,64]},
					index = [2001,2002,2003,2004])

df2 = pd.DataFrame({"HPI":[80,90,70,60], "Int_rate":[2,1,2,3],"ÏND_GDP":[50,45,40,64]},
					index = [2005,2006,2007,2008])
#merge = pd.merge(df1,df2)
#print(merge)

#Suppose you want to keep only on column common
#merge = pd.merge(df1,df2, on = "HPI")
#print(merge)

##Joining
#df1 = pd.DataFrame({"Int_rate":[2,1,2,3],"ÏND_GDP":[50,45,40,64]},
#					index = [2001,2002,2003,2004])

#df2 = pd.DataFrame({"Low_Tier_HPI":[50,45,67,34],"Unemployment":[1,3,5,6]},
#					index = [2001,2003,2004,2004])

#joined = df1.join(df2)
#print(joined)

##Changing the Index and Column headers
#changeIndexAndColumnHeader = {"Day":[1,2,3,4], "Visitors":[200,100,230,300], 'Bounce_Rate':[20,21,23,15]}
#df = pd.DataFrame(changeIndexAndColumnHeader)

#U want to change the index 
#df.set_index("Day", inplace=True)
##print(df)
#df.plot()
#plt.show()

#now suppose we wanna change column header from Visitors to Users
#df = df.rename(columns={"Visitors":"Users"})
#print(df)


##Concatenation
#concat = pd.concat(df1,df2)
#print(concat)

##Data Munging: can convert particular form of data in a different format
#example: txt-->xhtml
#not working .
#demo = pd.read_csv('C:\\Users\\sawa_kru\\Downloads\\SampleCSVFile_2kb.csv', index_col=0)
#demo.to_html('edu.html')