# README

## Required

Python3.5+

```bash
pip install nornir
pip install pandas
pip install xlwt
```

## Use

`ansible_inventoty.py`: An example to parse ansible hosts file.

`custom_csv_inventoty.py`: A custom inventory plugin to parse csv file.

`hp_comware_running_config_backup.py`: Backup running config to file

### hp_comware_gather_info.py

#### 使用

下载所有文件即可

#### 功能

1. 批量登录设备，执行单条命令，一般用来收集信息
2. 将收集到的信息按照设备名称保存到`gather_info`文件夹
3. 也可以将收集到的信息解析为格式化之后保存到 excel 文件中

#### 参数

1. `Parse output to Excel?(Y/N)`: parse=True 会把设备返回的内容格式化，如果模板错误或不存在，则将内容保存到文件中
2. `process_tasks(t,verbose=False)` : 修改verbose=True 可以显示任务执行中的详细错误信息
3. `parse_to_excel(t,one_sheet=False)`: 修改one_sheet=True 可以将收集到的所有信息保存到同一个 excel sheet 页中

#### 注意

如果要解析输出，需要自行修改系统环境变量。

#### 有什么用？

重复造轮子！
