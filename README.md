# spaCy and AWS comprehend named enitity identifiers
Python application which locates entities within csv datasets

About: This application seeks for csv files from a folder named as "datasets". Once it locates them it parses all datasets and then it merges them into a single Pandas dataframe. Main.py gets obtains this dataframe and it appends the text into a string list. This string list is appended onto a string list. This string ist is passed onto spaCy pipeline for entity extraction.

Prerequisites

Python (2.7 or 3.8) 

Pandas
spaCy (English version)
amazon comprehend
