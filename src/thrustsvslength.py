from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_thrustvslength_graphs():

  x = np.array([9.5, 11, 13.5, 15, 16.5, 18, 19.5])

  test1y = np.array([0.037,0.048,0.067,0.078,0.055,0.061,0.61])
  test2y = np.array([0.06,0.114,0.221,0.185,0.092,0.317,0.327])
  test3y = np.array([0.261,0.356,0.558,0.606,0.518,0.572,0.614])
  test4y = np.array([0.466,0.644,1.059,1.018,0.907,0.952,1.02])
  test5y = np.array([0.726,0.991,1.543,1.586,1.435,1.497,1.59])
  test6y = np.array([1.043,1.667,2.218,2.333,2.664,2.433,2.735])
  test7y = np.array([1.102,2.165,3.313,3.319,2.93,2.866,3.125])
  test8y = np.array([1.209,2.435,4.273,4.084,3.831,3.737,4.146])
  test9y = np.array([1.578,3.794,5.662,6.014,4.146,5.379,5.763])
  test10y = np.array([1.704,4.435,7.573,7.452,5.423,6.47,6.878])
  test11y = np.array([1.876,5.825,8.217,9.267,7.05,8.193,8.705])
  test12y = np.array([1.998,6.937,9.174,11.191,7.714,9.939,10.256])
  test13y = np.array([2.4,8.155,11.408,12.741,10.727,11.574,12.06])
  test14y = np.array([2.76,9.266,12.54,15.676,12.332,13.503,12.893])

  test1 = np.polyfit(x, test1y, 5)
  test2 = np.polyfit(x, test2y, 5)
  test3 = np.polyfit(x, test3y, 5)
  test4 = np.polyfit(x, test4y, 5)
  test5 = np.polyfit(x, test5y, 5)
  test6 = np.polyfit(x, test6y, 5)
  test7 = np.polyfit(x, test7y, 5)
  test8 = np.polyfit(x, test8y, 5)
  test9 = np.polyfit(x, test9y, 5)
  test10 = np.polyfit(x, test10y, 5)
  test11 = np.polyfit(x, test11y, 5)
  test12 = np.polyfit(x, test12y, 5)
  test13 = np.polyfit(x, test13y, 5)
  test14 = np.polyfit(x, test14y, 5)
  
  xp = np.linspace(x[0], x[len(x)-1], 100000)

  plt.plot(x, test1y, "bo", label="200 rpm")
  plt.plot(x, test2y, "go", label="400 rpm")
  plt.plot(x, test3y, "ro", label="600 rpm")
  plt.plot(x, test4y, "yo", label="800 rpm")
  plt.plot(x, test5y, "co", label="1000 rpm")
  plt.plot(x, test6y, "mo", label="1200 rpm")
  plt.plot(x, test7y, "o", label="1400 rpm", color="orange")
  plt.plot(x, test8y, "o", label="1600 rpm",color="brown")
  plt.plot(x, test9y, "o", label="1800 rpm",color="pink")
  plt.plot(x, test10y, "o", label="2000 rpm",color="GreenYellow")
  plt.plot(x, test11y, "o", label="2200 rpm", color="DarkCyan")
  plt.plot(x, test12y, "o", label="2400 rpm",color="aqua")
  plt.plot(x, test13y, "o", label="2600 rpm",color="Thistle")
  plt.plot(x, test14y, "o", label="2800 rpm",color="LightSlateGrey")

  plt.plot(xp, np.polyval(test1, xp), "b-")
  plt.plot(xp, np.polyval(test2, xp), "g-")
  plt.plot(xp, np.polyval(test3, xp), "r-")
  plt.plot(xp, np.polyval(test4, xp), "y-")
  plt.plot(xp, np.polyval(test5, xp), "c-")
  plt.plot(xp, np.polyval(test6, xp), "m-")
  plt.plot(xp, np.polyval(test7, xp), "-", color="orange")
  plt.plot(xp, np.polyval(test8, xp), "-", color="brown")
  plt.plot(xp, np.polyval(test9, xp), "-", color="pink")
  plt.plot(xp, np.polyval(test10, xp), "-",color="GreenYellow")
  plt.plot(xp, np.polyval(test11, xp), "-", color="DarkCyan")
  plt.plot(xp, np.polyval(test12, xp), "-", color="aqua")
  plt.plot(xp, np.polyval(test13, xp), "-", color="Thistle")
  plt.plot(xp, np.polyval(test14, xp), "-",color="LightSlateGrey")


  plt.title("Thrust vs. Length", fontsize=15)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([9.5, 11, 13.5, 15, 16.5, 18, 19.5])
  plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

  plt.legend(loc="upper left", prop={'size': 5})

  plt.savefig("thrustvsdiameter.png")
  plt.show()