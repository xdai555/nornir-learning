from tqdm import tqdm
from time import sleep
from nornir import InitNornir
from nornir.plugins.inventory.simple import SimpleInventory
from nornir.plugins.connections.netmiko import Netmiko
from nornir.core.deserializer.inventory import Inventory
import yaml


nr = InitNornir()
# import ipdb; ipdb.set_trace()
# alist = list(range(1,10000))
# bar = tqdm(alist)
# for letter in bar:
#     bar.set_description(f"Now get {letter}")
