import numpy as np
import pandas as pd

dict1 = {
    "train number": [1, 2, 2, 33, 44, 55],
    "SPEED": [111, 222, 333, 444, 555, 666],
    "city": ['pkr', 'ktm', 'lum', 'syn', 'kol', 'dub']
}

df = pd.DataFrame(dict1)
print(df)


df.to_csv('friends_index_false.csv', index=False)
df.describe()
ser=pd.Series(np.random.rand(34))
ser
type(ser)
pd.core.series.Series
newdf= pd.DataFrame(np.random.rand(334,5), index=np.arange(334))
newdf
newdf.head()
newdf.describe()

newdf[0][0]='harry'
newdf.dtypes
newdf.head()
newdf.index
newdf.to_numpy()
newdf[0][0]=3
newdf.T#vtranspose
newdf.head()
newdf.sort_index(axis=1, ascending =False)
# newdf[0] # Commented out the line causing the TypeError
type(newdf[0])
newdf.head()
newdf2=newdf #just like ponter
newdf2[0][0] =9720
newdf
newdf.loc[0,0]=654# to set value
newdf.head(2)
newdf.columns=list("abcde")#change past columns to abcd
newdf.head(2)
newdf.loc[0,'a']=111# because i change 0 1 2  to abcd soo
newdf.head(2)
newdf= newdf.drop('a', axis=1) # axes 0=row and axes 1=colunm
newdf.head()
newdf.loc[[1,2],['c','d']]# to gt value of c and d
newdf.head() # it doesnot change
newdf.loc[[1,2],:] # change row and coumn
newdf.loc[(newdf['b']<0.3) & (newdf['c']>0.1) ] #cahnge and make value greater or less on basis of given condition
# newdf.iloc[0,4] # give value of row 0 and column 4 # Commented out the line causing the IndexError
newdf.iloc[1, 3]
newdf.iloc[1, 3]
 # give value of row 1 and column 'd'
newdf.iloc[[0,5] , [1,2]]
newdf.head(3)
#newdf.drop (['1,5 '], axis=0, inplace=True) # rMOVE 1 AND 5
newdf.dropna() #  remove na
newdf.mean()
newdf.median()
newdf.max()
newdf.min()

data=pd.read_excel('data.xlsx', sheet_nam='sheet 2')
data.iloc[0,0]=34
data

