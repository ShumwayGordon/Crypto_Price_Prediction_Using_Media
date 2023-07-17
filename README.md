# Crypto Price Prediction Using information From Media

Our purpose is training a model that predicts the price of cryptocurrencies based on social media data the following steps were performed to achieve the goal
![Course20project20defense pdf (2)_page-0002](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/b500be11-8cc5-4d0c-894e-fd54d41238b4)

## Data Collecting

First step was data collecting. We use four sources: Yahoo finance, Google Trends, Reddit, Twitter.
![Course20project20defense pdf (2)_page-0004](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/43831093-a474-49dd-9a64-5b4552fec428)

We used the yfinance library to get the historical price of currencies from September 2014 to June 2022. This library returns data in the form of a pandas dataframe or dataseries. We have collected the open, high, low and close prices, volume, dividends and stock splits for 36 currencies.
![Course20project20defense pdf (2)_page-0005](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/6b2de197-fd1b-4d97-9730-ee4c6bc7a855)

Google is far and away the world’s most popular search engine as it accounts for 74.52% of all internet searches. This means that Google search data can provide incredible insights into what the world is interested in, and how interested in any given topic it is. Google makes this data available through ”Google Trends”. Google Trends data provides information on how popular given search terms are relative to other search terms at any given time. This website allows users to search for popularity of a particular topic through the Search Volume Index (SVI). To collect data from Google Trends we use PyTrends API is an Unofficial API that allows a simple interface for automating downloading of reports from Google Trends. 
![Course20project20defense pdf (2)_page-0006](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/5e525ed1-80e3-4f1f-ade1-36fb7082d4c4)

First of all it was important to find TOP-4 related queries for each coin to analyze more accurate statistics (the result is demonstrated on slide).
![Course20project20defense pdf (2)_page-0007](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/88061771-8147-4a09-8cc5-8a78e74f64dc)

The main problem was that SVI data obtained by searching over 90 days will be divided by week rather than by day. And to obtain the dataset on a daily basis, we apply the processing method of Erik Johansson.
![Course20project20defense pdf (2)_page-0008](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/95b1ab43-546e-4eb3-8999-ef8ae6e6dcfe)

Collecting data by day and then combining them into an array.
![Course20project20defense pdf (2)_page-0009](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/8d6df0c8-d3a6-4152-a4ae-70378d85eea3)

Collecting data by week in the same period of time.
![Course20project20defense pdf (2)_page-0010](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/15cdd437-2c0a-4e58-a9ea-0bed23d670b3)

Adjusting daily data based on weekly data. The adjustment factor is calculated by dividing the weekly SVI by daily SVI. 
![Course20project20defense pdf (2)_page-0011](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/0a0bbce7-dff2-4899-a6f4-c095b0cefdb6)

Multiplying the SVIs of the remaining days with the adjustment factor. 
![Course20project20defense pdf (2)_page-0012](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/be14a5da-8df4-4200-b549-1b2af2019000)

After completing all the steps, we get the daily dynamics of SVI.
![Course20project20defense pdf (2)_page-0013](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/2dc942b2-482c-4f41-994a-08e4dc78b1da)

As another data source reddit platform was used. It has its official API and python wrapper for it. Also some additional pushshift was used. Pushshift gives information from its own archive, it has more advanced search parameters and in the most cases it worked faster than original API. We parsed 10 posts per day with highest score for each considered coin. 
![Course20project20defense pdf (2)_page-0014](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/b5cdc6be-5637-4c4d-8b76-3b2cdcf751be)

As a feature we took mean number of comments, mean number of scores and features we got after applying nlp transformer from spacy library on posts titles. 
![Course20project20defense pdf (2)_page-0015](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/19bfb89b-ce0b-405a-bf51-75e5c1fa5649)

When we started to work with twitter, the first problem arosed - currently twitter does not provide access to the API. Therefore, a third-party Twint library was used, since it allows to collect twitter data without an API.
![Course20project20defense pdf (2)_page-0016](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/a2f8ed49-1128-4db3-9802-481365f01712)

