# data_analysis_S7

In this data analysis project in python, we had to use the "household power consumption" dataset from ICS. This dataset contains different power consumption measures, sampled every minute. It contains : Global active power, Global reactive power, Global Intensity, Voltage, Sub_metering_1, Sub_metering_2 and Sub_metering_3. It also contains 2 time related variables : Date, and Time.

Preprocessing :
First thing we did was replacing every nan values. As the data is sampled per minute, we replaced every missing minute by the mean value of that minute of the day. 
Then, we grouped Date and Time in one variable DataTime to use it as a DateTime index. That way, we can resample our data in other time frame : per hour, per day, per week, per month...
We saved this cleaned dataset as ; dataset-treated.csv
Last but not least, we used Web scrapping to retrieve data online to add a temperature variable in our dataset, as we had the following hypothethis : As electric consumption seems to be seasonal, as well as the temperature, they should be correlated  (positively or negatively, but more probably negatively). We managed to retrieve daily min and max temperatures from info-climat.fr, from 2006 to 2010. The data comes from a weather station in Paris, which is not so far from Sceaux, where the household that serves as the source of this dataset is. We saved this temperature dataset as temperatures.csv


Imports : 
For the vizualisation we will be using mostly pandas and matplotlib, but we also used vacances-scolaires-france from PyPi to retrieve the dates of every holiday in France in the right zone (C), so we can differentiate measures during a normal week (business days+weekends) a holiday, in some of our plots.
For the modeling, we used Tensorflow for the LSTM models, sklearn for the Random Forest models, and statsmodels for the AR/ARIMA/SARIMA models.

