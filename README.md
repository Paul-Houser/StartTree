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
  - [x] Allow setting the font size in the config
  - [ ] Install the update script into a `$PATH` directory

```yaml
font_size: 15
theme: void

tree_1:
  general:
    google: "https://www.google.com/"
    youtube: "https://www.youtube.com/"
  reddit:
    homepage: "https://www.reddit.com/"
    unixporn: "https://www.reddit.com/r/unixporn/"
```

# Themes

A variety of themes can be found in the `themes` directory. 

If one wishes to dynamically theme from `pywal`, they may select `pywal` as their chosen theme in `config.yaml`.
