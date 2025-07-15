import json
import os

def test_wallets_exist():
    assert os.path.exists("secrets/wallets.json")
    with open("secrets/wallets.json") as f:
        wallets = json.load(f)
    assert len(wallets["wallets"]) == 3
    for w in wallets["wallets"]:
        assert w["address"].startswith("0x")

def test_mnemonic_file():
    assert os.path.exists("secrets/mnemonic.txt")
    with open("secrets/mnemonic.txt") as f:
        words = f.read()
    assert len(words.split()) == 12
