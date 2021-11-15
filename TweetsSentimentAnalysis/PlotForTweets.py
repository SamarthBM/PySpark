import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(i):
    try:
        data = pd.read_csv('tweets.csv')
        x1 = data['pos']
        x2 = data['neg']
        y1 = data['positive_count']
        y2 = data['negative_count']
        plt.cla()
        plt.bar(x1,y1,label="positive")
        plt.bar(x2,y2,label='negative')
        plt.xlabel("Polarity")
        plt.ylabel("count")
        plt.tight_layout()

    except Exception as e:
        print(e)


ani = FuncAnimation(plt.gcf(),animate,interval=500)

plt.tight_layout()
plt.show()