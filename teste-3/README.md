# **3️⃣ Banco de Dados**

---

## **Descrição**

Este projeto tem como objetivo processar e analisar dados relacionados a operadoras de saúde, utilizando scripts Python para manipulação de arquivos e consultas SQL para responder às perguntas do teste.

---

## 🐍 Scripts Python

### **1. `unziper.py`**
Este script é responsável por descompactar arquivos ZIP contendo os dados necessários para o teste. Ele realiza as seguintes etapas:

1. **Localização do arquivo ZIP:**  
   Identifica os arquivos ZIP no diretório `../data/zip_files/`.

2. **Extração dos arquivos:**  
   Utiliza a biblioteca `zipfile` para extrair os arquivos para o diretório `../data/csvs/demo_cont`.

---

### **2. `populate_tables.py`**
Este script é responsável por popular as tabelas do banco de dados com os dados extraídos e processados. Ele realiza as seguintes etapas:

1. **Leitura de arquivos CSV:**  
   - Para a tabela `demonstracoes_contabeis`, os arquivos CSV localizados no diretório `../data/csvs/demo_cont` são lidos e concatenados em um único DataFrame utilizando a biblioteca `pandas`.
   - Para a tabela `op_plano_de_saude`, o arquivo `Relatorio_cadop.csv` é lido e processado.

2. **Processamento dos dados:**  
   - Substituição de vírgulas por pontos em valores numéricos.
   - Padronização dos nomes das colunas para letras minúsculas e remoção de espaços.
   - Conversão de tipos de dados, como datas e números, utilizando `pandas`.

3. **Inserção no banco de dados:**  
   - Utiliza a biblioteca `sqlalchemy` para conectar-se ao banco de dados PostgreSQL e inserir os dados nas tabelas `demonstracoes_contabeis` e `op_plano_de_saude`.

---

### **3. `app.py`**
Este é o script principal que orquestra a execução dos outros scripts e realiza tarefas auxiliares. Abaixo está o passo a passo do que foi feito:

1. **Execução do `unziper.py`:**  
   O script `app.py` inicia executando o `unziper.py` para descompactar os dados que estão zipados e adicioná-los dentro de uma pasta específica (`../data/csvs/demo_cont`).

2. **Execução do `populate_tables.py`:**  
   Após a descompactação, o `populate_tables.py` é executado para percorrer os arquivos CSV extraídos, concatenar os dados e criar um DataFrame que será inserido no banco de dados.

3. **Limpeza de arquivos CSV:**  
   Após a execução de todos os scripts, os arquivos CSV são apagados para otimizar o espaço de armazenamento. Os arquivos CSV ocupam cerca de 500 MB, enquanto os mesmos dados compactados ocupam apenas 70 MB. A limpeza é realizada pela função `clean_csv_folder`.

---

## 📂 Pasta `sql`

A pasta `sql` contém o arquivo `queries.sql`, que inclui as consultas SQL necessárias para responder às perguntas do teste. As consultas são:

1. **Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?**

2. **Quais as 10 operadoras com maiores despesas nessa categoria no último ano?**

Essas consultas podem ser executadas diretamente no banco de dados para obter os resultados esperados.

---

## 🛠️ Execução

Para rodar o projeto, siga os passos abaixo:

1. Certifique-se de estar no diretório `./teste-3`.
2. Execute o script principal `app.py` com o comando:

   ```bash
   python3 app.py
    ```
