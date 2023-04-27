import os

for year in range(2021, 2024):
    os.system(f"hdfs fs -mkdir {year}")

for year in range(2021, 2024)
    for month in range(1, 13):
        month_str = str(month).rjust(2, '0')
        os.system(f"hdfs fs -mkdir {year}/{month_str}")



