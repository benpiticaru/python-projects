import numpy as np
import pandas as pd
from datetime import date
import calendar
from itertools import cycle, islice



address = 'C:/Users/Benjamin Piticaru/Downloads/January - April Leading survey.csv'
survey_df = pd.read_csv(address)
survey_df = survey_df.drop('Timestamp', axis=1)

survey_df.columns = ['Name','email','phone','role','Zions Harp',
                    'Gospel Hymns','Hymns Zion','Celebration Book',
                    'Junior Hymnal', 'Camp Book','Dates off','Capacity','Groupchat']

## Changing Inputs from Yes/No and capacity to bool and 3,2,1 respecively
survey_df.replace(('Yes', 'No'), (True, False), inplace=True)
survey_df['Capacity'].replace(('regular (>3/month)', 'occasional (1-2/month)', 'reserve (0/month)'), (3, 2, 0), inplace=True)
survey_df.head()

## Creating the lists of Capacity per month
Leader_list = []
Piano_list = []

## The program multi_append(Str, num) produces a list with Str, n times.
def multi_append(name, n):
    l = []
    for i in range(n):
        l.append(name)
    return l

for i in range(len(survey_df)):
    if survey_df['role'][i] == 'Leader':
        Leader_list.extend(multi_append(survey_df['Name'][i], survey_df['Capacity'][i]))
    else:
        Piano_list.extend(multi_append(survey_df['Name'][i], survey_df['Capacity'][i]))

## Inputs the dates from January to April
timespan = 120
begin_date = '2023-01-01'
df = pd.DataFrame({'Start Date':pd.date_range(begin_date, periods=timespan),
                   'End Date':pd.date_range(begin_date, periods=timespan)})

## Filters out rows that are not wednesdays or Sundays
for index, row in df.iterrows():
    if row['Start Date'].weekday() == 6:
        continue
    elif row['Start Date'].weekday() == 2:
        continue
    else:
        df.drop(index, inplace=True)

## Creates Additional Sunday placement.
temp_df = []
for index, row in df.iterrows():
    if row['Start Date'].weekday() == 6:
        temp_df.extend([list(row)]*2)
    else:
        temp_df.append(list(row))

df = pd.DataFrame(temp_df, columns=df.columns)

## Implementing Sit/Stand format
def format(row):
    if row['Start Date'].weekday() == 6:
        return 'Sit'
    else:
        return    

df['format'] = df.apply(lambda row: format(row), axis=1)

if df.loc[0,'Start Date'].weekday() == 6:
    df.loc[0,'format'] = None

for i in range(3, len(df) - 1):
    if df.loc[i-2,'format'] != None:
        df.loc[i,'format'] = None
    elif df.loc[i-3,'format'] == 'Sit':
        df.loc[i,'format'] = 'Stand'
    else:
        continue

## Adding start and stop times
def start_time_of_day(row):
    if row['Start Date'].weekday() == 6:
        if row['format'] == None:
            return '4:40:00 PM'
        else:
            return '5:15:00 PM'
    else:
        return '7:30:00 PM'

def end_time_of_day(row):
    if row['Start Date'].weekday() == 6:
        if row['format'] == None:
            return '5:15:00 PM'
        else:
            return '5:45:00 PM'
    else:
        return '7:55:00 PM'

df['Start Time'] = df.apply(lambda row: start_time_of_day(row), axis=1)
df['End Time'] = df.apply(lambda row: end_time_of_day(row), axis=1)

## Adding Book used
book_list = ['Zions Harp','Celebration Hymnal',
'Gospel Hymns','Zions Harp','Gospel Hymns','Zions Harp',
'Zions Harp','Gospel Hymns','Gospel Hymns','Zions Harp',
'Hymns of Zion','Zions Harp','Zions Harp','Junior Hymnal',
'Gospel Hymns','Zions Harp','Gospel Hymns','Zions Harp',
'Zions Harp','Gospel Hymns','Gospel Hymns','Zions Harp',
'Camp Book','Zions Harp']

if df['Start Date'][0].weekday() == 2:
    book_list.insert(0,'Zions Harp')

df['Subject'] = list(islice(cycle(book_list), len(df)))

## Need to divide df into months to have stratified randomization

## Need to make a dataframe that holds dates that people can't lead (df with peoples names as columns and dates as 
#   indexes and binary values (yes no, true false))
#       will have to figure out a way to change input dates to numeric dates

## The function below takes a list and returns a random value from the list without replacing it.
def rd_wo_replacement(los):
    x = np.random.choice(los)
    for i in range(len(los)):
        if (los[i] == x):
            los.remove(los[i])
            return x

## How will I be able to fill the schedule while considering the dates that people cant play
## Make a df that has dates as index and columns as peoples names
## Have bool values for when they are available.
## randomly take from the list of capacity but check if that date is open to that name


## The following code takes the input of dates that an individual is not available and outs put a
## list in the proper format (YYY-MM-DD)

## Convert(str) takes in a string and returns a list of the string
##   broken up by a ','
def Convert(str):
    if type(str) == bool:
        return []
    if '-' in str:
        li = (str.replace(' ', ''))
        li = list(str.split(","))
        return li
    else:
        return []

dates_avail = pd.DataFrame(index=df['Start Date'],columns=(survey_df['Name'],))

for index, row in survey_df.iterrows():
    name = row['Name']
    los = Convert(row['Dates off'])
    for i in range(len(los)):
        dates_avail.loc[los[i],name] = False

## Still need to split the main dataframe and then populate it. This would work in a loop
##   and you save each dataframe?