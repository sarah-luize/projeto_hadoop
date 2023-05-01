# Donload dos dados do mês atual
# python src/download_data.py

# Download completo dos dados
python src/download_data.py --full

# Enviar os dados para dentro do docker do Namenode
docker compose cp files/extract/. namenode:/home/funds/
docker compose cp files/zip/. namenode:/home/funds_bkp/

# Transferir os dados do docker para os datanodes
docker compose exec -it namenode bash -c "hdfs dfs -put -f /home/funds /"
docker compose exec -it namenode bash -c "hdfs dfs -put -f /home/funds_bkp /"

# Limpar os dados
# docker compose exec -it namenode bash -c "hdfs dfs -rmr /funds_bkp"
# docker compose exec -it namenode bash -c "hdfs dfs -rmr /funds"
