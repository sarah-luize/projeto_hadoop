# Donload do mês atual
python src/download_data.py

# Download completo dos dados
python src/download_data.py --full

docker compose cp files/extract/. namenode:/home/funds/
docker compose cp files/zip/. namenode:/home/funds_bkp/

docker compose exec -it namenode bash

hdfs dfs -put -f /home/funds /
hdfs dfs -put -f /home/funds_bkp /
