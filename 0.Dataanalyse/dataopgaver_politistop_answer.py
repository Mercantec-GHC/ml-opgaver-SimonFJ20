from datetime import datetime
import random
from enum import Enum, auto
from typing import cast
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d = pd.read_csv('./Data/Police/police.csv')
# print(d.head())

# d = d[d["driver_gender"].any(lambda ) != None and d["violation"] != None and d["stop_outcome"] != None]
d = d[d["driver_gender"].notnull() & d["violation"].notnull() & d["stop_outcome"].notnull()]
d = cast(pd.DataFrame, d)

def date_str_to_date(datestr: str) -> datetime:
    year, month, date = [int(s) for s in datestr.split("-")]
    return datetime(year, month, date)

dates = d["stop_date"].map(date_str_to_date)
d["stop_date"] = dates
d["stop_year"] = [date.year for date in dates]
d["stop_month"] = [date.year for date in dates]

ages = 2021 - np.array(d["driver_age_raw"])
d["age"] = ages

intervals = [(i * 20, i * 20 + 20) for i in range(5)]
d = d.groupby(["age"])
# print(m)

