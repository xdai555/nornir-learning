from nornir import InitNornir
from plugins.tasks import gather_info,process_tasks
import os,pathlib


# 如果需要解析内容，添加临时环境变量，请根据实际情况更换路径
template_dir = '/home/eric/textfsm_hpe_cmw7/templates'
# template_dir = "D:\\test\\textfsm_hpe_cmw7_templates"
os.environ["NET_TEXTFSM"] = template_dir
# 以上函数尚未实现，忽略

# 初始化主机文件，从csv读取主机信息
csv_file = input("Input csv_file name :")
# csv_file = "test.csv"
nr = InitNornir(
    inventory = {
        "plugin": "plugins.inventory.csv_inventory.CsvInventory",
        "options": {
            "csv_file": csv_file,
        }
    }
)



cmd = input('Input the command:')
t = nr.run(gather_info, cmd=cmd)
process_tasks(t,verbose=True)

"""
1、将该脚本及项目文件夹 plugins 放到同级目录
2、设备信息为CSV格式，且表头需包含'host', 'username', 'password', 'device_type', 'device_name'
3、运行之后，按提示输入命令，设备用户需要有screen-dis及dis权限
4、会按设备名写入到 backup_config 文件夹
5、失败的主机会显示出来，可手动进行重试，或用 verbose 查看具体原因
"""
