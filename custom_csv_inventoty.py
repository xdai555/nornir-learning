from nornir import InitNornir
from pprint import pprint

# nr = InitNornir(config_file='myconfig.yaml')
nr = InitNornir(
    inventory = {
        "plugin": "plugins.inventory.custom_inventory.CustomInventory",
        "options": {
            "filename": "test.xlsx",
        }
    }
)
pprint(nr.inventory.hosts)