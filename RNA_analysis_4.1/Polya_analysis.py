import numpy as np
import pandas as pd

address = 'C:/Users/Benjamin Piticaru/Desktop/Masters/polya_results.tsv'
data = pd.read_csv(address, sep='\t')
data.columns = ['readname','contig','position','leader_start','adapter_start','polya_start','transcript_start','read_rate','polya_length','qc_tag']

## Subsetting data to only contain polya_length and contigs.
polya_data = data[['contig','polya_length']]
data2 = pd.DataFrame(columns=['contig','Avg','SD'])

## Removing values that are less than 0.
polya_data = polya_data.loc[polya_data['polya_length'] >= 0]

## Group by Contig and calculate average and standard deviation.
polya_groups = polya_data.groupby(polya_data['contig']).agg(
    avg=('polya_length','mean'),SD=('polya_length','std'))

## Produces a csv of data.
polya_groups.to_csv('test.csv')








