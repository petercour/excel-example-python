# coding: utf-8
import  pandas  as pd
 
df = pd.read_excel('example.xls')
data1 = df.head(7)
data2 = df.values
print("A \n{0}".format(data1)) 
print("B \n{0}".format(data2)) 
