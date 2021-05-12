from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_diameter_comparison_graphs():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800])

  diametery60 = np.array([0.0428, 0.118, 0.265, 0.47, 0.715, 1.049, 1.45, 1.905, 2.308, 3.277, 4.382, 5.139, 5.506, 6.103])
  diametery62 = np.array([0.037, 0.235, 0.54, 0.95, 1.519, 2.115, 2.965, 3.446, 4.05, 4.183, 4.68, 5.484, 8.93, 9.98])
  diametery65 = np.array([0.039, 0.209, 0.478, 0.915, 1.34, 1.995, 2.582, 3.382, 4.671, 6.024, 6.731, 8.135, 10.897, 11.386])
  diametery67 = np.array([0.066,0.277,0.574,1.116,1.535,2.503,3.232,4.41,5.238,6.164,8.456,10.08,11.475,13.759])
  diametery70 = np.array([0.078,0.185,0.606,1.018,1.586,2.333,3.319,4.084,6.014,7.452,9.267,11.191,12.741,15.676])
  diametery72 = np.array([0.082,0.332,0.827,1.364,2.176,3.212,4.15,5.28,6.873,8.39,10.553,12.508,14.661,16.67])
  diametery75 = np.array([0.091,0.241,0.589,1.025,1.636,2.048,3.286,4.327,7.082,8.825,10.612,12.665,14.062,16.889])
  diametery77 = np.array([0.054,0.368,0.548,0.952,1.543,2.378,3.296,3.734,4.84,6.135,7.42,9.3,11.047,12.727])
  diametery80 = np.array([0.063,0.253,0.561,1.07,1.544,2.346,3.136,4.072,5.456,6.131,7.897,9.383,11.376,12.601])
  
  diameter60 = np.polyfit(x, diametery60, 2)
  diameter62 = np.polyfit(x, diametery62, 2)
  diameter65 = np.polyfit(x, diametery65, 2)
  diameter67 = np.polyfit(x, diametery67, 2)
  diameter70 = np.polyfit(x, diametery70, 2)
  diameter72 = np.polyfit(x, diametery72, 2)
  diameter75 = np.polyfit(x, diametery75, 2)
  diameter77 = np.polyfit(x, diametery77, 2)
  diameter80 = np.polyfit(x, diametery80, 2)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, diametery60, "bo", label="60mm Diameter")
  plt.plot(x, diametery62, "go", label="62.5mm Diameter")
  plt.plot(x, diametery65, "ro", label="65mm Diameter")
  plt.plot(x, diametery67, "yo", label="67.5mm Diameter")
  plt.plot(x, diametery70, "o", label="70mm Diameter",color="Orange")
  plt.plot(x, diametery72, "co", label="72.5mm Diameter")
  plt.plot(x, diametery75, "mo", label="75mm Diameter")
  plt.plot(x, diametery77, "ko", label="77.5mm Diameter")
  plt.plot(x, diametery80, "o", label="80mm Diameter", color="GreenYellow")

  plt.plot(xp, np.polyval(diameter60, xp), "b-")
  plt.plot(xp, np.polyval(diameter62, xp), "g-")
  plt.plot(xp, np.polyval(diameter65, xp), "r-")
  plt.plot(xp, np.polyval(diameter67, xp), "y-")
  plt.plot(xp, np.polyval(diameter70, xp), "-", color="Orange")
  plt.plot(xp, np.polyval(diameter72, xp), "c-")
  plt.plot(xp, np.polyval(diameter75, xp), "m-")
  plt.plot(xp, np.polyval(diameter77, xp), "k-")
  plt.plot(xp, np.polyval(diameter80, xp), "-", color="GreenYellow")
  

  plt.title("Thrust vs. RPM", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800], fontsize=8)
  plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

  plt.legend(loc="upper left")

  plt.savefig("diametercomparison.png")
  plt.show()