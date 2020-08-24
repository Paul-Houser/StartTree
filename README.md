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

# Docker

In order to circumvent some restrictions on browsers for what is allowed as a "Home" and "New Tab" page, you can host StartTree as a lightweight `NGINX` server through `docker-compose`.

To set this up, one must have `docker` and `docker-compose` installed and configured. Then, go into the directory where you cloned `StartTree`, and run

```bash
cd docker
vim docker-compose.yaml # edit specifics to your liking
docker-compose -f docker-compose.yaml up -d
```

This will make the `NGINX` server persist across reboots. You can point your browser's new tab and home page to `localhost:p<port#>` and you should your startpage!

### NOTE: 

Currently, docker is unaware if a file changes on the fly (like generating a new colorscheme or adding new shortcuts), so you have to restart the container with

`docker-compose -f docker-compose.yaml restart <servicename>`
