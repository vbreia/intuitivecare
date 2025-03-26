import subprocess
import time

def run_script(script_path):
    start_time = time.time()
    result = subprocess.run(["python3", script_path])
    end_time = time.time()
    if result.returncode == 0:
        print(f"\t\n{'=' * 70}\n Sucesso ao executar {script_path} em {end_time - start_time:.2f} segundos\n{'=' * 70}\n")
    else:
        print(f"\t\n{'=' * 60}\n Falha ao executar {script_path}\n{'=' * 60}\n")


run_script("testes-1-e-2/scraping.py")
run_script("testes-1-e-2/transform.py")


