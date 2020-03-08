# pip install nornir
from nornir import InitNornir
from plugins.tasks import backup_running_config,process_tasks


device_file = input("Input your filename (csv or excel):")
nr = InitNornir(
    inventory = {
        "plugin": "plugins.inventory.custom_inventory.CustomInventory",
        "options": {
            "filename": device_file,
        }
    }
)
# print(nr.inventory.hosts)
backup = nr.run(backup_running_config)
process_tasks(backup,verbose=True)