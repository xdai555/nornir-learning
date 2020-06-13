from nornir.core.task import Result, Task


def napalm_compare_config(task: Task,) -> Result:
    conn = task.host.get_connection("napalm", task.nornir.config)
    result = conn.compare_config()
    return Result(host=task.host, result=result)
