import argparse
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zipfile import ZipFile

import requests

ZIP_FILES_PATH = "files/zip"
EXTRACT_FILES_PATH = "files/extract"
TODAY = datetime.today()


def create_dir(path: str):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


create_dir("files/zip")
create_dir("files/extract")


def download_full_data():
    for year in range(2021, 2024):
        for month in range(1, 13):
            month_str = str(month).rjust(2, "0")
            url = f"https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{year}{month_str}.zip"
            req = requests.get(url)

            if req.status_code != 200:
                continue

            print(f"Baixando arquivo referente a: {month_str}/{year}")

            (Path(ZIP_FILES_PATH) / f"{month_str}_{year}.zip").write_bytes(req.content)


def download_latest_data() -> Path:
    today = datetime.today()
    month = str(today.month).rjust(2, "0")
    year = today.year
    url = f"https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{year}{month}.zip"
    req = requests.get(url)
    if req.status_code != 200:
        pass

    print(f"Baixando arquivo referente a: {month}/{year}")
    path = Path(ZIP_FILES_PATH) / f"{month}_{year}.zip"
    path.write_bytes(req.content)
    return path


def unpack_file(path: str | Path):
    with ZipFile(path, "r") as zip:
        print(f"Extraindo {path}")
        zip.extractall(EXTRACT_FILES_PATH)
        print("OK!")


def unpack_full_data(path: str | None = None):
    for zip_file in Path(ZIP_FILES_PATH).iterdir():
        unpack_file(zip_file)


if __name__ == "__main__":
    create_dir("files/zip")
    create_dir("files/extract")

    if sys.argv[1] in ["-f", "--full"]:
        download_full_data()
        unpack_full_data()
    else:
        file_path = download_latest_data()
        unpack_file(file_path)
