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
│── 📂 src                     # Código-fonte do projeto
│   ├── 📂 testes-1-e-2        # Contendo o teste de web scraping e transformação de dados
│   │   ├── 📜 app.py          # Aplicativo python que roda os dois testes
│   │   ├── 📜 scraping.py     # Script python que faz o scrap
│   │   ├── 📜 transform.py    # Script python que transforma os dados
│── 📜 README.md               # Documentação do projeto
│── 📜 .gitignore              # Arquivos ignorados pelo Git
└── 📦 data                    # Outupts do projeto
```

### **1️⃣ e 2️⃣ Web Scraping e Transformação de Dados**

---

- **Descrição:**  
  - O teste de Web Scraping consiste em coletar arquivos PDF diretamente do site da ANS.  
  - O teste de Transformação de Dados consiste em extrair tabelas do PDF e convertê-las para CSV.
  - [Informações completas](testes-1-e-2/README.md)
