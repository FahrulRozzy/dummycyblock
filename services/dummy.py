import pandas as pd

class datadummy:
    def __init__(self,path):
        self.path = path
    
    def getdummy(self):
        data = pd.read_csv(self.path)
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