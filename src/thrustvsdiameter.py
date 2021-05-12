from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_thrustvsdiameter_graphs():

  x = np.array([60, 62.5, 65, 67.5, 70, 72.5, 75, 77.5, 80])

  test1y = np.array([0.0428,0.037,0.039,0.066,0.078,0.082,0.091,0.054,0.063])
  test2y = np.array([0.118,0.235,0.209,0.277,0.185,0.332,0.241,0.368,0.253])
  test3y = np.array([0.265,0.54,0.478,0.574,0.606,0.827,0.589,0.548,0.561])
  test4y = np.array([0.47,0.95,0.915,1.116,1.018,1.364,1.025,0.952,1.07])
  test5y = np.array([0.715,1.519,1.34,1.535,1.586,2.176,1.636,1.543,1.544])
  test6y = np.array([1.049,2.115,1.995,2.503,2.333,3.212,2.048,2.378,2.346])
  test7y = np.array([1.45,2.965,2.582,3.232,3.319,4.15,3.286,3.296,3.136])
  test8y = np.array([1.905,3.446,3.382,4.41,4.084,5.28,4.327,3.734,4.072])
  test9y = np.array([2.308,4.05,4.671,5.238,6.014,6.873,7.082,4.84,5.456])
  test10y = np.array([3.277,4.183,6.024,6.164,7.452,8.185,8.825,6.135,6.131])
  test11y = np.array([4.382,4.68,6.731,8.456,9.267,10.553,10.612,7.42,7.897])
  test12y = np.array([5.139,5.484,8.135,10.08,11.191,12.508,12.665,9.3,9.383])
  test13y = np.array([5.506,8.93,10.897,11.475,12.741,14.661,14.062,11.047,11.376])
  test14y = np.array([6.103,9.98,11.386,13.759,15.676,16.67,16.889,12.727,12.601])


  test1 = np.polyfit(x, test1y, 4)
  test2 = np.polyfit(x, test2y, 4)
  test3 = np.polyfit(x, test3y, 4)
  test4 = np.polyfit(x, test4y, 4)
  test5 = np.polyfit(x, test5y, 4)
  test6 = np.polyfit(x, test6y, 4)
  test7 = np.polyfit(x, test7y, 4)
  test8 = np.polyfit(x, test8y, 4)
  test9 = np.polyfit(x, test9y, 4)
  test10 = np.polyfit(x, test10y, 4)
  test11 = np.polyfit(x, test11y, 4)
  test12 = np.polyfit(x, test12y, 4)
  test13 = np.polyfit(x, test13y, 4)
  test14 = np.polyfit(x, test14y, 4)
  
  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, test1y, "bo", label="200 rpm")
  plt.plot(x, test2y, "go", label="400 rpm")
  plt.plot(x, test3y, "ro", label="600 rpm")
  plt.plot(x, test4y, "yo", label="800 rpm")
  plt.plot(x, test5y, "co", label="1000 rpm")
  plt.plot(x, test6y, "mo", label="1200 rpm")
  plt.plot(x, test7y, "o", label="1400 rpm", color="orange")
  plt.plot(x, test8y, "o", label="1600 rpm",color="brown")
  plt.plot(x, test9y, "o", label="1800 rpm",color="pink")
  plt.plot(x, test10y, "o", label="2200 rpm",color="GreenYellow")
  plt.plot(x, test11y, "o", label="2400 rpm", color="DarkCyan")
  plt.plot(x, test12y, "o", label="2600 rpm",color="SeaGreen")
  plt.plot(x, test13y, "o", label="2800 rpm",color="Thistle")
  plt.plot(x, test14y, "o", label="3000 rpm",color="LightSlateGrey")

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
  plt.plot(xp, np.polyval(test12, xp), "-", color="SeaGreen")
  plt.plot(xp, np.polyval(test13, xp), "-", color="Thistle")
  plt.plot(xp, np.polyval(test14, xp), "-",color="LightSlateGrey")


  plt.title("Thrust vs. Diameter", fontsize=15)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([60, 62.5, 65, 67.5, 70, 72.5, 75, 77.5, 80])
  plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) 

  plt.legend(loc="upper left", prop={'size': 4.5})

  plt.savefig("thrustvsdiameter.png")
  plt.show()