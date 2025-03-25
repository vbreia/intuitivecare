import os
import pandas as pd
from PyPDF2 import PdfReader
import tabula
import zipfile
import time

class PDFTableExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.num_pages = self._get_num_pages()
        self.tables = []

    def _get_num_pages(self):
        with open(self.pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            return len(pdf_reader.pages)

    def extract_tables(self, start_page):
        start_time = time.time()
        all_tables = []
        for page in range(start_page, self.num_pages + 1):
            page_tables = tabula.read_pdf(self.pdf_path, pages=page, multiple_tables=True)
            all_tables.extend(page_tables)
        self.tables = all_tables
        end_time = time.time()
        print(f'Tabelas extraídas em {end_time - start_time:.2f} segundos')

    def concatenate_tables(self):
        start_time = time.time()
        df_list = [pd.DataFrame(table) for table in self.tables]
        final_df = pd.concat(df_list, ignore_index=True)
        final_df = final_df.iloc[:, :13]
        end_time = time.time()
        print(f'Tabelas concatenadas em {end_time - start_time:.2f} segundos')
        return final_df

    def rename_columns(self, df):
        start_time = time.time()
        df.rename(columns={'OD': 'Seg. Odontológica'}, inplace=True)
        df.rename(columns={'AMB': 'Seg. Ambulatorial'}, inplace=True)
        df.rename(columns={'RN\r(alteração)': 'RN (alteração)'}, inplace=True)
        end_time = time.time()
        print(f'Colunas renomeadas em {end_time - start_time:.2f} segundos')
        return df

    def save_to_csv(self, df, output_csv):
        start_time = time.time()
        df.to_csv(output_csv, index=False)
        end_time = time.time()
        print(f'Arquivo CSV salvo com sucesso em {end_time - start_time:.2f} segundos')

    def compress_csv(self, output_csv, output_zip):
        start_time = time.time()
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(output_csv, os.path.basename(output_csv))
        os.remove(output_csv)
        end_time = time.time()
        print(f'Arquivo CSV comprimido em {end_time - start_time:.2f} segundos')

if __name__ == "__main__":
    pdf_path = "./data/ans/Anexo_I.pdf"
    output_csv = "./data/ans/Rol_de_Procedimentos.csv"
    output_zip = "./data/ans/Teste_victor-breia.zip"

    extractor = PDFTableExtractor(pdf_path)
    extractor.extract_tables(start_page=3)
    final_df = extractor.concatenate_tables()
    final_df = extractor.rename_columns(final_df)
    extractor.save_to_csv(final_df, output_csv)
    extractor.compress_csv(output_csv, output_zip)
