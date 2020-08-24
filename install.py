#!/bin/python3

import yaml
import os
from os.path import expanduser
from shutil import copyfile

# get home directory
home = expanduser("~")

# get config path
config_dir = home + '/.config/StartTree'
config_path = home + '/.config/StartTree/config.yaml'

# check if .config path exists
if not os.path.isdir(home + '/.config'):
    print("The directory '~/.config' does not exist, or you do not have permissions to edit it.")
    exit()

# check if .config/StartTree exists, create it and config if not
if not os.path.isdir(config_dir):
    print("Creating '~/.config/StartTree'...")
    os.mkdir(config_dir)
    print("Copying config.yaml")
    copyfile("./config.yaml", config_path)
    print("")

# check if config.yaml exists
if not os.path.exists(config_path):
    print("No config.yaml found in '~/.config/StartTree'")
    print("Copy the example config with:")
    print("\tcp ./config.yaml $HOME/.config/StartTree/config.yaml")
    print("or create your own in that directory.")
    exit()


file_dict = {}
num_columns = 0

with open(config_path, mode='r') as file:
    file_dict = yaml.full_load(file)
    file.close()

num_columns = len(file_dict)

