from bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8

run echo "deb http://archive.debian.org/debian stretch main contrib non-free" > /etc/apt/sources.list

run apt-get clean && apt update -y && apt upgrade -y && apt install python3 python3-pip python3-dev -y

COPY src/run.sh /run.sh

run python3 -m pip install requests

CMD ["/run.sh"]