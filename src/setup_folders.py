import os

if os.system("hdfs dfs -ls /user") != 0:
    print("Pasta /user inexistente - criando")
    os.system("hdfs dfs -mkdir /user")

if os.system("hdfs dfs -ls /user/root") != 0:
    print("Pasta /user/root inexistente - criando")
    os.system("hdfs dfs -mkdir /user/root")


for year in range(2021, 2024):
    os.system("hdfs dfs -mkdir {}".format(year))

for year in range(2021, 2024):
    for month in range(1, 13):
        month_str = str(month).rjust(2, '0')
        os.system("hdfs dfs -mkdir {}/{}".format(year, month_str))



