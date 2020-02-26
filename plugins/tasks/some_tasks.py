from nornir.core.task import Task
import sys,pathlib,re,os,time


# 此文件存放一些不会被 nornir 调用的任务


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






if __name__ == "__main__":
    pass