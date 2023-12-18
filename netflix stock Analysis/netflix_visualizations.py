##import piplite                    # I originally wrote this in JupyterLite. Only necessary if ran using that platform.
##await piplite.install('seaborn')

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


##### Read in Stock data for analysis
DJI = pd.read_csv('DJI.csv')
print(DJI.head())

NFLX = pd.read_csv('NFLX.csv')
print(NFLX.head())

ByQ = pd.read_csv('NFLX_daily_by_quarter.csv')
print(ByQ.head())


##### Rename 'Adj Close' column to 'Price' as this will be the data primarily used.
DJI.rename(columns={"Adj Close": "Price"}, inplace = True)
NFLX.rename(columns={"Adj Close": "Price"}, inplace = True)
ByQ.rename(columns={"Adj Close": "Price"}, inplace = True)


##### Create a violin chart showing the distribution of Netflix stock prices by quarter in 2017.
f, ax = plt.subplots(figsize = (15,20))
sns.violinplot(data = ByQ, x = 'Quarter', y = 'Price')
ax.set_title('Distribution of 2017 Netflix Stock Prices by Quarter')
ax.set_ylabel('Closing Stock Price')
ax.set_xlabel('Quarters in 2017')
plt.savefig('NetflixPricesByQuarterViolin.png')
plt.show()


##### Create a scatter plot for Netflix Shareholder earnings and Yahoo's projected earnings for each quarter in 2017 (Data taken from Yahoo Financial)
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]

plt.scatter(x_positions, earnings_actual, color = 'black', alpha = 0.5, marker = 'D')
plt.scatter(x_positions, earnings_estimate, color = 'green', alpha = 0.5, marker = 's')

plt.legend(['Actual Earnings', 'Yahoo Estimate'])
plt.xticks(x_positions, chart_labels)
plt.title('Earnings Per Share in Cents')

plt.savefig('EarningsPerShare.png')
plt.show()


##### Create and save a bar plot of Netflix stock earnings and revenue side-by-side for each quarter in 2017
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

## Create x locations for 'Revenue' graph (equation provided by codecademy)
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = .8 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]

## Create x locations for 'Earnings' graph (Also provided by codecademy)
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = .8 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]

## Create x location between the two for the location of ticks. (Provided by codecademy)
middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]

## Create bar plots of Netflix Stock revenue and earnings side by side for each quarter in 2017.
plt.bar(bars1_x, revenue_by_quarter)
plt.bar(bars2_x, earnings_by_quarter)
plt.xticks(middle_x, quarter_labels)
plt.ylabel('Billions of Dolars')
plt.legend(['Revenue', 'Earnings'])
plt.title('Netflix Earnings and Revenue by Quarter')

plt.savefig('EarningsRevenueBarChart.png')
plt.show()


##### Create two subplots of Netflix's stock prices and the DJI stock price for the beginning of each month in 2017 (for comparison)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig = plt.subplots(1,2, figsize = (12,6))

# Left plot Netflix
ax1 = plt.subplot(1,2,1)
ax1.plot(NFLX['Date'], NFLX['Price'], color = 'red', marker = 's')
ax1.set_title('Netfilx Stock Prices by Month', fontsize = 11)
ax1.set_xlabel('Month')
ax1.set_ylabel('Stock Price (USD)')
ax1.set_xticklabels(months)#this line of code causes an error that doesn't keep the graph from printing properly. I have discovered a workaround through some googling
                           #but it seems unnecessary for now and adds 2 lines. Can fix if needed.

# Right plot Dow Jones
ax2 = plt.subplot(1,2,2)
ax2.plot(DJI['Date'], DJI['Price'], color = 'purple', marker = 'D')
ax2.set_title('Dow Jones Industrial Stock Prices by Month', fontsize = 11)
ax2.set_xlabel('Month')
ax2.set_ylabel('Stock Price (USD)')
ax2.set_xticklabels(months) #this line of code causes an error that doesn't keep the graph from printing properly. I have discovered a workaround through some googling
                            #but it seems unnecessary for now and adds 2 lines. Can fix if needed.

plt.subplots_adjust(wspace=.3)
plt.savefig('NetflixDowPricesCompare.png')
plt.show()
