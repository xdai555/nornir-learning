from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


command = input('Pls input the commands splited by comma:')
cmds = command.split(',')

for cmd in cmds:
    nr = InitNornir()
    result = nr.run(
        task=netmiko_send_command,
        command_string=cmd,
    )
    import ipdb; ipdb.set_trace()
    print_result(result)

"""
通过 ipdb 进行追踪，查看结果对象
ipdb> result                                                                                                                         
AggregatedResult (netmiko_send_command): {'r1': MultiResult: [Result: "netmiko_send_command"]}
可以看到执行的结果是类似字典的，取值查看
ipdb> result['r1']                                                                                                                   
MultiResult: [Result: "netmiko_send_command"]

ipdb> result['r1'][0]                                                                                                                
Result: "netmiko_send_command"

ipdb> pp result['r1'][0].result                                                                                                      
('*down: administratively down\n'
 '(s): spoofing  (l): loopback\n'
 'Interface                Physical Protocol IP Address      Description \n'
 'GE0/0                    down     down     --              --\n'
 'GE0/1                    up       up       192.168.56.101  --\n'
 'GE0/2                    down     down     --              --\n'
 'GE5/0                    down     down     --              --\n'
 'GE5/1                    down     down     --              --\n'
 'GE6/0                    down     down     --              --\n'
 'GE6/1                    down     down     --              --\n'
 'Ser1/0                   down     down     --              --\n'
 'Ser2/0                   down     down     --              --\n'
 'Ser3/0                   down     down     --              --\n'
 'Ser4/0                   down     down     --              --')
ipdb>        

"""