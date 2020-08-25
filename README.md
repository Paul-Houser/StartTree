# StartTree
A terminal-style home page replicating the tree command.

<p align="center">
  <img src="/images/StartTree.png", title="StartTree"/>
</p>

<div align="center">
  <h1>
    <a href="https://gideonwolfe.com/">
        <img style="vertical-align:middle" src="/images/forest.png", width="400", />
    </a>
      <span style=""> 
        <img style="vertical-align:middle" src="/images/void.png", width="400", />
        </a>
      </span>
  </h1>
</div>

# Usage
## Installation
To install StartTree for the first time, run the following commands:  
(Note: If the `~/.config/StartTree` directory already exists, `init.py` will not execute to prevent accidentally overwriting a custom config. )
```
git clone https://github.com/Paul-Houser/StartTree.git
cd StartTree
./init.py
./generate.py
```
This will create the directory `~/.config/StartTree` containing the default `config.yaml`, as well as generate the html/css, which you can view by pointing your browser at `$HOME/.cache/StartTree/index.html`.

## Config
The config should be placed in `~/.config/StartTree/config.yaml`

## Updating the HTML
To re-generate the html/css after editing the config, navigate to the `StartTree` directory and execute `./generate.py`.

# Example Config
```yaml
font_size: 22 # specify font size
theme: void # specify the name of a theme in the themes/ directory, or use 'pywal'
tree_1: # each column should be named 'tree_X' where X is unique for each tree.
  general: # Header name
    github: "https://www.github.com/" # Link-text: url
    gmail: "https://mail.google.com/"
  reddit:
    # the following is an example of naming a link something with a space,
    # or containing characters that cannot be in a yaml variable name.
    frontpage: 
      - "https://www.reddit.com/"
      - "front page" # 
    unixporn: "https://www.reddit.com/r/unixporn/"
tree_2:
  other:
    archwiki: 
      - "https://archlinux.org/"
      - "arch wiki"
    hulu: "https://www.hulu.com/"
    netflix: "https://www.netflix.com/"
    youtube: "https://www.youtube.com/"
```

# Themes

A variety of themes can be found in the `themes` directory. 

If one wishes to dynamically theme from `pywal`, they may select `pywal` as their chosen theme in `config.yaml`.
