#!/usr/bin/env python
"""mapper.py"""

__authors__ = 'Nikolaos Nikolaidis and Konstantinos Riganas'

import sys
import json
import numpy as np
import pandas as pd

# Load the centers
centers = []
with open('temp/centers.txt', 'r') as f:
    for line in f.readlines():
        xy = line.split(',')
        x = float(xy[0])
        y = float(xy[1])
        centers.append((x, y))

points = pd.read_csv('data.txt')
col_to_center = {}
for pos, center in enumerate(centers):
    col_name = f'dist{pos+1}'
    col_to_center[col_name] = pos
    points[col_name] =np.sqrt(np.square(points['x'] - center[0]) + np.square(points['y'] - center[1]))
points['closest'] = points.iloc[:, 2:].idxmin(1)
points['closest'] = points.loc[:, 'closest'].map(col_to_center)
file = 'temp/temp_points_cluster.txt'
points.loc[:, ['x', 'y', 'closest']].to_csv(file, sep=',', index=False)
print(file, end='')
