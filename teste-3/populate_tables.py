import pandas as pd
from sqlalchemy import create_engine
import os
from sqlalchemy.types import String, Integer, Date

engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/postgres')

def populate_demonstracoes_contabeis():
    csv_folder = '../data/csvs/demo_cont'

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
    csv_file = '../data/csvs/Relatorio_cadop.csv'

    # Ler o arquivo CSV
    df = pd.read_csv(csv_file, delimiter=';', encoding='utf-8')


    # Padronizar os nomes das colunas
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Substituir aspas apenas nas colunas do tipo string
    string_columns = df.select_dtypes(include=['object']).columns
    df[string_columns] = df[string_columns].apply(lambda x: x.str.replace('"', '', regex=False))

    # Verificar a presença da coluna 'numero'
    if 'numero' in df.columns:
        df['numero'] = pd.to_numeric(df['numero'], errors='coerce')
    else:
        print("A coluna 'numero' não está presente no DataFrame.")

    # Converter outras colunas específicas para os tipos apropriados
    if 'regiao_de_comercializacao' in df.columns:
        df['regiao_de_comercializacao'] = pd.to_numeric(df['regiao_de_comercializacao'], errors='coerce')
    if 'data_registro_ans' in df.columns:
        df['data_registro_ans'] = pd.to_datetime(df['data_registro_ans'], errors='coerce', format='%Y-%m-%d')

    # Limpar e truncar valores nas colunas de texto
    if 'uf' in df.columns:
        df['uf'] = df['uf'].str.strip().str[:2]
    if 'cep' in df.columns:
        df['cep'] = df['cep'].astype(str).str.strip().str[:8]
    if 'ddd' in df.columns:
        df['ddd'] = df['ddd'].astype(str).str.strip().str[:2]
    if 'telefone' in df.columns:
        df['telefone'] = df['telefone'].astype(str).str.strip().str[:8]
    if 'fax' in df.columns:
        df['fax'] = df['fax'].astype(str).str.strip().str[:8]

    # Inserir os dados no banco de dados

    df.to_sql(
        'op_plano_de_saude',
        engine,
        if_exists='append',
        index=False,
        dtype={
            'registro_ans': String(5),
            'cnpj': String(14),
            'razao_social': String,
            'nome_fantasia': String,
            'modalidade': String,
            'logradouro': String,
            'numero': Integer,
            'complemento': String,
            'bairro': String,
            'cidade': String,
            'uf': String(2),
            'cep': String(8),
            'ddd': String(2),
            'telefone': String(8),
            'fax': String(8),
            'endereco_eletronico': String,
            'representante': String,
            'cargo_representante': String,
            'regiao_de_comercializacao': Integer,
            'data_registro_ans': Date
        }
    )
    print("Dados inseridos com sucesso na tabela op_plano_de_saude.")

populate_demonstracoes_contabeis()
populate_op_plano_de_saude()