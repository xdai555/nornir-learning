from nornir import InitNornir
from pprint import pprint
from plugins.inventory.csv_inventory import CsvInventory

nr = InitNornir(config_file='myconfig.yaml')
pprint(nr.inventory.hosts)