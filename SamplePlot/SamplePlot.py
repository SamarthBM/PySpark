import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

x_values=[]
y_values=[]

def animate(i):
    x_values.append(random.randint(0,10))
    y_values.append(random.randint(0,5))

    plt.cla()
    plt.plot(x_values,y_values)

ani = FuncAnimation(plt.gcf(),animate,interval=1000)

plt.tight_layout()
plt.show()