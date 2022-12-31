import numpy as np
import pandas as pd

grade_book = pd.read_csv('C:/Users/Benjamin Piticaru/Downloads/BIOL 309 - Fall 2022_GradesExport_2022-12-21-21-56.csv')
exam_book = pd.read_csv('C:/Users/Benjamin Piticaru/Downloads/BIOL-309 for grades.csv')
exam_book.columns = ['Student ID','Last Name','First Name','Grade'] 

grade_book.rename(columns={'OrgDefinedId':'Student ID'}, inplace=True)
grade_book.index = grade_book['Student ID']
exam_book.index = exam_book['Student ID']

df = grade_book['Student ID']

## The code below adds exam grade to exam book
for index1, row1 in exam_book.iterrows():
    row1['Student ID'] = ''.join(('#',str(row1['Student ID'])))
    for index2, row2 in grade_book.iterrows():
        if str(row1['Student ID']) in str(row2['Student ID']):
            grade_book.loc[index2,'Final exam Points Grade <Numeric MaxPoints:87 Weight:50>'] = row1['Grade']
        else:
            continue

grade_book.to_csv('out4.csv')
