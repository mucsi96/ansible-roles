from pathlib import Path
from ansible.parsing.vault import VaultSecret
from ansible.constants import DEFAULT_VAULT_ID_MATCH
from ansible.parsing.dataloader import DataLoader

def read_file(file_path: Path):
    try:
        with open(file_path, 'rb') as file:
            return file.read().strip()
    except:
        print("Error reading file at", file_path)


def load_vars(vault_secret_file: Path, vars_file: Path):
    vault_secret = read_file(vault_secret_file)
    loader = DataLoader()
    loader.set_vault_secrets([(DEFAULT_VAULT_ID_MATCH, VaultSecret(vault_secret))])
    return loader.load_from_file(str(vars_file))