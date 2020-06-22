from nornir.plugins.tasks.files import write_file
from nornir.core.task import Task
import sys,pathlib,re,os,time
# import openpyxl
import pandas as pd


# 此文件存放一些不会被 nornir 对象直接调用的任务，一般用来处理任务


def process_tasks(
    task: Task, 
    verbose: bool = False, 
    write_file: bool = False
    ):
    """
    verbose (`bool`): if True, print verbose errors.  
    write_file (`bool`): if True, write log to file.
    """
    if not task.failed:
        print(f"Task {task.name} completed successfully!")
    for i,j in task.failed_hosts.items():
        if verbose:
            for fail in j:
                print(f" {task.name} error ".center(66,"*"))
                print(fail.result)
        else:
            print(f"ERROR:{i} {j}")

def parse_vpn_instance():
    pass    

def backup_startup_config(task):
    """
    Parse startup file name and put it into server.
    """
    pass


def parse_to_excel(task,one_sheet=False):
    """
    For gather_info.py textfsm to excel.
    """
    print(" Start parsing output ".center(66,"*"))
    # import ipdb; ipdb.set_trace()
    info_all = []
    # gather_info函数返回值为列表，其中的result为AggregateResult对象，对数据进行分解处理
    for name,result in task.items():
        hostname = name
        info = result.result[0]
        cmd = result.result[1]
        # 如果提取出来的cmd是一个字符，说明任务执行错误。
        if len(cmd) > 1:
            file_name = f"{cmd}.xlsx"
            # 判断目标excel文件是否存在，不存在则创建
            if not os.path.exists(file_name):
                wb = openpyxl.Workbook()
                wb.save(file_name)
        else:
            print(f"ERROR:Can't parse output, please check task gather_info: {hostname}")
        # 判断解析值是否为列表，列表写入excel；解析失败则原始字符串写入文件
        if type(info) is str:
            if len(info) != 1:
                pathlib.Path("gather_info").mkdir(exist_ok=True)
                with open(f'./gather_info/{hostname}.log','w') as f:
                    f.write("\n\n" + f" {cmd} ".center(66,"#") + "\n" + info)
            else:
                pass
        else:
            # one_sheet 作用是将所有的信息放在同一个sheet页,例如收集所有的设备的软件版本
            # not one_sheet 则是把每个信息都按照hostname放入不同的sheet页。例如收集所有设备的mac地址表
            if not one_sheet:
                df = pd.DataFrame(info)
                # 写入opeyxl加载的工作簿，防止pandas重写文件。
                # write操作放在`for`循环内，是为了遍历`hostname`作为`sheet`页的名字
                with pd.ExcelWriter(file_name) as writer:
                    writer.book = openpyxl.load_workbook(file_name)
                    df.to_excel(writer,sheet_name=hostname,index=False)
            else:
                # one_sheet 的write操作要放在循环体外面，因为内容不确定，无法追加sheet，且sheet名不能重复
                # 此处将`hostname`也写入info中，并返回重构后的所有内容（用到了开头定义的 info_all）
                info_dict = {}
                for dic in info:
                    info_dict.update(dic)
                    info_dict["hostname"] = hostname
                    info_all.append(info_dict)
    if one_sheet:
        df = pd.DataFrame(info_all)
        with pd.ExcelWriter(file_name) as writer:
            writer.book = openpyxl.load_workbook(file_name)
            df.to_excel(writer,sheet_name="one_sheet",index=False)
    print("\n" + " Parsing completed ".center(66,"*"))
    print(f"Parse_to_excel completed. See \"{file_name}\"")
    print("If excel file is blank, see output in \"gather_info\" directory.")


if __name__ == "__main__":
    pass