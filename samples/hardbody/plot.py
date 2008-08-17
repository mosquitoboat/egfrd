#!/usr/bin/env/python

import sys

import numpy
import scipy.io
from matplotlib.pylab import *


N_A = 6.0221367e23

def plot_data( N, T, fmt ):
    T = numpy.array( T )

    mean = T.mean(1)
    std_err = T.std()/math.sqrt(len(T))

    #errorbar( N, mean, yerr=std_err, fmt=fmt )
    print N, mean
    loglog( N, mean, fmt )


T=0.001
V=40e-15
#N=100
#C=


data_V = [
# T=1, N=30, V=4e-14
[23.315,22.9394,20.5574,],
# T=0.1, N=100, V=4e-14
[149.173,184.204,151.575,],
# T=0.1, N=300, V=4e-14
[1064.21,1126.35,1058.9,],
# T=0.01, N=1000, V=4e-14
[8091.16,8165.06,8251.17,],
# T=0.001, N=3000, V=4e-14
[55945.4,56406.1,54867.2,],
# T=0.001, N=10000, V=4e-14
[450881,432767,465305,],
# T=0.001, N=30000, V=4e-14
[3.64982e+06,3.81537e+06,3.67867e+06,],
# T=0.0001, N=100000, V=4e-14
[5.15492e+07,5.21321e+07,5.47858e+07,],
# T=1e-05, N=300000, V=4e-14
[9.74809e+08,1.04633e+09,1.19417e+09,],
]


data_C = [
# T=0.1, N=30, V=4e-16
[468.066,507.768,467.671,],
# T=0.01, N=100, V=1.3e-15
[1719.25,2028.88,1795.73,],
# T=0.01, N=300, V=4e-15
[4857.45,5050.15,4895.15,],
# T=0.001, N=1000, V=1.3e-14
[17910,17879,19016,],
# T=0.001, N=3000, V=4e-14
[54424.8,61632.8,61028.5,],
# T=0.001, N=10000, V=1.3e-13
[185866,199623,209752,],
# T=0.001, N=30000, V=4e-13
[590986,601685,605688,],
# T=0.001, N=100000, V=1.3e-12
[2.1659e+06,2.12368e+06,2.08641e+06,],
# T=0.001, N=300000, V=4e-12
[6.51655e+06,6.69382e+06,6.65525e+06,],

# T=0.0001, N=1e+06, V=1.3e-11
#[1.11533e+08,1.19388e+08,1.24238e+08,],

]


data_N300 = [
# T=0.01, N=300, V=4e-13
[397.484,223.208,335.77,],
# T=0.01, N=300, V=4e-14
[1024.77,1261.94,1096.29,],
# T=0.001, N=300, V=4e-15
[5129,4306.26,5631.82,],
# T=0.001, N=300, V=4e-16
[56705,29575.4,52085.5,],
# T=0.0001, N=300, V=4e-17
[640690,1.61436e+06,507055,],
# T=1e-05, N=300, V=4e-18
[1.41336e+07,2.21781e+07,2.45075e+07,],
# T=1e-06, N=300, V=4e-19
[1.95089e+08,2.73275e+08,2.069e+08,],
# T=1e-06, N=300, V=1e-19
#[1.67064e+09,1.72815e+09,1.70991e+09,],
]





data_N3000 = [
# T=0.01, N=3000, V=4e-12
[2816.14,2636.4,2925.99,],
# T=0.01, N=3000, V=4e-13
[11614.1,10752.4,11324.9,],
# T=0.001, N=3000, V=4e-14
[58727,55016.6,57321.9,],
# T=0.001, N=3000, V=4e-15
[316766,361824,388791,],
# T=0.001, N=3000, V=4e-16
[6.25142e+06,6.32483e+06,6.35022e+06,],
# T=0.0001, N=3000, V=4e-17
[2.17666e+08,2.18491e+08,2.19281e+08,],
# T=1e-05, N=3000, V=4e-18
[2.31403e+09,2.39566e+09,2.48136e+09,],
]






Nv = numpy.array([30,100,300,1000,3000,10000,30000,100000,300000])
Nc = numpy.array([30,100,300,1000,3000,10000,30000,100000,300000])#,1000000])

# (40e-18 ** (1/3.0))**2 / 1e-12
# = 11.69607095285148

Nb = numpy.array([10,30,100,300,1000,3000,10000])#,30000,100000])
data_bd_5 = numpy.array([\
        #t=1e-8, dt = 1e-5 tau
        [0.0485391616821,0.0476109981537,0.0482919216156],
        [0.138695001602,0.139840841293,0.139472007751],
        [0.45738196373,0.454463005066,0.458449840546],
        [1.35839486122,1.36714601517,1.36983513832],
        [4.74575400352,4.73176693916,4.71269416809],
        [14.96296978,14.7860958576,14.9349989891],
        [50.471544981,51.1204040051,51.8594009876],
#        [0,0,0],
#        [0,0,0]]
        ])
