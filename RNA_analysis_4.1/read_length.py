import argparse
from read_analysis import format_df,make_plot

parser = argparse.ArgumentParser()
parser.add_argument('inputfile_1')
parser.add_argument('inputfile_2')
args = parser.parse_args()

print(args.inputfile_1)
print(args.inputfile_2)

sample_1 = format_df(args.inputfile_1)
sample_2 = format_df(args.inputfile_2)
make_plot(sample_1,sample_2)