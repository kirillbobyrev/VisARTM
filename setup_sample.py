#!/usr/bin/env python3

import os

from manage import *

clear()
create()

if not os.path.exists('data'):
        os.makedirs('data')

generate_sample('data')

add_dataset('Sample Dataset', 'data')
add_topicmodel('Sample Topicmodel', 'data', 1)
add_topicmodel('Sample Topicmodew', 'data', 1)
add_topicmodel('Sample Topicmodew', 'data', 1)

add_dataset('Second Dataset', 'data')
add_topicmodel('Sample Topicmoder', 'data', 2)
add_topicmodel('Sample Topicmodeq', 'data', 2)
