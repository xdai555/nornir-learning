from nornir import InitNornir
from plugins.tasks import gather_info,process_tasks,parse_to_excel
import os,pathlib


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

cmd = input("Input the command:")
parse = input("Parse output to Excel?(Y/N)")
if "y" in parse.lower():
    parse = True
    # 如果要解析内容，需要添加系统环境变量（引用另一个项目），根据实际情况更换路径
    # 如果是思科或其他厂商，可以 `pip install ntc-template`，环境变量设为该项目的路径
    template_dir = '/home/eric/textfsm_hpe_cmw7/templates'
    # windows系统改成以下路径（举例）
    # template_dir = "D:\\test\\textfsm_hpe_cmw7_templates"
    os.environ["NET_TEXTFSM"] = template_dir
else:
    parse = False

t = nr.run(gather_info, cmd=cmd, parse=parse)

process_tasks(t,verbose=False)

# 如果需要放到同一个sheet页,修改one_sheet = True
if parse:
    parse_to_excel(t,one_sheet=False)


"""
1、将该脚本及项目文件夹 plugins 放到同级目录，如果涉及解析文本，需要下载另一个项目（textfsm_hpe_cmw7），并修改脚本路径
2、设备信息为CSV格式，且表头需包含'host', 'username', 'password', 'device_type', 'device_name'
3、运行之后，按提示输入命令，设备用户需要有screen-dis及dis权限
4、如果不解析文本到excel，会按设备名写入到 gather_config 文件夹，解析失败的也会写到文件夹
5、解析文本可选择放到一个sheet（如设备版本号）或者按设备名放入多个sheet（如数量较多的表项），按实际情况来定。
6、失败的主机会显示出来，可手动进行重试，或用 verbose 查看具体原因
"""
