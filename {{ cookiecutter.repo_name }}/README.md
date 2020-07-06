{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── experiments        <- keep experiment results
    │
    ├── experiments_cfg    <- config files to reproduce experiments
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── lib            <- useful code for the project
    │   │   │
    │   │   ├── data       <- data related code, creating dataset code chunks, or typical DL datasets
    │   │   │
    │   │   ├── losses
    │   │   │
    │   │   ├── models     <- model definition, together with train, fit, evaluate methods if it requires
    │   │   │                   specialized code
    │   │   ├── utils      <- general utility functions, summary writing, plotting and visualizations
    │   │                    
    │   │
    │   └── scripts        <- end-point scripts for different tasks
    │   │   └── consolidate_dataset.py
    │   │   └── train.py
    │   │   └── evaluate.py
    │   │
    │   └── test           <- scripts to help writing code and testing them, not the typical UnitTest but sth similar
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
