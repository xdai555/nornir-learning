from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.plugins.tasks.files import write_file
import pathlib
from plugins.tasks import process_tasks


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


def config(task,nr):
    cmds = nr.inventory.hosts[task.host.name]["cmds"]
    print(cmds)
    pathlib.Path("gather_info").mkdir(exist_ok=True)
    r = task.run(
        task=netmiko_send_config,
        name=f"Gathering {task.host.name} {task.host.hostname}",
        config_commands=cmds,
        use_timing=True,
    )
    # task.host['backup'] = r.result
    w = task.run(
        task=write_file,
        filename=f"gather_info/{task.host.name}.log",
        content="\n\n" + f" {cmds} ".center(66,"#") + "\n" + r.result,
        append=True,
    )
    if not w.failed:
        print(f"{r.name} completed successfully!")
    return r.result,cmds


t = nr.run(task=config,nr=nr)
process_tasks(t,verbose=True)