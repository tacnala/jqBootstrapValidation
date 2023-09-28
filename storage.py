
from statement import Sheet, Record
from typing import List, Dict

import json, os


class Storage:

    def __init__(self):
        self.sheets: Dict[str, Sheet] = {}

        if os.path.exists('Library\\sheets.json'):
            self.load_sheets()

    def add_sheet(self, sheet: Sheet):
        assert sheet.name not in self.sheets.keys(), 'sheet name already exists !!'
        self.sheets[sheet.name] = sheet

    def store_sheets(self):
        if not os.path.exists('Library\\sheets.json'): Storage.json_create('sheets.json')
        with open('Library\\sheets.json') as js_in:
            tmp_js = json.load(js_in)

        for sheet_name, sheet in self.sheets.items():
            tmp_js[sheet_name] = sheet.storage

        with open('Library\\sheets.json', 'w') as js_out:

    def load_sheets(self):
        if not os.path.exists('Library\\sheets.json'):
            print('error: No sheets file found')
            return
        
        storage: Dict
        with open('Library\\sheets.json') as js_in:
            storage = json.load(js_in)
            assert len(storage.keys()) != 0, 'no Sheets exist in stored file!!'

        for sheet_name in storage.keys():
            sheet_info: Dict = storage[sheet_name]["info"]
            sheet_records: List = storage[sheet_name]["records"]

            sheet = Sheet(**sheet_info)
            record_dict: Dict
            for record_dict in sheet_records:
                sheet.add_record(Record(**record_dict))
                print(f'storage: {sheet_name}:: loaded record {record_dict["name"]}')

            self.sheets[sheet_name] = sheet
            print(f'storage: loaded sheet {sheet_name}')

    @staticmethod
    def json_create(file_name):
        with open('Library\\'+file_name, 'w') as js_out:
            json.dump({},js_out)


def test_create():

    main_storage = Storage()

    main_storage.add_sheet(Sheet("Needs"))
    main_sheets = main_storage.sheets

    # macy_cc = Record("Macy CC", 36.0, 2, True, "Macy's Credit Card Monthly Payment")
    # discover_cc = Record("Discover CC", 60, 15, True, "Discover Credit Card Monthly Payment")

    main_sheets["Needs"].add_record(Record("Macy CC", 36.0, 2, True, "Macy's Credit Card Monthly Payment"))
    main_sheets["Needs"].add_record(Record("Discover CC", 60, 15, True, "Discover Credit Card Monthly Payment"))

    main_storage.store_sheets()

def test_load():
    main_storage = Storage()

    print(main_storage.sheets)

    print(main_storage.sheets["Needs"].storage)


if __name__ == '__main__':
    print('Running storage.py ...')
    # test_create()
    test_load()

    














