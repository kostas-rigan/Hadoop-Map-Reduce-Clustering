#!/usr/bin/env python
"""mapper.py"""

import sys
import json
import numpy as np
import pandas as pd

with open('config.json', 'r') as f:
    json_d = json.load(f)
centers = [tuple(json_d['center1']), tuple(json_d['center2']), tuple(json_d['center3'])]

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
