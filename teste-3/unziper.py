# Extrai os arquivos csv dos arquivos zipados para o diretório /csvs.
import os
import zipfile
import csv

def extract_csvs_from_zip_files(input_dir, output_dir):
    for file in os.listdir(input_dir):
        if file.endswith('.zip'):
            with zipfile.ZipFile(input_dir + file, 'r') as zip_ref:
                zip_ref.extractall(output_dir)
    return  

def main():
    input_dir = 'data/zip_files/'
    output_dir = 'data/csvs/demo_cont'
    extract_csvs_from_zip_files(input_dir, output_dir)
    return  

if __name__ == '__main__':
    main()
