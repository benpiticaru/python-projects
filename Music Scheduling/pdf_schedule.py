import numpy as np
import pandas as pd
from datetime import date
import calendar

## make_pdf(df) takes the shedule dataframe and outputs a new dataframe that is the pdf version of the schedule.
def make_pdf(df):
    new_df = pd.DataFrame(np.arange(216).reshape(18,12))
    i = 0
    for index, row in df.iterrows():
        if row['Start Date'].weekday() == 6:
            if row['Start Time'] == '4:40:00pm':
                new_df.iloc[1,i] = row['Leader']
                new_df.iloc[2,i] = row['Pianist']
            else:
                new_df.iloc[0,i] = row['Start Date']
                new_df.iloc[3,i] = row['Leader']
                new_df.iloc[4,i] = row['Pianist']
                new_df.iloc[5,i] = row['format']
                new_df.iloc[6,i] = row['Subject']
        else:
            new_df.iloc[8,i] = row['Start Date']
            new_df.iloc[9,i] = row['Leader']
            new_df.iloc[10,i] = row['Pianist']
            new_df.iloc[11,i] = row['Subject']
            i += 1
    return new_df
