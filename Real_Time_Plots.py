import psutil
import matplotlib.pyplot as plt
i = 0
fig = plt.figure('Precentage of used CPU')
ax = fig.add_subplot(1, 1, 1)
pcu = []
x = []
while True:
    i = i+1
    pcu = pcu[-20:]
    pcu.append(psutil.cpu_percent())
    x = x[-20:]
    x.append(i)
    plt.title('Precentage of used CPU')
    plt.xlabel("Time [0.1s]")
    plt.ylabel('CPU [%]')
    ax.plot(x, pcu, c='red')
    plt.pause(0.1)



