# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/drivendata/cookiecutter-data-science


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`. Run `make`
│			  for available commands
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                			<- Source code for use in this project.
│   │
│   ├── lib				<- The module that shares code for the project
│   │   ├── data			<- everything related to data e.g. augmentation,
│   │   │   │                              standardization, loading, ...
│   │   │   ├── __init__.py
│   │   │   └── data.py
│   │   ├── __init__.py
│   │   ├── models			<- model definition, train and predictions, summaries, logging, etc
│   │   │   ├── __init__.py
│   │   │   ├── predict_model.py
│   │   │   └── train_model.py
│   │   ├── utils
│   │   │   └── __init__.py
│   │   └── visualization		<- use it to evaluate and generate plots or useful visualization
│   │       ├── __init__.py
│   │       └── visualize.py
│   ├── scripts				<- scripts exposed to user, i.e. to be run from bash, i.e. with a main
│   │   └── _init_paths.py
│   └── test				<- test scripts which need not be maintained among experiments,
│       └── _init_paths.py		   or just some scripts for debugging
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt
