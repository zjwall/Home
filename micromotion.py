import scipy.special as sci
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import h,pi

#Read CSV file
#for s in np.arange(10,250,3):
with open("Z:/Group_Share/Barium/Data/2020.dir/11.dir/2020_11_17.dir/000" + '28' + " - E2LaserSweep_prob.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    data = [row for row in reader]

    #graph raw data
    x =  [float(item[0]) for item in data]
    y =  [1-float(item[1]) for item in data]
    #plt.xticks(np.arange(0,2,.1),np.around(np.arange(int(float(x[0]))-1,int(float(x[len(x)-1]))+1,.1),3),rotation ='vertical')
    #plt.yticks(np.arange(0,1,.1))
    plt.figure()
    plt.plot(x,y)
    plt.xticks(rotation=90)
    plt.show()
#sum = np.zeros(200)
sum = np.zeros(len(x))
omega = 2.2 * 10 ** 6
gamma = (1/30)*2*pi
w_laser = x
#delta = np.arange(-100000000,100000000,1000000)
for i in range(len(x)):
    for n in np.arange(-200,200,1):
        sum[i] += ((sci.jv(n,5))**2)/((((w_laser[i]-6100)*10**6)+n*omega)**2+.25*gamma**2)
        #sum[i] += ((sci.jv(n,1.7))**2)/((delta[i]+n*omega)**2+.25*gamma**2)
plt.figure()
plt.plot(x,sum)
