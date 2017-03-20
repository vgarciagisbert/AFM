import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import time

X=np.linspace(0,6.14,200)
Y=np.cos(X)
fig = plt.figure(figsize=(6,6))
ax1 = fig.add_subplot(7,1,1)
ax2 = fig.add_subplot(7,1,2)
ax3 = fig.add_subplot(7,1,3)
ax4 = fig.add_subplot(7,1,4)
ax5 = fig.add_subplot(7,1,5)
ax6 = fig.add_subplot(7,1,6)
ax7 = fig.add_subplot(7,1,7)




with PdfPages('deleteme5.pdf') as pdf:
    line1 = ax1.plot(X, Y)[0]
    line2 = ax2.plot(X, Y)[0]
    line3 = ax3.plot(X, Y)[0]
    line4 = ax4.plot(X, Y)[0]
    line5 = ax5.plot(X, Y)[0]
    line6 = ax6.plot(X, Y)[0]
    super_t=time.time()
    for n in range(100):
        
        
        p=10*np.random.rand(10)
        Y1=np.cos(X*n*p[0])
        Y2=np.cos(X*n*p[1])
        Y3=np.cos(X*n*p[2])
        Y4=np.cos(X*n*p[3])
        Y5=np.cos(X*n*p[4])
        Y6=np.cos(X*n*p[5])
        t=time.time()
        # Now instead of plotting, we update the current line:
        line1.set_xdata(X)
        line1.set_ydata(Y1)
        line2.set_xdata(X)
        line2.set_ydata(Y2)
        line3.set_xdata(X)
        line3.set_ydata(Y3)
        line4.set_xdata(X)
        line4.set_ydata(Y4)
        line5.set_xdata(X)
        line5.set_ydata(Y5)
        line6.set_xdata(X)
        line6.set_ydata(Y6)
        # If autoscaling is necessary:
        ax1.relim()
        ax1.autoscale()
        ax2.relim()
        ax2.autoscale()
        ax3.relim()
        ax3.autoscale()
        ax4.relim()
        ax4.autoscale()
        ax5.relim()
        ax5.autoscale()
        ax6.relim()
        ax6.autoscale()
        t2=time.time()-t
        pdf.savefig(fig)
        t=time.time()-t
        #not implementedyet
        for index_sub in range(1,7,1):
            my_fig=fig
            my_fig.get_children()[1].get_children()[0].get_ydata() #this really works!
            my_fig.get_children()[1].get_children()[0].get_ydata()
            my_ax=my_fig.get_children[index_sub]
            my_line=ax.get_children[0]
            my_line=ax.get_children[1]
            
super_t=time.time()-super_t
print('on average, each one takes: '+str(super_t/100))
