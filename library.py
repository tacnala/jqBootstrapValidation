
from typing import Dict

import json
import os


class xdIdentity:
    id_dict:Dict = {
        "Identity": {}
    }

    @staticmethod
    def idme(class_object, object_name) -> int:
        me_class, me_name = class_object.__name__, object_name

        Identity.id_dict = Identity.load()

        if me_class in Identity.id_dict.keys():
            me_ids = [v for k, v in Identity.id_dict[me_class].items() if k == me_name]
            all_ids = [v for k, v in Identity.id_dict[me_class].items()]
            if len(me_ids) == 0:
                me_id = max(all_ids) + 1
            else:
                me_id = max(me_ids)
        

            Identity.id_dict[me_class] 

    @staticmethod
    def load():

        #check if library file exists
        #create if not (with current)
        if os.path.exists('Library\\identity.json'):
            with open('Library\\identity.json') as js_in:
                print('load: identity.json')
                return json.load(js_in)
        else:
            Identity.create()
            return Identity.id_dict
  
    @staticmethod
    def create():
        with open('Library\\identity.json','w') as js_out:
            json.dump(Identity.id_dict, js_out)
        print('create: identity.json')

        
















class Identity:
    """Purpose of this is to ID a class and keep it organized in a dictionary"""

    id_dict:Dict = {
        "dictionary": {}
    }

    @staticmethod
    def idme(class_object, object_name) -> int:
        """Returns Smallest Avaiable ID for its class"""

        Identity.load()
        me_class, me_name = class_object.__class__.__name__, object_name

        if me_class in Identity.id_dict.keys():
            me_ids = [k for k, v in Identity.id_dict[me_class].items() if v == me_name]
            if len(me_ids) != 0: return min(me_ids)

            id_existing = [int(k) for k in Identity.id_dict[me_class].keys()]
            id_out =  min([x for x in range(1,max(id_existing) + 2) if x not in id_existing])
            #id_out =  max(Identity._dict[class_name]) + 1

            Identity.id_dict[me_class][f'{id_out}'] = me_name
            Identity.store()
            return id_out
        else:
            Identity.id_dict[me_class] = {"1": me_name}
            Identity.store()
            return 1
        
        
    @staticmethod
    def rmme(class_object, object_id):
        """Removes ID from objects IDs"""
        Identity.load()
        class_name = class_object.__class__.__name__

        if class_name in Identity.id_dict.keys():
            if f'{object_id}' in Identity.id_dict[class_name].keys():
                del Identity.id_dict[class_name][f'{object_id}']
                print(f'delete: {class_name}.{object_id}')
                Identity.store()
                return
            
        print('warning: object(_id) DNE')
        
        
    @staticmethod
    def load():
        if os.path.isfile('Library\\identity.json'):
            with open('Library\\identity.json') as json_in:
                Identity.id_dict = json.load(json_in)
                print('load: identity.json')
        else:
            print('FILE DNE')
            Identity.create()

        if len(Identity.id_dict.keys()) == 0:
            print('Warning: No Identitys')   
    
    @staticmethod
    def store():

        if len(Identity.id_dict.keys()) == 0:
            print('Warning: No Identitys')

        with open('Library\\identity.json', 'w') as json_out:
            json.dump(Identity.id_dict, json_out)
            print('store: identity.json')

    @staticmethod
    def create():
        with open('Library\\identity.json','w') as js_out:
            json.dump(Identity.id_dict, js_out)
        print('create: identity.json')



class Store:

    @staticmethod
    def sheet(sheet_dict: Dict):
        return

