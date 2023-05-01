import sys
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile

import requests

ZIP_FILES_PATH = "files/zip"
EXTRACT_FILES_PATH = "files/extract"
TODAY = datetime.today()


def download_data(year: str, month: str) -> Path | None:
    url = f"https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{year}{month}.zip"
    req = requests.get(url)
    print(f"Baixando arquivo referente a: {month}/{year}")
    if req.status_code != 200:
        print(f"Arquivo referente a: {month}/{year} não encontrado.")
        return None

    path = Path(ZIP_FILES_PATH) / year / month
    path.mkdir(parents=True, exist_ok=True)
    filename = f"{month}_{year}.zip"
    print(f"Salvando o arquivo em: {path/filename}")
    (path / filename).write_bytes(req.content)
    return path / filename


def unpack_file(path: str | Path, path_to: str | Path):
    with ZipFile(path, "r") as zip:
        print(f"Extraindo {path}")
        zip.extractall(path_to)
        print("OK!")


if __name__ == "__main__":
    Path("files/zip").mkdir(parents=True, exist_ok=True)
    Path("files/extract").mkdir(parents=True, exist_ok=True)
    try:
        param = sys.argv[1]
        if param in ["-f", "--full"]:
            for year in range(2021, TODAY.year):
                for month in range(1, 13):
                    month_str = str(month).rjust(2, "0")
                    year_str = str(year)
                    path = download_data(year_str, month_str)
                    if not path:
                        continue

                    unpack_file(path, Path(EXTRACT_FILES_PATH) / year_str / month_str)
    except IndexError:
        year_str = str(TODAY.year)
        month_str = str(TODAY.month).rjust(2, "0")
        path = download_data(year=year_str, month=month_str)
        if not path:
            raise ValueError(
                f"Erro ao baixar os dados referentes a {month_str}/{year_str}"
            )
        unpack_file(path, Path(EXTRACT_FILES_PATH) / year_str / month_str)
