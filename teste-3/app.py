import subprocess
import time
import os

def run_script(script_path):
    start_time = time.time()
    result = subprocess.run(["python3", script_path])
    end_time = time.time()
    if result.returncode == 0:
        print(f"\t\n{'=' * 70}\n Sucesso ao executar {script_path} em {end_time - start_time:.2f} segundos\n{'=' * 70}\n")
        return True
    else:
        print(f"\t\n{'=' * 60}\n Falha ao executar {script_path}\n{'=' * 60}\n")
        return False

def clean_csv_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Erro: A pasta {folder_path} não existe ou não é acessível.")
        return

    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    if not csv_files:
        print(f"Nenhum arquivo CSV encontrado em {folder_path}.")
        return

    # Calcular o tamanho total dos arquivos CSV
    total_size = sum(os.path.getsize(os.path.join(folder_path, file)) for file in csv_files)
    total_size_mb = total_size / (1024 * 1024)  # Converter para megabytes

    try:
        for file in csv_files:
            os.remove(os.path.join(folder_path, file))
        print(f"\t\n{'=' * 70}\n Todos os arquivos CSV foram removidos de {folder_path}.\n")
        print(f"\tFoi removido o total de: {total_size_mb:.2f} MB\n{'=' * 70}\n")
    except Exception as e:
        print(f"Erro ao remover arquivos: {e}")

# Executar os scripts
if run_script("unziper.py") and run_script("populate_tables.py"):
    # Remover os arquivos CSV se ambos os scripts forem executados com sucesso
    clean_csv_folder("../data/csvs/demo_cont")