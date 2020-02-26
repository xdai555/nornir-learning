# pip install nornir
from nornir import InitNornir
from plugins.tasks import backup_running_config,process_tasks


"""
1、将该脚本及项目文件夹 plugins 放到同级目录
2、设备信息为CSV格式，且表头需包含'host', 'username', 'password', 'device_type', 'device_name'
3、运行之后，用户需要有screen-dis及dis cur 权限，配置会按设备名写入到 backup_config 文件夹
4、失败的主机会显示出来，可手动进行重试
"""
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