from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.plugins.tasks.files import write_file
import pathlib
from plugins.tasks import process_tasks,config


device_file = 'hosts_example.csv'
cmds_file = "cmds"
nr = InitNornir(
    core={"num_workers": 20},
    inventory={
        "plugin": "plugins.inventory.custom_inventory.CustomInventory",
        "options": {
            "filename": device_file,
            "cmds_file": cmds_file
        }
    },
    dry_run=False,
)

t = nr.run(task=config,nr=nr)
process_tasks(t,verbose=True)