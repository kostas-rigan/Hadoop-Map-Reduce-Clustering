#!/usr/bin/env python
"""reducer.py"""

import sys
import pandas as pd


def print_centers(centers: pd.DataFrame):
    x = centers.to_string(header=False,
                  index=False,
                  index_names=False).split('\n')
    vals = [','.join(ele.split()) for ele in x]
    print('\n'.join(vals), end='')


for line in sys.stdin:
    input_file = line.replace('\n', '')

data = pd.read_csv(input_file)
new_centers = data.groupby('closest').mean()

print_centers(new_centers)
