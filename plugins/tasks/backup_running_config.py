import pathlib
from nornir.plugins.tasks.files import write_file
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.core.task import Task


def backup_running_config(task: Task):
    """
    Use netmiko_sent_command task backup running-config to "back_config" dir.  
    `screen-length disable` privilege is required.
    """
    # 创建存放备份配置的目标文件夹
    pathlib.Path("backup_config").mkdir(exist_ok=True)
    r = task.run(
        task=netmiko_send_command,
        name=f"Backup {task.host.name} {task.host.hostname}",
        command_string="display current-configuration",
        use_timing=True,
    )
    # task.host['backup'] = r.result
    if not r.failed:
        print(f"{r.name} completed successfully!")
    task.run(
        task=write_file,
        filename=f"backup_config/{task.host.name}.cfg",
        content=r.result
    )