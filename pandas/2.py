# Series 
from turtle import TPen
import pandas as pd
u1=[10,0,30,4]
s=pd.Series(u1, name="NO of time watch")
print(type(s))
print(s)
print(s[0])
print(s[2])
print(s[1:3])