from nornir.plugins.tasks.files import write_file
from nornir.core.task import Task
import sys,pathlib,re,os,time,openpyxl
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
                print("#"*15 + f" {task.name} error "  + "#"*15)
                print(fail.result)
        else:
            print(f"Task {task.name} has the following errors:\n{i} {j}")


def parse_vpn_instance():
    pass    

def backup_startup_config(task):
    """
    Parse startup file name and put it into server.
    """
    pass


def parse_to_excel(task,all_in_one=False):
    """
    For gather_info.py textfsm to excel.
    """
    info_all = []
    # gather_info函数返回值为列表，其中的result为AggregateResult对象，对数据进行分解并判断
    for name,result in task.items():
        hostname = name
        info = result.result[0]
        cmd = result.result[1]
        # TODO: 如果task错误的情况，如何不添加文件名
        file_name = f"{cmd}.xlsx"
        # 判断目标excel文件是否存在，不存在则创建
        if not os.path.exists(file_name):
            wb = openpyxl.Workbook()
            wb.save(file_name)
        # 判断解析值是否为列表，列表写入excel；解析失败则原始字符串写入文件
        if type(info) is str:
            print(info)
            pathlib.Path("gather_info").mkdir(exist_ok=True)
            with open(f'./gather_info/{hostname}.log','w') as f:
                f.write(info)
        else:
            # all_in_one 作用是将所有的信息放在同一个sheet页,例如收集所有的设备的软件版本
            # not all_in_one 则是把每个信息都按照hostname放入不同的sheet页。例如收集所有设备的mac地址表
            if not all_in_one:
                df = pd.DataFrame(info)
                # 写入opeyxl加载的工作簿，防止pandas重写文件。
                # write操作放在`for`循环内，是为了遍历`hostname`作为`sheet`页的名字
                with pd.ExcelWriter(file_name) as writer:
                    writer.book = openpyxl.load_workbook(file_name)
                    df.to_excel(writer,sheet_name=hostname,index=False)
            else:
                # all_in_one 的write操作要放在循环体外面，因为内容不确定，无法追加sheet，且sheet名不能重复
                # 此处将`hostname`也写入info中，并返回重构后的所有内容（用到了开头定义的 info_all）
                info_dict = {}
                for dic in info:
                    info_dict.update(dic)
                    info_dict["hostname"] = hostname
                    info_all.append(info_dict)
    if all_in_one:
        df = pd.DataFrame(info_all)
        df.to_excel(file_name,sheet_name=cmd,index=False)
    print(f"Parse_to_excel completed. See {file_name}")

                    # info_all.append(info_dict)
    # df = pd.DataFrame(info_all)
    # if not all_in_one:
    #     df.to_excel(file_name,sheet_name=hostname,index=False)
    # else:
    #     df.to_excel(file_name,sheet_name=cmd,index=False)
    # pass




if __name__ == "__main__":
    pass