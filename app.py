from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import requests
import os
import time

# Configuração do chromedriver
PATH = "/usr/bin/chromedriver"  # Atualize este caminho para o caminho real do chromedriver no seu sistema
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# URL da página
driver.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")

try:
    # Fechar o popup clicando em qualquer campo
    body = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, "body"))
    )
    body.click()
    print("Popup fechado")

    # Obter o link do Anexo I
    anexo_i_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Anexo I"))
    )
    anexo_i_url = anexo_i_element.get_attribute("href")
    print(f"URL do Anexo I: {anexo_i_url}")

    # Obter o link do Anexo II
    anexo_ii_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Anexo II"))
    )
    anexo_ii_url = anexo_ii_element.get_attribute("href")
    print(f"URL do Anexo II: {anexo_ii_url}")

    # Diretório para salvar os anexos
    download_dir = os.path.expanduser("./src/scraping/anexos-ans")
    os.makedirs(download_dir, exist_ok=True)

    # Função para baixar e salvar o PDF
    def download_pdf(url, filename):
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"PDF salvo em: {filename}")

    # Baixar e salvar os PDFs
    download_pdf(anexo_i_url, os.path.join(download_dir, "Anexo_I.pdf"))
    download_pdf(anexo_ii_url, os.path.join(download_dir, "Anexo_II.pdf"))

    time.sleep(5)
    
except Exception as e:
    print(e)
finally:
    driver.quit()