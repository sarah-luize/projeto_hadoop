# Projeto Hadoop - MBA FIAP Data Engineering

## Autores

Daniel Udala - RM348932

Sara Luize - RM348391

Giancarlo Lester - RM348315

Vinicius Mesel - RM348353


## Dataset - CVM Fundos

Esse projeto contempla o dataset da CVM, o [Fundos de Investimento: Documentos: Informe Diário](https://dados.cvm.gov.br/dataset/fi-doc-inf_diario). Este é um dataset que reporta dados de cotações de fundos diariamente na CVM, o arquivo em si é mensal porém a frequência de atualização é diária.

**Segundo a CVM**: O INFORME DIÁRIO é um demonstrativo que contém as seguintes informações do fundo, relativas à data de competência:

 - Valor total da carteira do fundo;
 - Patrimônio líquido;
 - Valor da cota;
 - Captações realizadas no dia;
 - Resgates pagos no dia;
 - Número de cotistas

Os arquivos são disponibilizados no formato ZIP e salvos nos mesmos diretórios abertos publicos.

## Por que do dataset?

Escolhemos este dataset por termos interesse na área de investimentos e sermos investidores de alguns fundos de investimentos.

## Formato do dataset

O dataset é disponibilizado em um diretório HTTP no site de dados abertos da CVM. Cada um dos arquivos disponibilizados está no formato ZIP e dentro deste ZIP está um CSV com os dados disponibilizados pelas gestoras de investimento.

## Estrutura de dados dentro do HDFS

A estrutura de diretórios e de dados escolhida para o HDFS é baseada em data do arquivo, seguindo em ano e mês. Então a estrutura de arquivos ficaria:

```
/home/funds/2023
├── 01
│   └── inf_diario_fi_202301.csv
├── 02
│   └── inf_diario_fi_202302.csv
├── 03
│   └── inf_diario_fi_202303.csv
└── 04
    └── inf_diario_fi_202304.csv
```

Essa estrutura foi escolhida para favorecer o uso de arquivos datados e suas atualizações, permitindo com que saibamos o arquivo que foi atualizado e o mês que ele se refere, além de permitir com que compartimentemos os dados por seus meses e anos de competência. 

### Executando o projeto

Para poder executar o projeto você vai precisar de 2 terminais, esses 2 terminais serão usados com 2 entrypoints diferentes

No primeiro terminal, você vai entrar, executar os seguintes comandos
```
docker-compose up -d --build # Este comando irá subir o ambiente e buildar as imagens
docker-compose exec datanode bash # Você entrará dentro deste container do datanode

# Dentro do data node, no bash dele você irá executar

sh /src/run.sh
```

Já no segundo terminal você também entrará no container, mas executará as rotinas de preparação do ambiente e load de dados. A rotina de setup de ambiente (setup_folders.py) dentro do HDFS permite com que tenhamos todo o ambiente criado com as pastas respectivas para meses e anos dos dados da CVM


```
docker-compose exec datanode bash # Você entrará dentro deste container do datanode

python3 /src/setup_folders.py # Montará a estrutura de diretórios dentro do HDFS (só precisa ser rodado 1 vez)
python3 /src/download_dataset.py # Rodar diariamente para baixar os dados
```

### Estratégia de Backup

```
Redigir uma estratégia de backup condizente com os dados. A meu ver (vinicius aqui), devemos ter um backup de arquivos zip, com uma retenção mensal. Não sei como estruturar isso dentro do HDFS, porém deve ser algo simples.
```

```
/home/funds_bkp/2023
├── 01
│   └── 01_2023.zip
├── 02
│   └── 02_2023.zip
├── 03
│   └── 03_2023.zip
└── 04
    └── 04_2023.zip
```