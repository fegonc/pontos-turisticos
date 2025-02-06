import os
import shutil

def delete_pycache(root_dir="."):
    """Remove todos os diretórios __pycache__ dentro de root_dir"""
    for root, dirs, files in os.walk(root_dir):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            shutil.rmtree(pycache_path)
            print(f"Removido: {pycache_path}")

if __name__ == "__main__":
    delete_pycache()