data_bd_5 *=  11.696/ 1e-8
data_bd_6 = data_bd_5 * 10

X = numpy.array([5,100,300,1000,3000,10000,30000,100000,5e6])


axes([.12,.12,.8,.8])

#for i in range( len(Nv) ):
plot_data( Nv, data_V,'kx' )

loglog( X, 0.09* X**(5.0/3), 'k--' )

figtext( .25, .18, r'(2) V = 40 fL' )
figtext( .8, .72, r'$t \ \propto \ N^{5/3}$', color='k' )


#for i in range( len(Nc) ):
plot_data( Nc, data_C,'ko' )
loglog( X, 18* X, 'k-' )

figtext( .135, .36, r'(1) C = 100 nM' )
figtext( .8, .59, r'$t \  \propto \ N$', color='k' )

#plot_data( Nb, data_bd_6,'k.' )

loglog( X, 5e7* X, 'b:' ) # 1e-6 tau
loglog( X, 5e4* X, 'b:' ) # 1e-3 tau

figtext( .2, .78, r'BD', color='k' )

figtext( .19, .62, r'BD (relaxed)', color='k' )

#loglog( data1[0] , data1[1], 'o-', label='Vol. = 1e-15 L' )
#loglog( data2[0] , data2[1], 'o-', label='# particles = 600' )
#loglog( data3[0] , data3[1], 'o-', label='Conc. = 1e-6 M' )

xlabel( 'N [# particles]', size=18 )
#xlabel( 'Concentration [M]' )
ylabel( 'time [s]', size=18 )
#legend()
xlim(4,9e6)
ylim(1.1,2e11)

#xticks( Nv )

#grid()

Cx3000=numpy.array([
#    9.35e-11,
    9.35e-10,
    9.35e-9,
    9.35e-8,#N=3000,V=40e-15
    9.35e-7,#N=3000,V=40e-16
    9.35e-6,#N=3000,V=40e-17
    9.35e-5,#N=3000,V=40e-18
    9.35e-4

    ])

Cx300=numpy.array([
    9.35e-10,#N=300,V=40e-14
    9.35e-9,#N=300,V=40e-15
    9.35e-8,#16
    9.35e-7,#17
    9.35e-6,#18
    9.35e-5,#19
    9.35e-4,#20
#    3.74e-3,#1e-21
#    9.35e-3,#4e-21
    ])

#data_N3000 *= 11696
#data_N300 *= 11696

axes([.60,.16,.28,.29])

# M-> uM
Cx300 *= 1e6
Cx3000 *= 1e6

for i in range( len(Cx3000) ):
    plot_data( Cx3000, data_N3000,'k+' )
#loglog( Cx3000, 5e1** Cx3000, 'b:' )
bd3000 = numpy.array([17.1796619892,17.4832251072,17.5032970905]).mean()
bd3000 *= 11.69607 / 1e-9
loglog( [1e-4,1e4],[bd3000,bd3000], 'b:' )


for i in range( len(Cx300) ):
    plot_data( Cx300, data_N300,'kd' )
loglog( Cx300, 2.5e4* Cx300**(2.0/3.0), 'k-.', label='C^(2/3)' )
#loglog( Cx300, 2.5e4* Cx300**(4.0/3.0), 'k-.', label='C^(4/3)' )

figtext( .73, .18, r'(3a) N = 300' )
figtext( .79, .22, r'$t \ \propto \ C^{2/3}$', color='k' )
figtext( .62, .31, r'(3b) N = 3000' )

#bd 300
bd300 = numpy.array([1.62390208244,1.62284588814,1.63388109207]).mean()
bd300 *= 11.69607 / 1e-9
loglog( [1e-5,1e5],[bd300,bd300], 'b:' )

figtext( .63, .405, r'BD', color='k' )

#xlabel( 'Concentration' )
#ylabel( 'time [s]' )

#xlim(5e-10,5e-2)
#ylim(1e2,5e9)
#xlim(5e-10,5e-3)
xlim(2e-4,9e3)
ylim(2e2,8e11)

xticks( [1e-3, 1e0, 1e3], ['nM','uM','mM'] )
yticks( [1e4, 1e7, 1e10] )

show()
#savefig('fig1.eps')




#>>> _gfrd.S_irr( .0001 * 1e-8**2/1e-12, 1e-8, 10 * 1e-8 * 1e-12, 1e-12, 1e-8 )
#0.99116163945434221


