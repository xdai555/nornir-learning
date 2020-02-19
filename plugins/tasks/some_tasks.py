
import sys,pathlib
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.text import template_file
from nornir.plugins.tasks.files import write_file
from nornir.plugins.tasks.networking import netmiko_send_command


def render_config(task):
    # 这里的 "j2_template_file",需要增加hosts文件的变量，对应模板文件
    j2 = task.host["j2_template_file"]
    # 创建存放配置的目标文件夹，若文件夹已存在则忽略
    pathlib.Path("desired_config").mkdir(exist_ok=True)
    # 运行任务"template_file"来渲染生成配置，模板存放在"templates"目录下
    r = task.run(
        task=template_file,
        name="Base Template Configuration",
        template=j2,
        path="templates",
        **task.host
    )
    # 返回的结果为渲染后的配置，将它存放在主机变量中
    # task.host["config"] = r.result
    task.run(
        task=write_file,
        filename=f"desired_config/{task.host.name}",
        content=r.result
    )


def backup_config(task):
    # 创建存放备份配置的目标文件夹
    pathlib.Path("backup_config").mkdir(exist_ok=True)
    # 执行dis cur命令，用户需要 screen-length disable 权限
    r = task.run(
        task=netmiko_send_command,
        name=f"Backup {task.host.name}",
        command_string="display current-configuration",
        use_timing=True,
    )
    # task.host['backup'] = r.result
    task.run(
        task=write_file,
        filename=f"backup_config/{task.host.name}",
        content=r.result
    )


def process_tasks(task, verbose=False):
    """
    verbose (`bool`): if True, print verbose errors.
    """
    if not task.failed:
        print(f"Task {task.name} completed successfully!")
    if verbose:
        task.raise_on_error()
    else:
        for i,j in task.failed_hosts.items():
            print(f"Task {task.name} has the following errors:\n{i} {j}")


if __name__ == "__main__":
    pass