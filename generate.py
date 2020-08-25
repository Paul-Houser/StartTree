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

def prettifyHTML(html):
    soup = BeautifulSoup(html, 'html.parser')
    prettyHTML = soup.prettify()
    return prettyHTML

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
        value = file_dict[key]
        print(key + "->" + str(value))
        if not isinstance(value, list):
            html_file.write("<li><a href=\"" + value + "\">" + key + "</a></li>")
        else:
            html_file.write("<li><a href=\"" + value[0] + "\">" + value[1] + "</a></li>")

def gen_col_headers(html_file, file_dict):
    for key in file_dict:
        html_file.write("<li>\n")
        html_file.write("  <h1>" + key + "</h1>\n")
        html_file.write("  <ul>\n")

        # generate list indices
        gen_list_indices(html_file, file_dict[key])

        html_file.write("  </ul>\n")
        html_file.write("</li>\n")

def gen_columns(html_file, file_dict):
    for key in file_dict:
        if key.split("_")[0] == "tree":
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
    cache_html = open(cache_dir + '/index.html', 'w+')

    # copy skeleton_html to cache_html until Column Start comment
    lines = skeleton_html.readlines()
    for line in lines:
        if line == "<!-- Columns start -->\n":
            gen_columns(cache_html, file_dict)
        else:
            cache_html.write(line)

    #  prettify
    cache_html.seek(0)
    pretty_string = cache_html.read()
    pretty_string = prettifyHTML(pretty_string)
    cache_html.close()
    cache_html = open(cache_dir + '/index.html', 'w')
    cache_html.write(pretty_string)

    # close files
    skeleton_html.close()
    cache_html.close()

    print("Done!")

def gen_style(file_dict):
    skeleton_style = open('./skeletons/style.css', 'r')
    cache_style = open(cache_dir + '/styles/style.css', 'w')

    # find style attributes in file_dict
    font_size = 20
    theme = "void"
    for key in file_dict:
        if key == "font_size":
            font_size = file_dict[key]
        if key == "theme":
            theme = file_dict[key]

    if theme == "pywal":
        theme = home + '/.cache/wal/colors.css'
    else:
        theme = './themes/' + theme + '.css'

    copyfile(theme, home + '/.cache/StartTree/styles/colors.css')

    cache_style.write("@import url('./colors.css');\n")

    lines = skeleton_style.readlines()
    for line in lines:
        if line == "/* font-size */\n":
            cache_style.write("font-size: " + str(font_size) + "px;\n")
        else:
            cache_style.write(line)

def main():
    file_dict = parse_yaml()
    gen_style(file_dict)
    gen_html(file_dict)

if __name__ == '__main__':
    main()
