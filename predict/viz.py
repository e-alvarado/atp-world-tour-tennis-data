import pandas as pd

mstats_2021 = pd.read_csv(r"C:\Users\mexic\atp-world-tour-tennis-data\csv\3_match_stats\match_stats_2021.csv")

#initial verification of import
print(len(mstats_2021.index))
print(mstats_2021.shape[0])