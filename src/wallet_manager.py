from eth_account import Account
import os
import json

class WalletManager:
    def __init__(self, secrets_path="./secrets/wallets.json"):
        self.secrets_path = secrets_path
        self.wallets = []

    def generate_wallets(self, count=3):
        self.wallets = []
        for _ in range(count):
            acct, mnemonic = Account.create_with_mnemonic()
            self.wallets.append({
                "address": acct.address,
                "private_key": acct.key.hex(),
                "mnemonic": mnemonic
            })
        self._save_wallets()
        return self.wallets

    def _save_wallets(self):
        os.makedirs(os.path.dirname(self.secrets_path), exist_ok=True)
        with open(self.secrets_path, "w") as f:
            json.dump(self.wallets, f, indent=4)

    def load_wallets(self):
        if os.path.exists(self.secrets_path):
            with open(self.secrets_path, "r") as f:
                self.wallets = json.load(f)
        return self.wallets
