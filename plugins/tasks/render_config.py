import pathlib
from nornir.plugins.tasks.text import template_file
from nornir.plugins.tasks.files import write_file
from nornir.core.task import Task


def render_config(task: Task):
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
