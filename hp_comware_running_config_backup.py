from nornir import InitNornir
from plugins.tasks.some_tasks import backup_running_config,process_tasks


csv_file = input("Input csv_file name :")
nr = InitNornir(
    inventory = {
        "plugin": "plugins.inventory.csv_inventory.CsvInventory",
        "options": {
            "csv_file": csv_file,
        }
    }
)
# print(nr.inventory.hosts)
backup = nr.run(backup_running_config)
process_tasks(backup,verbose=True)