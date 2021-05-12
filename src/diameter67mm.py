from api import *
import matplotlib.pyplot as plt
import numpy as np
import math


def plot_67mm_diameter_graph():

    x = np.array([200**2, 400**2, 600**2, 800**2, 1000**2, 1200**2, 1400**2, 1600**2, 1800**2, 2000**2, 2200**2, 2400**2,2600**2,2800**2])
    y = np.array([0.066,0.277,0.574,1.116,1.535,2.503,3.232,4.41,5.238,6.164,8.456,10.08,11.475,13.759])

    p2 = np.polyfit(x, y, 2)

    xp = np.linspace(x[0], x[len(x) - 1], 1000)

    plt.plot(x, y, "ro", label="67.5mm Diameter")
    plt.plot(xp, np.polyval(p2, xp), "r-")

    plt.title("RPM vs. Thrust", fontsize=16)
    plt.ylabel("Thrust", fontsize=12)
    plt.xlabel("RPM", fontsize=12)

    plt.grid(b=None, which='major', axis='both')

    slope = np.polyfit(np.log(x), np.log(y), 1)
    print("Slope:", slope[0])

    plt.legend(loc="upper left")

    plt.savefig("diameter: 67mm.png")
    plt.show()
