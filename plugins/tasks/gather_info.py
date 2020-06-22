import pathlib
from nornir.plugins.tasks.files import write_file
from nornir.plugins.tasks.networking import netmiko_send_command


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
            content="\n\n" + f" {cmd} ".center(66,"#") + "\n" + r.result,
            append=True,
        )
        if not w.failed:
            print(f"{r.name} completed successfully!")
    else:
        return r.result,cmd