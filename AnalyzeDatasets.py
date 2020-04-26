import pandas as pd
import glob
import re

class AnalyzeDatasets():
    path = r'datasets'  # use your path
    all_files = glob.glob(path + "/*.csv")
    li = []
    for filename in all_files:
        read_csv = pd.read_csv(filename, index_col=None, sep='delimiter', header=None, encoding="utf-8", squeeze=True)
        li.append(read_csv)

    frame = pd.concat(li, axis=0, ignore_index=True)

