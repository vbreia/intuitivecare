import requests
from bs4 import BeautifulSoup
import os

class Scraper:
    def __init__(self, download_dir):
        self.download_dir = download_dir
        os.makedirs(download_dir, exist_ok=True)

    def get_page_content(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro se a solicitação falhar
        return response.content

    def get_anexo_url(self, soup, link_text):
        try:
            link = soup.find('a', string=link_text)
            url = link['href']
            print(f"URL do {link_text}: {url}")
            return url
        except Exception as e:
            print(f"Erro ao obter o URL do {link_text}: {e}")
            return None

    def download_pdf(self, url, filename):
        try:
            response = requests.get(url)
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"PDF salvo em: {filename}")
        except Exception as e:
            print(f"Erro ao baixar o PDF de {url}: {e}")

    def scrape(self, url):
        content = self.get_page_content(url)
        soup = BeautifulSoup(content, 'html.parser')
        anexos = ['Anexo I.', 'Anexo II.']
        for anexo in anexos:
            anexo_url = self.get_anexo_url(soup, anexo)
            if anexo_url:
                self.download_pdf(anexo_url, os.path.join(self.download_dir, f"{anexo.replace(' ','_')}pdf"))
                

if __name__ == "__main__":
    DOWNLOAD_DIR = os.path.expanduser("./data/pdf")
    URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    scraper = Scraper(DOWNLOAD_DIR)
    scraper.scrape(URL)