## BAKSA at SemEval-2020 Task 9: Bolstering CNN with Self-Attention for Sentiment Analysis of Code Mixed Text

This repository contains all code created as a part of the SemEval 2020 shared task. We participated in the task as a part of course CS698O under the mentorship of Prof. Ashutosh Modi. The paper was accepted at Proceedings of the 14th International Workshop on Semantic Evaluation, find the pdf [here](https://arxiv.org/abs/2007.10819)

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
#### Create and start a virtual environment
##### Using virtualenv
```
virtualenv -p python3 env --no-site-packages

source env/bin/activate
```
#### Using conda
```
conda create -n env python=3.6

source activate env
```
#### Install the project dependencies:
```
pip3 install -r requirements.txt
```

### Running
```
cd src
python main.py <dataset_name>

Example:
  python main.py hinglish
  python main.py spanglish
```
Note: We have shown our results on two datasets namely Hinglish and Spanglish


## Citation
If our method is useful for your research, please consider citing:

```bash
  @inproceedings{baksa2020sentimix,
  title={BAKSA at SemEval-2020 Task 9: Bolstering CNN with Self-Attention for Sentiment Analysis of Code Mixed Text},
  author={Kumar, Ayush and
  Agarwal, Harsh and
  Bansal, Keshav and
  Modi, Ashutosh},
  booktitle = {Proceedings of the 14th International Workshop on Semantic
  Evaluation ({S}em{E}val-2020)},
  year = {2020},
  month = {December},
  address = {Barcelona, Spain},
  publisher = {Association for Computational Linguistics},
  }
```
