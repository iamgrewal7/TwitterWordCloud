# Creating Word from Twitter Data

## About
In the project I extracted 2000 tweets from Twitter, using Twitter API, into two equal sized datasets. First dataset contain random tweets while the second is the result when "COVID-19" is searched on Twitter.
Both the datasets were cleaned and compared using Venn Diagrams before creating the word clouds.

Link to the word cloud that I tweet - https://twitter.com/iamgrewal7/status/1267226701236334592?s=20

## Project Structure

1. `extract.py` holds code for extrating tweets from Twitter and storing them into csv or json files.
2. `*.csv` and `*.json` store tweets in respective format.
3. `process.ipynb` in the main code that load data into dataframe, cleans it, compare data sets and create a word cloud.
4. `setting.py` is used set authentication and logging settings.