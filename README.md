# README

## Required

Python3.5+

```bash
pip install nornir
pip install pandas
pip install xlwt
pip install xlrd
```

## Use

`ansible_inventoty.py`: An example to parse ansible hosts file.

`custom_csv_inventoty.py`: A custom inventory plugin to parse csv file.

`hp_comware_running_config_backup.py`: Backup running config to file

### hp_comware_gather_info.py

#### 使用

下载所有文件即可

#### 功能（更新……）

1. 批量登录设备，执行单条命令，一般用来收集信息
2. 将收集到的信息按照设备名称保存到`gather_info`文件夹
3. 将收集到的信息解析之后保存到 excel 文件中，默认按设备名称区分 sheet ，也可将全部结果放入同一个 sheet

#### 参数

1. `Parse output to Excel?(Y/N)`: parse=True 会把设备返回的内容格式化，如果模板错误或不存在，则将内容保存到文件中
2. `process_tasks(t,verbose=False)` : 修改verbose=True 可以显示任务执行中的详细错误信息
3. `parse_to_excel(t,one_sheet=False)`: 修改one_sheet=True 可以将收集到的所有信息保存到同一个 excel sheet 页中

#### 使用自定义系统环境变量

如果要解析输出，需要自行脚本中修改系统环境变量。

##### HPE Comware

下载 [textfsm_hpe_cmw7](https://github.com/odai5/textfsm_hpe_cmw7) 中的 `templates` 文件夹保存到本地。

1. Linux  
直接修改脚本的路径(line 24)，或者`bash`运行：

```bash
# 修改为自己的路径
export NET_TEXTFSM=/path/to/textfsm_hpe_cmw7/templates/
```

2. Windows  
我的电脑，右键【属性】--->【高级系统设置】--->【环境变量】--->【新建】--->变量名：`NET_TEXTFSM` 变量值（举例，按实际写）：`D:\textfsm_hpe_cmw7\templates`  
然后取消注释并修改脚本中的路径(line 26)，注意路径中的 `\\`，注释掉 line 24 。

## 有什么用？

专业网工，业余写脚本，重复造轮子！！！

## 小脚本更新记录

2020/03/08：优化`gather_info`保存输出到文件功能，修改为追加模式并写入执行的命令，用来区分多次执行的结果；`hp_comware_gather_info.py`增加多条命令支持，可一次性收集多条信息  
2020/03/04: 更新主机插件，现在可支持 csv 和 excel 文件  
2020/03/02: 更新`parse_to_excel`，可以将所有输出保存在同一个 sheet 页中  
2020/03/01：增加`parse_to_excel`，将设备输出的结果解析后保存到 excel 文件中，解析失败则写入文本文件  
2020/02/26：调整`plugins/tasks`目录结构，分离任务模块；增加`gather_info`任务，用来收集设备输出信息，并写入到文本文件  
2020/02/24：更新`process_tasks`，调整 verbose 输出  
2020/02/20：添加 csv 主机插件，可从 csv 文件解析设备信息  
2020/02/16：初次学习`Nornir`，主要以 HP_Comware 设备为验证对象进行学习
