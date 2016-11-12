#!/usr/bin/env python3

import os

from manage import *

clear()
create()

if not os.path.exists('data'):
    os.makedirs('data')

generate_sample('data')

add_dataset('Sample Dataset', 'data')
add_topicmodel('Sample Topic Model 1', 'data', 1)
add_topicmodel('Sample Topic Model 2', 'data', 1)
add_topicmodel('Sample Topic Model 3', 'data', 1)

add_dataset('Second Dataset', 'data')
add_topicmodel('Sample Topic Model 1', 'data', 2)
add_topicmodel('Sample Topic Model 2', 'data', 2)
