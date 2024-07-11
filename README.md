<!-- Required extensions: pymdownx.betterem, pymdownx.tilde, pymdownx.emoji, pymdownx.tasklist, pymdownx.superfences -->

[comment]: <> (This is a comment, it will not be included)

# Project Description

## Subsection Project Description

In our paper [Beyond timestamps: Integrating implicit timing information into digital forensic timelines](https://doi.org/10.1016/j.fsidi.2024.301755) we describe how to integrate implicit timing information into digital forensic timelining.
This project contains the implementation to our paper.
Thus, it may be beneficial to read our paper in order to understand the core concepts such as "implicit timing information", "time domain" or "time domain entry" before trying out the tool itself.


The core of our implementation is the database schema, in which we modelled our concepts for TypeDB. We added a Python script for inserting data from a .tsv file together with some example data and some example queries. These queries can either be ran directly on the database (e.g. using TypeDBStudio as GUI) or you can use our utility scripts for running automatized queries.

You can find the queries in the directory "Utility_Scripts/Queries", the data in "Utility_Scripts/Example_Data" and the utility scripts in "Utility_Scripts/"


## Installation

To use our tooling, you need to install TypeDB, the database we base our tooling on. You can find instructions to install TypeDB Core here: [https://typedb.com/docs/home/install/core](https://typedb.com/docs/home/install/core)

Note that we used an installation via the packet manager, so if you want to use Docker, you probably need to adapt our scripts.

To use our tooling such as the ingest module you also need to install Python - we're using Python 3.10, but other versions may work as well. Additionally you need to install the Python packages in requirements.txt, e.g., using the following command:

```console
foo@bar:~$ pip install -r requirements.txt
```

There are two ways of analyzing the data in the database: either using an automatized script such as our Utility Scripts or querying the data directly, e.g. using TypeDB Studio as GUI. This software is developed by Vaticle to be used for TypeDB, offering not only an editor for the queries and showing their answers. One key feature is its capability to not only show a machine-readable answer, but also to offer a graph-view visualization of the answer. You find a explanation of how to install TypeDB Studio here: [https://typedb.com/docs/manual/console](https://typedb.com/docs/manual/console)

## How to Use our Tooling

### Setup the Database

To set up the database, we recommend running our utility script create_database.py using the folllowing command:

```console
foo@bar:~$ python3 Utility_Scripts/create_database.py
```

### Insert Data

If you want to directly insert data from a tsv as in our paper, you should use the ingest module. It can be found as ingest_module.py in the root directory offers options as explained when running --help.

For our example cases, you can choose one of the following commands:

```console
foo@bar:~$ python3 ingest_module.py "Utility_Scripts/Example_Data/Case_Study_1_FAT_Data_with_Time_Manipulation.tsv" 5=datetime 10=long 12=long -c 5,10,12
```

```console
foo@bar:~$ python3 ingest_module.py "Utility_Scripts/Example_Data/Precedence_Example.tsv" 1=datetime 2=datetime -p "1<2" -t firefox
```

We recommend inserting only one file once as otherwise undefined behaviour may occur and plan to add an utility script in near future: it should guide the user through the process of choosing the correct parameters in a dialogue.

### Analyze the data
To use the database, this repository offers two options: Using them in automatized Python scripts (our utility scripts) or directly querying the database. You will find each way described in one of the following subsections.


#### Utility Scripts
Currently, we're providing one utility script that detects inconsistencies. It can be run using the following command:

```console
foo@bar:~$ python3 Utility_Scripts/detect_inconsistency.py
```

We will add some more utility scripts in near future.

#### Query the Database directly 

To query the database you can either directly use TypeDB Console or TypeDB Studio. The former is documented under [https://typedb.com/docs/manual/console](https://typedb.com/docs/manual/console) while the question of how to use the later is explained under [https://typedb.com/docs/manual/studio](https://typedb.com/docs/manual/studio).

In each case, you need to use the database "Hypertimelining_III" and run a read-query with inference turned on. For those queries, you can either stick to our example queries in "Utility_Scripts/Queries" or write new queries in the database language TypeQL as described in [https://typedb.com/docs/typeql/overview}(https://typedb.com/docs/typeql/overview).


## Paper Reference
Dreier, L. M., Vanini, C., Hargreaves, C. J., Breitinger, F., & Freiling, F. (2024). Beyond timestamps: Integrating implicit timing information into digital forensic timelines. Forensic Science International: Digital Investigation, 49, doi: https://doi.org/10.1016/j.fsidi.2024.301755, url: https://www.sciencedirect.com/science/article/pii/S266628172400074X.


