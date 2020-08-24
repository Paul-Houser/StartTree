#!/bin/python3

import yaml

file_dict = {}
num_columns = 0

with open(r'./config.yaml') as file:
    file_dict = yaml.full_load(file)
    file.close()

num_columns = len(file_dict)

