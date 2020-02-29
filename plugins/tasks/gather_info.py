import pathlib,os,openpyxl
from nornir.plugins.tasks.files import write_file
from nornir.plugins.tasks.networking import netmiko_send_command
import pandas as pd
from nornir.core.task import Task


def gather_info(task,cmd,parse=False):
    """
    """
    # 创建存放备份配置的目标文件夹
    pathlib.Path("gather_info").mkdir(exist_ok=True)
    r = task.run(
        task=netmiko_send_command,
        name=f"Gathering {task.host.name} {task.host.hostname}",
        command_string= cmd,
        use_timing=True,
        use_textfsm=parse,
    )
    # task.host['backup'] = r.result
    if not parse:
        w = task.run(
            task=write_file,
            filename=f"gather_info/{task.host.name}.log",
            content=r.result
        )
        if not w.failed:
            print(f"{r.name} completed successfully!")
    else:
        return r.result,cmd


# 多线程写入会存在 IO 问题，若使用进程锁，执行速度会变慢
# TODO：将解析返回的列表放入全局字典中，一次性写入
# def to_excel(result,cmd,sheet_name,all_in_one=False):
#     file_name = f"{cmd}.xlsx"
    # if not os.path.exists(file_name):
    #     wb = openpyxl.Workbook()
    #     wb.save(file_name)
    # writer = pd.ExcelWriter(file_name)
    # writer.book = openpyxl.load_workbook(file_name)
    # if not all_in_one:
    #     df = pd.DataFrame(result)
    #     with pd.ExcelWriter(file_name) as writer:
    #         writer.book = openpyxl.load_workbook(file_name)
    #         df.to_excel(writer,sheet_name=sheet_name,index=False)
    #         print("Done")
    # else:
    #     info_dict = {}
    #     for dic in result:
    #         info_dict.update(dic)
    #     info_dict['IP'] = sheet_name


info_temp_list = []