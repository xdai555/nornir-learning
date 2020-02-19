# 将 Ansible 迁移到 Nornir，加载主机文件时用到 AnsibleInventory 插件
# Migrating Ansible to Nornir, using AnsibleInventory plugin when loading host files
from nornir import InitNornir
# from nornir.plugins.inventory.ansible import AnsibleInventory
from plugins.tasks.some_tasks import backup_config,process_tasks
from nornir.plugins.functions.text import print_result,print_title
from pprint import pprint


# Notice: options-hostsfile, not the default ``host_file``
nr = InitNornir(
    inventory={
        "plugin": "nornir.plugins.inventory.ansible.AnsibleInventory",
        "options": {
            "hostsfile": "hosts",
        }
    }
)
import ipdb; ipdb.set_trace()
# test = nr.run(task=backup_config)
# process_tasks(test)



"""
# use ipdb to dive into hosts's variables
ipdb> pp nr.inventory.hosts                                                                                                          
{'192.168.56.103': Host: 192.168.56.103, 'asw1': Host: asw1, 'asw2': Host: asw2}
ipdb> pp nr.inventory.groups                                                                                                         
{'asw': Group: asw, 'csw': Group: csw}

# ``.data`` can show host vars ,but can not show gloable vars(defined in [all:vars])
ipdb> pp nr.inventory.hosts['asw2'].data                                                                                             
{'passwd': 'passwd', 'user': 'user'}
# ``.items()`` can show all vars
ipdb> pp nr.inventory.hosts['asw2'].items()                                                                                          
dict_items([('passwd', 'passwd'), ('user', 'user'), ('ntp_server', '1.1.1.1')])
# some connection variables have fixed key(username,password,port),use`.`method.
ipdb> nr.inventory.hosts['asw2'].username                                                                                            
'admin'
ipdb> nr.inventory.hosts['asw2']. 
  close_connection()          dict()                      has_parent_group()          password                     
  close_connections()         get()                       hostname                    platform                     
  connection_options          get_connection()            items()                     port                         
  connections                 get_connection_parameters() keys()                      username                    >
  data                        get_connection_state()      name                        values()                     
  defaults                    groups                      open_connection()           .git/   
"""