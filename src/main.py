import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
from scipy.interpolate import *
from numpy import *

SCOPE = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("../creds.json", SCOPE)
client = gspread.authorize(creds)

sheet = client.open("data toplama propeller").sheet1


def main():
    
  data = sheet.col_values(2)

  x = array([200,400,600,800,1000])
  y = array([0.6,0.52,0.49,0.41,0.35])

  #print(data)

  p1 = polyfit(x, y, 1)
  p2 = polyfit(x, y, 4)

  xp = linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, y, "o")
  plt.plot(xp, polyval(p1, xp), "r-")
  plt.plot(xp, polyval(p2, xp), "r-")

  plt.title("Propeller Data", fontsize=20)

  plt.show()

if __name__ == "__main__":
    main()
