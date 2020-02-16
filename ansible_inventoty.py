# 将 Ansible 迁移到 Nornir，加载主机文件时用到 AnsibleInventory 插件
from nornir import InitNornir
from nornir.plugins.inventory.ansible import AnsibleInventory
from some_tasks import backup_config,process_tasks
from nornir.plugins.functions.text import print_result,print_title
from nornir.core.exceptions import NornirSubTaskError,NornirExecutionError


nr =InitNornir(config_file="./myconfig.yaml")
test = nr.run(task=backup_config)
# import ipdb; ipdb.set_trace()
process_tasks(test,verbose=True)

"""
通过 ipdb 进行追踪调试
ipdb> pp nr.inventory.hosts                                                                                                          
{'asw1': Host: asw1,
 'asw2': Host: asw2,
 'csw1': Host: csw1,
 'csw2': Host: csw2,
 'dsw1': Host: dsw1,
 'dsw2': Host: dsw2}
ipdb> pp nr.inventory.groups                                                                                                         
{'asw': Group: asw, 'csw': Group: csw, 'dsw': Group: dsw}

查看主机变量，使用data无法查看到全局变量
ipdb> pp nr.inventory.hosts['csw1'].data                                                                                             
{'pass': 'passwd', 'user': 'admin'}
但是可以通过items()看到全部的变量
ipdb> pp nr.inventory.hosts['csw1'].items()                                                                                          
dict_items([('user', 'admin'), ('pass', 'passwd'), ('ntp', '1.1.1.1')])
"""