## BAKSA at SemEval-2020 Task 9: Bolstering CNN with Self-Attention for Sentiment Analysis of Code Mixed Text

This repository contains all code created as a part of the SemEval 2020 shared task. We participated in the task as a part of course CS698O under the mentorship of Prof. Ashutosh Modi.

The objective of the task was sentiment analysis of code mixed social media text. The dataset for the task was provided by the organizers of the task.

At the end of competition, we were ranked 5th out of 62 teams in Hinglish and 13th out of 29 teams in spanglish.


The approach we used was to the strengthen the prevailent CNN structure with a self attention model to better enable the classification of neutral tweets.

The instructions to run our code are given below :


### Getting Started

A step by step series of examples that tell you how to get the code running

Clone the repo

```
git clone https://github.com/keshav22bansal/BAKSA_IITK
```
create and start a virtual environment

```
virtualenv -p python3 env --no-site-packages

source env/bin/activate
```
Install the project dependencies:
```
sudo pip3 install -r requirements.txt

```

Then run
```
cd src
python main.py <dataset_name>

Example:
  python main.py hinglish
  python main.py spanglish
```
Note: We have shown our results on two datasets namely Hinglish and Spanglish
