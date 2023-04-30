# Donload do mês atual
python src/download_data.py

# Download completo dos dados
python src/download_data.py -f

docker compose cp files/extract/. namenode:/home/files/
docker compose cp files/zip/. namenode:/home/bkp/

docker compose exec -it namenode bash
hdfs dfs -mkdir /fundos
hdfs dfs -mkdir /fundos_bkp

hdfs dfs -put -f /home/files/*.csv /fundos/
hdfs dfs -put -f /home/bkp/*.zip /fundos_bkp/