Twint itself provides such tools for search configuration as: 
- searching by keyword 
- filtering by interactions and date 
- setting the required number of tweets 

![Course20project20defense pdf (2)_page-0017](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/ae988a86-6c41-4aa2-8844-7374b07228aa)

However, twint also had significant drawbacks. For example, searching with the configuration unchanged could result in a different number of tweets. Also, after some time of continuously parsing tweets, twitter blocked the guest token used to access the data. Therefore, the Twitter data collection algorithm was built in the form shown in the diagram on the slide. 
![Course20project20defense pdf (2)_page-0018](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/1eec61bb-dfd9-4b99-ae8a-d4d7661e1801)

## Features from Twitter Data

Calculated some statistics features based on collected tweets
![Course20project20defense pdf (2)_page-0019](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/8ed42a1a-5a0e-4913-93a7-c7ea6c8cb089)

Used interactivity metric from paper (Hao V.M. et al., 2019. Predicting cryptocurrency price movements based on Social Media)
![Course20project20defense pdf (2)_page-0020](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/6dac2fd6-4ecd-4612-8a3f-63dca1d23dfb)

Also computed NLP sentiments metrics using TextBlob 
![Course20project20defense pdf (2)_page-0021](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/8026bacb-d5b7-4b9a-b823-eb5de82492c3)

And finally used fear/greed index of crypto market
![Course20project20defense pdf (2)_page-0022](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/db841d1d-64f0-4680-a8fa-b9caa09a4841)


## Correlation analysis

We performed Сorrelation analysis for BTC-USD features by Spearman's Rank-Order Correlation. On the heatmap we can see the day_likes, day_replies, mean_likes, mean_replies,adj, adj_svi, adj_svi_norm features have the highest correlation with the closing price. 
![Course20project20defense pdf (2)_page-0024](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/ff97657a-6a28-41b3-aeee-7e452eb98500)

On the example of the dynamics of changes in bitcoin and adj _svi, we see how these features correlate with each other
![Course20project20defense pdf (2)_page-0025](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/7554062a-e44d-4a09-8416-a5de13f08f1c)


## Training models for price forecasting

In training phase we loaded all the data from HDFS, merged it together, used last days data as a features, splitted dataset into train and test subsets and normalized based on training part. We trained Linear Regression and Random Forest Regressor models from pyspark module and make predictions on test subset. All results we saved into HDFS. 
![Course20project20defense pdf (2)_page-0027](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/0a4d7b05-c581-4bdf-b78e-be7c796fdb72)

The slide shows the results of evaluating the work of models trained on different coins by mean absolute error. Here you can see the effect of adding media data during training for different models and coins. 
Analysis of the results showed that 
1) aave, icp, zil combined with LinearRegression gave the best result with media 
2) bnb, doge, lrc, ltc, zil in combination with Random Forest Regressor gave the best result with media 
3) in the end, 22% of model-currency pairs performed better when using media, and for these pairs, on average, the result (MAE) improved by 15% 

![Course20project20defense pdf (2)_page-0028](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/c275652a-5480-4a4c-ae93-c2b17752393c)

The chart on the slide shows the target and predicted values for AAVE-USD obtained by the two models. As mentioned earlier, linear regression with media data for the AAVE-USD coin showed one of the best results.
![Course20project20defense pdf (2)_page-0029](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/1965a03a-af53-4b98-b644-476ac58069ca)

Our current inference pipeline is consists of data loading, forecasting and predictions delivery parts. While working with dedicated cluster we faced few difficulties: 
1) Internet absence, so we needed to manually parse data and put it into the HDFS 
2) Absence of some programming libraries, so at the current stage predictions delivery represents python notebook output
![Course20project20defense pdf (2)_page-0030](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/1b7e6573-64bc-4a59-b769-10038ee47769)

## Materials
![Course20project20defense pdf (2)_page-0034](https://github.com/ShumwayGordon/Crypto_Price_Prediction_Using_Media/assets/33491221/53099b1c-d3f4-4bb6-8c61-b490a99d3a3a)

