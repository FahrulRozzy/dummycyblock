from services.dummy import datadummy

class DummyController:
    def __init__(self, path):
        self.service = datadummy(path)

    def get(self):
        try:
            data = self.service.getdummy()
            return data.to_dict(orient="records")
        except Exception as e:
            return {"error": str(e)}
    
    def update_dummmy(self,nc,blockbaru):
        try:
            data = self.service.updatedummy(nc,blockbaru)
            return data.to_dict(orient="records")
        except Exception as e:
            return {"error":str(e)}
        
