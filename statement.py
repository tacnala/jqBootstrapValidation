
from typing import List, Dict
from library import Identity

import json

class Sheet:
    def __init__(self, name: str, category: str = None, sheetID = None):

        self.name, self.category, self.id = name, category, sheetID
        if self.id is None: self.id = Identity.idme(self, name)

        self.storage = {
            "info": {
                "sheetID": self.id
                ,"name": self.name
                ,"category": self.category
            }
            ,"records": []
        }
        
        self.records: Dict[str, Record] = {}

    def add_record(self, record):
        self.records[record.name] = record
        self.storage["records"].append(record.storage)
        return


class Record:
    def __init__(self, name: str, amount: float = 0.0, day: int = 0, fixed: bool = True, description: str = '', start_date: str = "1/1/1999", end_date: str = "1/1/2099", recordID = None):
        self.name, self.amount, self.day, self.fixed, self.description, self.start_date, self.end_date = name, amount, day, fixed, description, start_date, end_date
        self.id = recordID
        if self.id is None: self.id = Identity.idme(self, self.name)

        self.storage = {
            "recordID": self.id
            ,"name": self.name
            ,"amount": self.amount
            ,"day": self.day
            ,"fixed": self.fixed
            ,"description": self.description
            ,"start_date": self.start_date
            ,"end_date": self.end_date
        }




def main():
    return

if __name__ == '__main__':
    
    needs = Sheet("Needs")

    macy_cc = Record("Macy CC", 36.0, 2, True, "Macy's Credit Card Monthly Payment")
    discover_cc = Record("Discover CC", 60, 15, True, "Discover Credit Card Monthly Payment")

    needs.add_record(macy_cc)
    needs.add_record(discover_cc)

    print(needs.storage)
