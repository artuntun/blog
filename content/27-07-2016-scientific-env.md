Title: Finding a Scientific Working Environment In Python
Date: 27-07-2016
Authors: Andy Mellor
Slug: scientific-env
Tags: Python, Docker, Conda
Category: General
Status: Published

<!-- PELICAN_BEGIN_SUMMARY -->

Reproducability is hard!

<!-- PELICAN_END_SUMMARY -->

# Finding the right workflow

####Issues
* Using multiple machines
* Using different operating systems
* Using different IDEs

# Solutions

## virtualenv

Not sure about this one

## Anaconda

conda env create

activate or source activate

## Docker

dockerfile

docker build .

docker run

notebook server, or interactive work.


# Conclusions

Lots of possibilities!
Remains an issue, but docker seems like the most powerful (but requires the most effort)
For the future, it would be great for research to include dockerfiles, data, and notebooks for reproducability.

Also, watch out for JupyterLab!


We might just be able to use markdown to be honest

```bash
sudo install docker
```

```bash
source activate
```

```python
import x
```

```
INSTALL:
    Requires
```



{% notebook d3.ipynb cells[1:3] %}

We'll generate a random Erdos-Reyni (ER) graph as a quick example, callable through the in-build Networkx function. 
ER graphs are generated by creating a set of $N$ nodes, 
and then for each potential node pairing, a coin is flipped and with probability $p$ and edge is formed. 
For small ER graphs it is likely (with probability $(1-p)^{(N-1)}$) that a node will have no edges which can be undesirable in some cases, 
hence we generate graphs untill we find one with a single connected component.
