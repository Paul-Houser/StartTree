#!/bin/python3

import yaml
import os
from os.path import expanduser
from shutil import copyfile
from bs4 import BeautifulSoup

# get home directory
home = expanduser("~")

# get config path
config_dir = home + '/.config/StartTree'
config_path = home + '/.config/StartTree/config.yaml'

# get cache path
cache_dir = home + '/.cache/StartTree'

def prettifyHTML():
    html = "<div><h1>Hello</h1></div>"
    soup = BeautifulSoup(html, 'html.parser')
    prettyHTML = print(soup.prettify())
    return prettyHTML

def setup():
    # check if .config path exists
    if not os.path.isdir(home + '/.config'):
        print("The directory '~/.config' does not exist, or you do not have permissions to edit it.")
        exit()

    if not os.path.isdir(home + '/.cache'):
        print("The directory '~/.cache' does not exist, or you do not have permissions to edit it.")
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

    # create directory structure in .cache
    if not os.path.isdir(cache_dir):
        print("Creating '" + cache_dir + "'...")
        os.mkdir(cache_dir)

        print("Creating '" + cache_dir + "/styles'")
        os.mkdir(cache_dir + '/styles')

    print("Creating style.css")
    copyfile("./skeletons/style.css", cache_dir + '/styles/style.css')

    print("Creating Hack.ttf")
    copyfile("./skeletons/Hack.ttf", cache_dir + '/styles/Hack.ttf')

def parse_yaml():
    with open(config_path, mode='r') as file:
        file_dict = yaml.full_load(file)
        file.close()

    return file_dict

def print_keys(dictionary):
    for key in dictionary:
        print(key)
        if isinstance(dictionary[key], dict):
            print_keys(dictionary[key])

def gen_list_indices(html_file, file_dict):
    for key in file_dict:
        print(key)

def gen_col_headers(html_file, file_dict):
    for key in file_dict:
        html_file.write("<li>\n")
        html_file.write("  <h1>" + key + "</h1>\n")
        html_file.write("  <ul>\n")

        # generate list indices
        gen_list_indices(html_file, file_dict)

        html_file.write("  </ul>\n")
        html_file.write("</li>\n")

def gen_columns(html_file, file_dict):
    for key in file_dict:
        html_file.write("<div class=\"column\">\n")
        html_file.write("  <div class=\"tree\">\n")
        html_file.write("    <h1>.</h1>\n")
        html_file.write("    <ul>\n")

        # generate the column headers
        gen_col_headers(html_file, file_dict[key])

        html_file.write("    </ul>\n")
        html_file.write("  </div>\n")
        html_file.write("</div>\n")


def gen_html(file_dict):
    print("Generating index.html...")

    # open files
    skeleton_html = open('./skeletons/index.html', 'r')
    cache_html = open(cache_dir + '/index.html', 'w')

    # copy skeleton_html to cache_html until Column Start comment
    lines = skeleton_html.readlines()
    for line in lines:
        if line == "<!-- Columns start -->\n":
            gen_columns(cache_html, file_dict)
        else:
            cache_html.write(line)

    # close files
    skeleton_html.close()
    cache_html.close()

    print("Done!")

def main():
    setup()
    file_dict = parse_yaml()
    gen_html(file_dict)

if __name__ == '__main__':
    main()
