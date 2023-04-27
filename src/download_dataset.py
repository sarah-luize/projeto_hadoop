import os
import requests

try:
    os.mkdir("downloads")
except:
    pass

for year in range(2021, 2024):
    for month in range(1, 13):
        month_str = str(month).rjust(2, '0')

        req = requests.get("https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/{}{}.zip".format(year, month_str))
        print("Baixando dado: {}/{}".format(month_str, year))

        with open("downloads/{}{}.zip".format(year, month_str), "wb") as zip_download:
            zip_download.write(req.content)
        
        print("Movendo dado: {}/{} - para HDFS".format(month_str, year))
        os.system("hdfs dfs -put downloads/{}{}.zip {}/{}/inf_diario.zip".format(year, month_str, year, month_str))