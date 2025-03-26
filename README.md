# 🏥 IntuitiveCare - Teste de Nivelamento  

Bem-vindo(a) ao repositório do **Teste de Nivelamento** para a IntuitiveCare! 🚀  
Este projeto foi desenvolvido para demonstrar habilidades em **coleta, transformação, armazenamento e análise de dados**, além da criação de uma API interativa.  

---

## 📌 **Descrição do Projeto**  

Este repositório contém soluções para os desafios propostos, divididos em quatro etapas:  

1️⃣ **Web Scraping**: Coleta de arquivos PDF diretamente do site da ANS.  
2️⃣ **Transformação de Dados**: Extração de tabelas do PDF e conversão para CSV.  
3️⃣ **Banco de Dados**: Criação e manipulação de tabelas SQL para análise de dados.  
4️⃣ **API e Interface Web**: Desenvolvimento de uma API em Python e uma interface em Vue.js.  

Cada etapa foi implementada com foco em **boa organização, eficiência e boas práticas de desenvolvimento**.  

---

## 🛠 **Tecnologias Utilizadas**  

- **Linguagem:** Python 3.10+  
- **Bibliotecas:** `requests`, `BeautifulSoup`, `PyPDF2`, `pandas`, `tabula`, `SQLAlchemy`, `FastAPI`  
- **Banco de Dados:** PostgreSQL (Docker)  
- **API:** FastAPI  
- **Frontend:** Vue.js (Docker)  
- **Testes:** Postman (Docker)  

---

## 📂 **Estrutura do Projeto**  

```bash
📦 intuitivecare
│── 📂 testes-1-e-2            # Contendo o teste de web scraping e transformação de dados
│   ├── 📜 app.py              # Aplicativo Python que roda os scripts
│   ├── 📜 scraping.py         # Script Python que faz o scraping
│   ├── 📜 transform.py        # Script Python que transforma os dados
│── 📂 teste-3                 # Contendo o teste de SQL
│   ├── 📜 populate_tables.py  # Script Python que popula as tabelas do banco postgres
│   ├── 📜 unziper.py          # Scripy Python que descompacta os arquivos CSV do teste 3
│   └── 📂 sql                 # Contendo as queries utilizadas para solucionar o teste 3
│── 📜 README.md               # Documentação do projeto
│── 📜 .gitignore              # Arquivos ignorados pelo Git
│── 📜 docker-compose.yml      # Docker rodando PostgreSQL
│── 📜 requirements.txt        # Bibliotecas necessárias para rodar o projeto
│── 📂 sql                     # DDL que inicia junto ao docker quando sobe o banco
└── 📂 data                    # Outputs do projeto
```

---

### **1️⃣ e 2️⃣ Web Scraping e Transformação de Dados**

---

- **Descrição:**  
  - O teste de Web Scraping consiste em coletar arquivos PDF diretamente do site da ANS.  
  - O teste de Transformação de Dados consiste em extrair tabelas do PDF e convertê-las para CSV.
  - [Informações completas](testes-1-e-2/README.md)

---

### **3️⃣Banco de Dados**

---

- **Descrição:**  
  - O teste de Banco de Dados consiste em criar e manipular tabelas SQL para análise de dados.
  - [Informações completas](teste-3/README.md)

---
