import numpy as np
import pandas as pd
from datetime import date
import calendar
from itertools import cycle, islice

## Things needed to add:
##    Need to add people who can both lead and play piano to both lists
##    Need to make it so when you call the program, you input the source file,
##      output folder, start date, etc.
##    Need to figure out how to split into modules and read documents where people
##      can change the books that they use in their specific churches

address = 'C:/Users/Benjamin Piticaru/Downloads/January - April Leading survey.csv'
survey_df = pd.read_csv(address)
survey_df = survey_df.drop('Timestamp', axis=1)

survey_df.columns = ['Name','email','phone','role','Zions Harp',
                    'Gospel Hymns','Hymns of Zion','Celebration Hymnal',
                    'Junior Hymnal', 'Camp Book','Dates off','Capacity','Groupchat']


## Changing Inputs from Yes/No and capacity to bool and 3,2,1 respecively
survey_df.replace(('Yes', 'No'), (True, False), inplace=True)

## Creating the lists of Capacity per month
Leader_list = []
Piano_list = []

## The program multi_append(Str, num) produces a list with Str, n times.
def multi_append(name, n):
    l = []
    for i in range(n):
        l.append(name)
    return l

## The program below creates a list of leaders/piano names * the number of times they are able to
##   play a month

for index, row in survey_df.iterrows():
    if row['role'] == 'Leader':
        Leader_list.extend(multi_append(row['Name'], row['Capacity']))
    else:
        Piano_list.extend(multi_append(row['Name'], row['Capacity']))

## Inputs the dates for 4 months, starting with start_month. 
##   Change this out for the input option month.
timespan = 120
start_month = '1'
begin_date = '2023-0d-01'
begin_date = begin_date.replace('d',start_month)

df = pd.DataFrame({'Start Date':pd.date_range(begin_date, periods=timespan),
                   'End Date':pd.date_range(begin_date, periods=timespan)})
dates_avail = pd.DataFrame(index=df['Start Date'],columns=(survey_df['Name']))

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

for index, row in df.iterrows():
    row['Start Date'] = str(row['Start Date'])[:10]
    row['End Date'] = str(row['End Date'])[:10]

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

## The function below takes a list and returns a random value from the list without replacing it.
def rm_from_lst(los,x):
    for i in range(len(los)):
        if (los[i] == x):
            los.remove(los[i])

## Convert(str) takes in a string and returns a list of the string
##   broken up by a ','
def Convert(s):
    if type(s) == float:
        return []
    if '-' in s:
        li = (s.replace(' ', ''))
        li = list(s.split(","))
        return li
    else:
        return []

books_df = survey_df.filter(['Zions Harp','Gospel Hymns','Hymns of Zion',
                            'Celebration Hymnal','Junior Hymnal', 'Camp Book'], axis=1)
books_df.index = survey_df['Name']
books_df.columns = ['Zions Harp','Gospel Hymns','Hymns of Zion','Celebration Hymnal','Junior Hymnal','Camp Book']

## The following code creates and formats the dates that people are available for.
##dates_avail = pd.DataFrame(index=df['Start Date'],columns=(survey_df['Name']))
dates_avail = dates_avail.applymap(lambda x: True)

for index, row in survey_df.iterrows():
    name = row['Name']
    los = Convert(row['Dates off'])
    for i in range(len(los)):
        dates_avail.loc[los[i],name] = False

## Creating the Leader and Pianist columns
df['Leader'] = list(range(len(df)))
df['Pianist'] = list(range(len(df)))

## The code below splits the main schedule into 4 schedules for each month
sched_1 = df[df['Start Date'].dt.strftime('%Y-%m') == '2023-01']
sched_2 = df[df['Start Date'].dt.strftime('%Y-%m') == '2023-02']
sched_3 = df[df['Start Date'].dt.strftime('%Y-%m') == '2023-03']
sched_4 = df[df['Start Date'].dt.strftime('%Y-%m') == '2023-04']

## need to replace from list if name is not chosen.
## Populates leaders

def fill_schedule(df):
    lol = Leader_list.copy()
    lop = Piano_list.copy()
    Old_leader = ''
    Old_pianist = ''
    for index, row in df.iterrows():
        leader = np.random.choice(lol)
        pianist = np.random.choice(lop)
        while ((books_df.loc[leader,row['Subject']] != True) | 
        (dates_avail.loc[row['Start Date'],leader] == False) | (Old_leader == leader)):
            leader = np.random.choice(lol)
        while ((books_df.loc[pianist,row['Subject']] != True) | (
            dates_avail.loc[row['Start Date'],pianist] == False) | (Old_pianist == pianist)):
            pianist = np.random.choice(lop)
        lol.remove(leader)
        lop.remove(pianist)
        df.loc[row['Leader'],'Leader'] = leader
        df.loc[row['Pianist'],'Pianist'] = pianist
        Old_leader = leader
        Old_pianist = pianist

fill_schedule(sched_1)
fill_schedule(sched_2)
fill_schedule(sched_3)
fill_schedule(sched_4)

## The code below converts the dataframes back to a single schedule
sched_1 = sched_1.append(sched_2,ignore_index=True)
sched_1 = sched_1.append(sched_3,ignore_index=True)
sched_1 = sched_1.append(sched_4,ignore_index=True)

final_df = sched_1.filter(['Subject','Start Date','End Date', 'Start Time','End Time'],axis=1)


## The following code writes the description column for the final df.
def write_description(row):
    string = 'Leader: {leader} | Pianist: {pianist} \n Format: {format}'.format(leader=row['Leader'],pianist=row['Pianist'],format=row['format'])
    return string

final_df['Description'] = sched_1.apply(lambda row: write_description(row), axis=1)

final_df.to_csv('Music_Schedule.csv')
