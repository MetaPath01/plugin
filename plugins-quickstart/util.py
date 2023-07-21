import json
import os

def get_equipment_no(address):
    equipmentNo = ''
    if len(address) <= 32:
        n = 32 - len(address)
        for i in range(n):
            equipmentNo += 'x'
        equipmentNo += address
    else:
        equipmentNo = address
    return equipmentNo.lower()[0:32]

    
def get_coin_info(name, chain):
    tokens = []
    try:
        with open('./plugins-quickstart/token_files/{}_tokens_map.json'.format(chain.lower(), 'r')) as f:
            tokens = json.load(f)
        print(name)
        if name in tokens:
            return tokens[name]
        if name.upper() in tokens:
            return tokens[name.upper()]
        if name.lower() in tokens:
            return tokens[name.lower()]
        print(name)
    except:
        return []

if __name__ == "__main__":
    get_coin_info("bnb", "ETH")