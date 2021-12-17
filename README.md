# PYTHON FOR DATA ANALYSIS - HOUSEHOLD POWER CONSUMPTION

#### /!\ This README is a very short summary of the results of the project, the jupyter notebooks mentionned in it (the links) are the documents containing the code but also the in-depth interpretation of our results, please do not forget to have a quick look at them !

## Introduction (origin of the dataset, goal of the analysis and context):

#### In this data analysis project in python, we had to use the "household power consumption" dataset from ICS. This dataset contains different power consumption measures, sampled every minute. It contains : Global active power, Global reactive power, Global Intensity, Voltage, Sub_metering_1, Sub_metering_2 and Sub_metering_3. It also contains 2 time related variables : Date, and Time. The source is EDF, and the values correspond to the mean value of a minute. I contains values from december 2006 to december 2010, containing around 2 million rows.

#### *source:* [Individual household electric power consumption Data Set, ICS](https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption)
 
---

#### The analysis has 2 goals : Solve a specific issue and display possible other usage of the dataset. 

#### The context is the following, we have to use the data of the power consumption of one household to be able to predict its consumption in the future. If it is possible, it will be highly useful for 2 reasons. First, for the household itself. For a household that possesses a local energy production system like solar panels or wind turbines, by predicting its future consumption, we can crossmatch the results with weather condition or other factors (or even only the consumption itself) to determine if they can afford to sell a part of the electricity they produce, without selling more than what they will use, and how much to sell. It will help them avoid to sell energy they would have used and having to buy energy from their supplier again, loosing their rentability or even rendering it negative. On the other side, if the supplier can forecast the power consumption of the households in its power grid, they can adapt their production in advance, therefor lowering costs of unnecessary production and avoiding shortage.

#### Also, we will have a look in specific time frames of our data, to see if we can predict/guess a family's habits just by looking at their consumption, which could for example be a way to target them with appropriate adversiting at the appropriate time, or to automate the start and stop of certain appliances to improve the overall power consumption of the household. It would also suggest the need for the supplier to improve the security/privacy of this data to not accidentaly give informations about its consumers.



## Preprocessing :

#### In the preprocessing, we cleaned the dataset, reformated certain variables and replaced missing values. We also added daily temperature data using web scrapping, and then saved the new datasets in a csv format, easily readable in the rest of our notebooks. 

#### *More details in the notebook:* [data_preprocessing.ipynb](https://github.com/Theodlz/data_analysis_S7/blob/main/pre_processing/data_preprocessing.ipynb)

## Imports :

#### For the vizualisation we will be using mostly pandas and matplotlib, but we also used vacances-scolaires-france from PyPi to retrieve the dates of every holiday in France in the right zone (C), so we can differentiate measures during a normal week (business days+weekends) a holiday, in some of our plots.
#### For the modeling, we used Tensorflow for the LSTM models, scikit-learn for the Random Forest models, and statsmodels for the AR/ARIMA/SARIMA models.


## Data Vizualisation:

* In the first part our the data visualization, we started by visualizing all of our variables in different time resamplings (day, month, year...). It allowed us to see which variables are of interest adn which of them show anomalies/irregularities, which variables are correlated to the one we want to predict (Global Active Power), and how their pourcentage of correlation changes depending on the time sampling. 

* In the second part of our analysis, a focus on the global active power and a series of required graphs to apply time series models accordingly. It allowed us to observe seasonality in the data, as well as determine the correlation between lagged variables and the current/future values. This analysis showed us that it is theorically possible to predict variables in the present or future using past data, as well as which parameters to use for some of our models (AR, ARIMA, SARIMA).

* The last part of our Data Visualization focuses not on the modeling, but on a different possible approach to this dataset : observing the evolution of values at smaller time scales to discover patterns, habits and usages of the member of the household, aka can we "spy" on someones daily life/routine just by looking at its electrical consumption ! If it is, a totally different project than ours could be done using models that uses the power consumption to analyse a family's routine and tell what they are doing at a given time. Turns out that it does seem to be possible, which we will see through in depth graphical interpretation over specific time periods.

#### *More details in the notebook:* [DATA_VISUALIZATION.ipynb](https://github.com/Theodlz/data_analysis_S7/blob/main/DATA_VISUALIZATION.ipynb)

## Modeling:

* The first type of models we tried are auto regressive models, such as AR, ARIMA and SARIMA. Those models give us weekly forecasting of values using only a given timestamp as an input, but no past data, as past data is only necessary for the training phase in those models. The best and only accurate one is the SARIMA model, that encapsulates the seasonality of the data from this dataset.

#### *More details in the notebook:* [AUTO_REGRESSION.ipynb](https://github.com/Theodlz/data_analysis_S7/blob/main/AUTO_REGRESSION.ipynb)

* For short term forecasting (minutes/hours/days) we developped LSTM models using Keras. To be able to learn and predict correctly, an additional processing on the dataset was necessary: the addition of 3 columns, holding the time of the day (Hour), the day of the week (Day), and the month of the year (Month).

#### *More details in the notebook:* [LSTM.ipynb](https://github.com/Theodlz/data_analysis_S7/blob/main/LSTM.ipynb)

* We also created Random Forest models for short term forecasting. In addition to being able to predict the power consumption one step ahead, like the LSTM model, we implemented multistep forecasting using the Random Forrest models. It makes possible the prediction of several time steps ahead, from only one data point input. We can thus for example predict the consumption of a whole day, given 1 input of the early morning's consumption.

#### *More details in the notebook:* [RANDOM_FOREST_REGRESSION.ipynb](https://github.com/Theodlz/data_analysis_S7/blob/main/RANDOM_FOREST_REGRESSION.ipynb)

#### We created a simple web interface using Flask, for the use of the Random Forest model for one step prediction. Here is a preview:
![Flask Interface Preview](https://github.com/Theodlz/data_analysis_S7/blob/main/Flask/interface_web_flask.PNG)

## Conclusion: What did we learn ?

#### About the problematic itself, we confirmed that it is possible to predict the electric consumption using different models in different time frames, both short term and long term, which solves both issues mentionned in the introduction. The modeling part of the project is a success and has solid bases and justification thanks to our time series analysis. Moreover, we observed that it is possible to look at the electrical consumption in detail to display hypothetic behavior of the members of an household.


