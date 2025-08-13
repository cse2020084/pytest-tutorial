class Employee():
    def __init__(self):
        self.records={}
    
    def add_record(self,id,name):
        if id in self.records:
            raise ValueError('Record is already there in database')
        self.records[id]=name
        return True
    
    def get_record(self,id):
        return self.get(id,'Unknown')