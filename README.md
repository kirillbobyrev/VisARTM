# VisARTM

VisARTM is intended to become a successor of
[tm_navigator](https://github.com/omtcyf0/tm_navigator), a tool for visualizing
and assessing Topic Models primarily built using
[BigARTM](https://github.com/bigartm/bigartm) - fast and scalable library
for Topic Modelling.


## Installation and setup

VisARTM uses Python 3. While VisARTM is likely to work with Python 2, it is not
guaranteed.

`pip install -r requirements.txt` before using VisARTM. VisARTM requiers fairly
recent `flask` and `flask_sqlalchemy`.

## Data format in VisARTM

All files required by VisARTM should be provided in `.csv` format. See columns
and sample values for each input file below.

### Files related to dataset

#### document.csv

id|abstract|content
---|---|---
0|document-0|abstact-0|document-0-content
1|document-1|abstact-1|<h1>Header</h1>document-1-content

#### term.csv

id|text
---|---
0|milk
1|Python

#### document_similarity.csv

document_l_id|document_r_id|similarity
---|---|---
0|1|0.5
0|2|0.2

#### term_similarity.csv

term_l_id|term_r_id|similarity
---|---|---
0|1|0.5
0|2|0.6

#### document_term.csv

document_id|term_id|count
---|---|---
0|0|100
0|1|0

### Files related to topic model

#### topic.csv

id|title|probability|is_background
---|---|---|---
0|Topic 0|0.95|1
1|Topic 1|0.2|0

#### topic_similarity.csv

topic_l_id|topic_r_id|similarity
---|---|---
0|1|0.22
0|2|0.6

#### document_topic.csv

document_id|topic_id|prob_dt|prob_td
---|---|---|---
0|0|0.22|0.6
0|1|0.61|0.3

#### topic_term.csv

topic_id|term_id|prob_wt|prob_tw
---|---|---|---
0|0|0.22|0.6
0|1|0.4|0.2

## Loading data into VisARTM

To generate some random data and see its visualization use `./setup_sample.py`.
This script generates some random data, writes everything to `data` subfolder
and adds generated data to VisARTM database.

Generating VisARTM-compatible models from BigARTM models would be supported in
the future.

To load your custom model into VisARTM do the following:

0. Put data files in appropriate format into a folder.
1. Call `clear()` and `create()` to ensure that project database is cleared
from everything.
2. Call following Python functions from `manage.py`:
  * `add_dataset('Your Dataset Name', 'path_to_dataset')` - this creates
    dataset-related entries in the database and loads data.
  * `add_topic_model('Your Topic Model name', 'data', created_dataset_id)`
    where `created_dataset_id` is the id of added dataset returned from
    previous point
3. Good job! Now you're all set. Do `python3 serve.py` to see the loaded model
and begin assessment.
