import os
import requests

os.mkdir("downloads")

for year in range(2021, 2024):
    for month in range(1, 13):
        month_str = str(month).rjust(2, '0')

        req = requests.get(f"https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/{year}{month_str}.zip")

        print(f"https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/{year}{month_str}.zip")

        with open(f"downloads/{year}{month_str}.zip", "wb") as zip_download:
            zip_download.write(req.content)