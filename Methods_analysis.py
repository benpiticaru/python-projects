import numpy as np
import pandas as pd
import os
import subprocess as sp
import argparse
from read_analysis import find_guppy_location,basecaller,file_combine,run_analysis,format_read_df,format_poly_df,make_read_plot,make_read_hist,make_poly_plot

## The following arguments are the location of the fast5 files and sample name for one sample, followed by
##   the fast5 files and sample name for sample 2.
parser = argparse.ArgumentParser()
parser.add_argument('experiment_name')
parser.add_argument('inputfile_1')
parser.add_argument('name_1')
parser.add_argument('inputfile_2')
parser.add_argument('name_2')
args = parser.parse_args()

##########################################################################################################
## Variable Information needed for location of programs.
##########################################################################################################
reference_genome='/home/ben/MINION/reference_genomes/ncbi-genomes-2023-01-04/GCF_000001405.26_GRCh38_rna.fna'
nanopolish='/home/ben/Applications/nanopolish/nanopolish'
minimap2='/home/ben/Applications/minimap2/minimap2'

## add a condition for if guppy_outdir is empty, then run guppy and create a folder and run guppy.

## making the output folders
sp.run('mkdir {a}'.format(a=args.experiment_name),shell=True)
os.chdir('{a}'.format(a=args.experiment_name))
## Turns the information inputed into a dataframe
s1 = args.name_1
s2 = args.name_2
data={'location':[args.inputfile_1,args.inputfile_2],'Sample':[s1,s2]}
df = pd.DataFrame(data)

for index, row in df.iterrows():
    fast5_dir = row['location']
    sample_ID = row['Sample']
    sp.run('mkdir {a}'.format(a=sample_ID),shell=True)
    os.chdir('{a}'.format(a=sample_ID))
    guppy_outdir = find_guppy_location(sample_ID)
    if guppy_outdir == 'NONE':
        guppy_outdir = basecaller(fast5_dir,sample_ID)
    file_combine('{a}/pass'.format(a=guppy_outdir),sample_ID)
    run_analysis(nanopolish,fast5_dir,'{a}/sequencing_summary.txt'.format(a=guppy_outdir),
                                        '{a}-combined.fastq'.format(a=sample_ID),minimap2,reference_genome,sample_ID)
    format_read_df('{a}-read_length_dataset.csv'.format(a=sample_ID),sample_ID)
    format_poly_df('{a}-polya_length.csv'.format(a=sample_ID),sample_ID)
    os.chdir('..')

make_poly_plot('{a}/{a}-formated-poly-lengths.csv'.format(a=df.iloc[0,1]), 
df.iloc[0,1],'{a}/{a}-formated-poly-lengths.csv'.format(a=df.iloc[1,1]), df.iloc[1,1])

sp.run("echo 'Poly(A) Length analysis complete.'", shell=True)

make_read_plot('{a}/{a}-formated-read-lengths.csv'.format(a=df.iloc[0,1]), 
df.iloc[0,1],'{a}/{a}-formated-read-lengths.csv'.format(a=df.iloc[1,1]), df.iloc[1,1])

make_read_hist('{a}/{a}-read_length_dataset.csv'.format(a=df.iloc[0,1]), 
df.iloc[0,1],'{a}/{a}-read_length_dataset.csv'.format(a=df.iloc[1,1]), df.iloc[1,1])

sp.run("echo 'Read Length analysis complete.'", shell=True)