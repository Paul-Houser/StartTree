# StartTree
A terminal-style home page replicating the tree command.

<p align="center">
  <img src="/StartTree.png", title="StartTree"/>
</p>

## TODO
- [x] Add screenshot to README.md
- [x] add install script
  - [ ] Should allow selection of search engine
  - [x] Should allow for multiple columns
  - [x] User makes a 'config.yaml' file that is parsed and translated into the HTML
  - [ ] Allow setting the font size in the config
  - [ ] Install the update script into a `$PATH` directory

```yaml
font_size: 15
theme: void

Tree_1:
  General:
    Google: "https://www.google.com/"
    Youtube: "https://www.youtube.com/"
  Reddit:
    Homepage: "https://www.reddit.com/"
    Unixporn: "https://www.reddit.com/r/unixporn/"
```

# Themes

A variety of themes can be found in the `themes` directory. 

If one wishes to dynamically theme from `pywal`, they may select `pywal` as their chosen theme in `config.yaml`.
