import pandas as pd
import random
class datadummy:
    def __init__(self,path):
        self.path = path
         # definisi kapasitas
        self.block_capacity = {
            "A": {"columns": 13, "rows": 7, "tiers": 6},
            "B": {"columns": 18, "rows": 7, "tiers": 6},
            "C": {"columns": 18, "rows": 7, "tiers": 6},
        }
        
    
    def getdummy(self):
        data = pd.read_csv(self.path)
        # Buat set semua slot yang mungkin
        all_slots = set()
        for block, conf in self.block_capacity.items():
            for row in range(1, conf["rows"] + 1):
                for col in range(1, conf["columns"] + 1):
                    for tier in range(1, conf["tiers"] + 1):
                        all_slots.add((block, row, col, tier))

        # Ambil slot yang sudah terisi
        used_slots = set(
            zip(data["Block"], data["Row"], data["Column"], data["Tier"])
        )

        # Cari slot kosong
        empty_slots = list(all_slots - used_slots)
        
         # Jika slot kosong ada, pilih maksimal 3 random
        num_to_move = min(3, len(empty_slots), len(data))
        chosen_slots = random.sample(empty_slots, num_to_move)

        # Update maksimal 3 container
        for i, slot in enumerate(chosen_slots):
            block, row, col, tier = slot
            data.loc[i, ["Block", "Row", "Column", "Tier"]] = [block, row, col, tier]

        return data
    
    def updatedummy(self,nc,blockbaru):
        data = pd.read_csv(self.path)
        parts = blockbaru.split('.') 
        print(blockbaru)
        print(parts) 
    
        if len(parts) != 4:
            raise ValueError("Format blockbaru harus 'Block.Row.Column.Tier'")
        block, row, column, tier = parts  # kasih nama biar jelas
        print(block)
        print(row)
        print(column)
        # update nilai
        data.loc[data['Container'] == nc, ['Block']] = block
        data.loc[data['Container'] == nc, ['Row']] = row
        data.loc[data['Container'] == nc, ['Column']] = column
        data.loc[data['Container'] == nc, ['Tier']] = tier
        data.to_csv(self.path,index=False,mode="w")
        return data