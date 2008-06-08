#!/usr/bin/env/python

import sys

import numpy
import scipy.io
from matplotlib.pylab import *


N_A = 6.0221367e23

def plot_data( N, T, fmt ):

    mean = T.mean(1)
    std_err = T.std()/math.sqrt(len(T))

    #errorbar( N, mean, yerr=std_err, fmt=fmt )
    print N, mean
    loglog( N, mean, fmt )


T=0.001
V=40e-15
#N=100
#C=

Nv = numpy.array([30,100,300,1000,3000,10000,30000,100000,300000])

#constant V
data_V = numpy.array([\
        [0.026524066925,0.0297000408173,0.0274858474731],\
        [0.142389059067,0.113878965378,0.115298986435],\
        [0.42008805275,0.552675008774,0.504842042923],\
        [2.62250494957,2.66188097,2.69252300262],\
        [15.1535229683,16.8973779678,14.9991471767],\
        [124.967854023,133.611082077,123.066022873],\
        [1034.05404186,1096.23250008,1057.50415492],\
        [8449.71553087,8680.26774883,8656.0344696],
        [106510.697317,99656.1300039,106500],
        ])

Nc = numpy.array([30,100,300,1000,3000,10000,30000,100000,300000])
#constant C
data_C = numpy.array([\
        [0.184664011002,0.133192062378,0.0721089839935],
        [0.494563102722,0.608535051346,0.625062942505],
        [1.80025911331,1.86633396149,1.7485370636],
        [5.40078306198,5.61715006828,5.58888196945],
        [15.1535229683,16.8973779678,14.9991471767],
        [56.2781181335,58.5534842014,58.6970460415],
        [166.159019947,163.929265976,170.353613138],
        [581.35748601,581.,583.06929493],
        [3680.69806099,3458.51354122,3600] ])


# (40e-18 ** (1/3.0))**2 / 1e-12
# = 11.69607095285148
data_V *= 11696
data_C *= 11696

Nb = numpy.array([10,30,100,300,1000,3000,10000,30000,100000])
data2 = numpy.array([\
        [0.0333709716797,0.0316069126129,0.0350742340088],
        [0.133962154388,0.144722938538, 0.129770040512],
        [0.453906059265,0.476196050644,0.480502128601],
        [1.31794595718,1.31320905685,1.24801301956],
        [4.22622799873,4.18033003807,4.1173210144],
        [12.1447920799,11.9920589924,12.0459198952],
        [39.7432990074,40.1183140278,39.9150369167],
        [0,0,0],
        [0,0,0]])
data2 *= 1169607
data3 = data2 * 10
data4 = data2 * 100

X = numpy.array([2,100,300,1000,3000,10000,30000,100000,3e6])

#for i in range( len(Nv) ):
plot_data( Nv, data_V,'kx' )
loglog( X, 0.3* X**(5.0/3), 'k--' )

figtext( .2, .15, r'(2) $y \ \propto \ N^{5/3}$', color='k' )

#for i in range( len(Nc) ):
plot_data( Nc, data_C,'ko' )
loglog( X, 60* X, 'k-' )

figtext( .15, .32, r'(1) $y \  \propto \ N$', color='k' )

#for i in range( len(Ns) ):
#    plot_data( Ns[i], data2[i],'k.' )
loglog( X, 4500* X, 'b:' )

#for i in range( len(Nb) ):
plot_data( Nb, data4,'k.' )
loglog( X, 45000* X, 'b:' )

#for i in range( len(Ns) ):
#    plot_data( Ns[i], data4[i],'k.' )
loglog( X, 450000* X, 'b:' )

figtext( .25, .6, r'BD', color='k' )

#loglog( data1[0] , data1[1], 'o-', label='Vol. = 1e-15 L' )
#loglog( data2[0] , data2[1], 'o-', label='# particles = 600' )
#loglog( data3[0] , data3[1], 'o-', label='Conc. = 1e-6 M' )

xlabel( 'N [# particles]' )
#xlabel( 'Concentration [M]' )
ylabel( 'time [sec]' )
#legend()


Cx3000=numpy.array([
    9.35e-11,
    9.35e-10,
    9.35e-9,
    9.35e-8,#N=3000,V=40e-15
    9.35e-7,#N=3000,V=40e-16
    9.35e-6,#N=3000,V=40e-17
    9.35e-5,#N=3000,V=40e-18
    9.35e-4

    ])
data_N3000 = numpy.array([\
        [2.60435891151,2.66381216049,2.65526103973],
        [2.96514296532,2.98465490341,2.91663217545],
        [5.06253409386,5.16982102394,4.63183999062],
        [15.1535229683,16.8973779678,14.9991471767],
        [91.7706329823,81.1482388973,83.5025150776],
        [778.856128931,814.321280003,814.321280003],
        [14289.9441504,0,0],
        [168404.857111,172778.390098,0]
        ])

Cx300=numpy.array([
    9.35e-10,#N=300,V=40e-14
    9.35e-9,#N=300,V=40e-15
    9.35e-8,
    9.35e-7,
    9.35e-6,
    9.35e-5,
    9.35e-4,
    9.35e-3,
    ])
data_N300 = numpy.array([\
        [0.292788028717,0.290889978409,0.29689002037],
        [0.42008805275,0.552675008774,0.504842042923],\
            [1.77118682861,1.79518914223,1.48541378975],\
            [7.26162099838,7.4746389389,7.98878598213],\
            [72.3886461258,85.8097350597,70.3874559402],\
            [1492.82738304,0,0],
            [16768.1778502,0,0],
            [0,0,0]
        ])

data_N3000 *= 11696
data_N300 *= 11696

axes([.61,.18,.27,.28])

#for i in range( len(Cx3000) ):
#plot_data( Cx3000, data_N3000,'k+' )
#loglog( Cx3000, 5e6** Cx3000, 'b:' )
#bd3000 = numpy.array([12.1447920799,11.9920589924,12.0459198952]).mean()
#bd3000 *= 1169607 * 10
#loglog( [1e-11,1e-2],[bd3000,bd3000], 'b:' )


#for i in range( len(Cx300) ):
plot_data( Cx300, data_N300,'kd' )
loglog( Cx300, 2e11* Cx300*(1.0/3.0), 'k--', label='C^(1/3)' )

figtext( .69, .2, r'(3) $y \ \propto \ C^{1/3}$', color='k' )

#bd 300
bd300 = numpy.array([1.31794595718,1.31320905685,1.24801301956]).mean()
bd300 *= 1169607 * 10
loglog( [1e-11,1e-2],[bd300,bd300], 'b:' )

figtext( .65, .4, r'BD', color='k' )

xlabel( 'Concentration [M]' )
ylabel( 'time [sec]' )

xlim(5e-10,5e-3)
ylim(1e2,2e9)
show()




#>>> _gfrd.S_irr( .0001 * 1e-8**2/1e-12, 1e-8, 10 * 1e-8 * 1e-12, 1e-12, 1e-8 )
#0.99116163945434221

