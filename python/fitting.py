# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:14:28 2015

"""

import numpy as np
import matplotlib.pylab as pl


M=3  # 次数
freq=1.0  #元の波形周波数
actN=10  #サンプリングする個数
sigma=0.2  #ノイズの分散
actdatax=np.linspace(0.0, 1.0, actN+1 )
actdata=np.sin( 2*freq*actdatax*np.pi )

sampledatax=np.linspace( 0.0, 1.0, actN+1 )
sampledata=np.sin( 2*freq*sampledatax*np.pi )
noise = np.random.normal(0,sigma,actN+1)
sampledata += noise;

# sampledatax[] sampledata[]  ノイズ入りの波形からactN個サンプリングしたデータ

 
# -----
lam=0.0
sumxn=[0.0]*(M*2)
sumtnxn=[0.0]*(M+1)
  
for i in range( 0, actN ):
    for j in range( 0, M*2 ):
        sumxn[j] += sampledatax[i]**(j+1)
    for j in range( 0, M+1):
        sumtnxn[j] += sampledata[i]*sampledatax[i]**j


m=np.zeros((M+1,M+1))
v=np.zeros(M+1)
w=np.zeros(M+1)
for row in range(0,M+1):
    for col in range(0,M+1):
        if row+col==0:
            m[row,col]= actN+lam
        else:
            m[row,col]= sumxn[col+row-1]
            if row==col:
                m[row,col]=sumxn[col+row-1]+lam

for row in range(0, M+1):
    v[row]=sumtnxn[row]
    
mi=np.linalg.inv( m )
w = np.dot( mi, v)
# y=w[0]+w[1]*x+w[2]*x**2+w[3]*x**3...w[actN]*x**actN

resampleN = 100
resamplex = np.linspace( 0.0, 1.0, resampleN+1 )
resample=[0.0]*(resampleN+1)
for n in range(0,resampleN+1):
    ta = 0.0
    for j in range(0,M+1):
        ta += w[j]*resamplex[n]**j
    resample[n] = ta
    
pl.ylim( -1.5,1.5 )
pl.plot( actdatax, actdata, 'bs-', sampledatax,sampledata, 'rx' )
pl.plot( resamplex, resample, 'go' )
pl.show()
