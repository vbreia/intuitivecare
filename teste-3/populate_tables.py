import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/postgres')

def populate_demonstracoes_contabeis():
    csv_folder = './data/csvs/demo_cont'

    # Consolidar todos os arquivos CSV em um único DataFrame
    all_files = [os.path.join(csv_folder, f) for f in os.listdir(csv_folder) if f.endswith('.csv')]
    df_list = [pd.read_csv(file, delimiter=';', encoding='utf-8') for file in all_files]
    df = pd.concat(df_list, ignore_index=True)

    # Substituir vírgula por ponto nos valores numéricos
    df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.').astype(float)
    df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].str.replace(',', '.').astype(float)

    df.columns = df.columns.str.lower()

    # Popular a tabela demonstracoes_contabeis com o DataFrame criado
    df.to_sql('demonstracoes_contabeis', engine, if_exists='append', index=False)
    print("Dados inseridos com sucesso na tabela demonstracoes_contabeis.")
    

def populate_op_plano_de_saude():
    csv_file = './data/csvs/Relatorio_cadop.csv'

    df = pd.read_csv(csv_file, delimiter=';', dtype=str)

    df['Numero'] = pd.to_numeric(df['Numero'], errors='coerce')
    df['Regiao_de_Comercializacao'] = pd.to_numeric(df['Regiao_de_Comercializacao'], errors='coerce')
    df['Data_Registro_ANS'] = pd.to_datetime(df['Data_Registro_ANS'], errors='coerce', format='%d/%m/%Y')

    df.columns = df.columns.str.lower()

    df.to_sql('op_plano_de_saude', engine, if_exists='append', index=False)
    print("Dados inseridos com sucesso na tabela op_plano_de_saude.")

populate_demonstracoes_contabeis()
populate_op_plano_de_saude()