from manage import *

clear()
create()

generate_sample_dataset('data')
generate_sample_topicmodel('data')

add_dataset('Sample Dataset', 'data')
add_topicmodel('Sample Topicmodel', 'data', 1)
