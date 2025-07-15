import json
from eth_account import Account
from mnemonic import Mnemonic

mnemo = Mnemonic("english")
words = mnemo.generate(strength=128)
seed = mnemo.to_seed(words)

Account.enable_unaudited_hdwallet_features()
wallets = []

for i, asset in enumerate(["WETH", "DAI", "USDC"]):
    acct = Account.from_mnemonic(words, account_path=f"m/44'/60'/0'/0/{i}")
    wallets.append({
        "asset": asset,
        "address": acct.address,
        "private_key": acct.key.hex()
    })

with open("secrets/mnemonic.txt", "w") as f:
    f.write(words)

with open("secrets/wallets.json", "w") as f:
    json.dump({"wallets": wallets}, f, indent=2)

print("Wallets generated and saved.")
