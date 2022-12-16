import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

## Data set
address = 'C:/Users/Benjamin Piticaru/Documents/python projects/Python for Data Science Essential Training Part 2/Exercise Files/Data/groceries.csv'
data = pd.read_csv(address)

## Data Conversion
basket_sets = pd.get_dummies(data)
#basket_sets.head()

## Support Calculation
apriori(basket_sets, min_support=0.02)
## generates with name of columns for items purchased
apriori(basket_sets, min_support=0.02, use_colnames=True)

df = basket_sets
##  Changing the min_support
frequent_itemsets = apriori(basket_sets, min_support=0.002, use_colnames=True)
## adding a column with the number of items as well, calculated in the lambda function
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets

## filtering for itemset >=3
frequent_itemsets[frequent_itemsets['length'] >= 3]

## Generating Association Rules
##   Confidence
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
rules.head()

##   Lift
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head()

##   Lift and COnfidence
rules[(rules['lift'] >= 5) & (rules['confidence']>= 0.5)]
rules.head()
