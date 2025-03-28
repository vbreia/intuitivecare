# **1️⃣ e 2️⃣ Web Scraping e Transformação de Dados**

---

## 1️⃣ Web Scraping

**Descrição:**
O script `scraping.py` realiza o download de um arquivo PDF a partir de uma página da web. Abaixo está o passo a passo do que foi feito:

1. **Definição do diretório de download:**  
   O diretório onde o arquivo será salvo é definido como `../data/pdf`.

2. **Obtenção do conteúdo da página:**  
   A função `get_page_content` utiliza a biblioteca `requests` para acessar a URL fornecida e obter o conteúdo HTML da página.

3. **Extração do link do PDF:**  
   A função `get_anexo_url` utiliza a biblioteca `BeautifulSoup` para localizar o link do arquivo PDF na página, baseado no texto do link.

4. **Download do PDF:**  
   A função `download_pdf` baixa o arquivo PDF a partir do link extraído e o salva no diretório especificado.

---

## 2️⃣ Transformação de Dados

**Descrição:**
O script `transform.py` processa o arquivo PDF baixado, extrai tabelas e transforma os dados em um formato estruturado. Abaixo está o passo a passo do que foi feito:

1. **Leitura do PDF:**  
   O arquivo PDF é lido utilizando a biblioteca `PyPDF2` e/ou `tabula` para extrair as tabelas contidas no documento.

2. **Extração de tabelas:**  
   A classe `PDFTableExtractor` é utilizada para extrair as tabelas a partir de páginas específicas do PDF.

3. **Concatenação das tabelas:**  
   As tabelas extraídas são concatenadas em um único DataFrame utilizando a biblioteca `pandas`.

4. **Renomeação de colunas:**  
   As colunas do DataFrame são renomeadas para facilitar a interpretação dos dados.

5. **Exportação para CSV:**  
   O DataFrame final é salvo como um arquivo CSV no diretório especificado.

6. **Compressão do CSV:**  
   O arquivo CSV gerado é compactado em um arquivo ZIP para facilitar o armazenamento e compartilhamento.

---

## 🛠️ Execução

Para rodar o projeto, siga os passos abaixo:

1. Certifique-se de estar no diretório `./testes-1-e-2`.
2. Execute o script principal `app.py` com o comando:

   ```bash
   python3 app.py
    ```
