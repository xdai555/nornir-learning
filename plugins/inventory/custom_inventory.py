from nornir.core.deserializer.inventory import Inventory
import pandas as pd
import configparser
from nornir.core.inventory import ConnectionOptions


class CustomInventory(Inventory):
    def __init__(self, **kwargs):
        """
        Module pandas is required.
        A very simple inventory plugin to handle csv/excel file.
        Your file must have this keys:'host', 'username', 'password', 'device_type', 'device_name'
        The 'device_name' is alias of device(e.g. r1,sw1 and so on), and other keys is always used in netmiko.
        """
        hosts = self._hosts(self.get_file_content(kwargs["filename"],))
        groups = self._groups_data(kwargs["cmds_file"])
        defaults = {}
        super().__init__(hosts=hosts, groups=groups, defaults=defaults, **kwargs)

    def get_file_content(self, filename: str):
        # df : This host format can be used in netmiko directly.
        if ".csv" in filename.lower():
            df = pd.read_csv(filename)[['host', 'username', 'password', 'device_type', 'device_name', 'groups', 'secret']].fillna("").to_dict(orient='records')
        else:
            df = pd.read_excel(filename)[['host', 'username', 'password', 'device_type', 'device_name', 'groups', 'secret']].\
                to_dict(orient='records')
        return df

    @staticmethod
    def _hosts(df):
        hosts = {}
        for item in df:
            host = {
                item["device_name"]:
                    {
                        'hostname': item["host"],
                        'password': item["password"],
                        'platform': item["device_type"],
                        'username': item["username"],
                        'groups': [item["groups"], ],
                        'connection_options':{
                            "netmiko":{
                                "extras": {
                                        "secret": item["secret"],   
                                }
                            }
                            },
                        }
                }
            hosts.update(host)
        return hosts


    @staticmethod
    def _groups(df):
        groups = {}
        for item in df:
            group = {item['']}
        groups.update(group)
        return groups
    
    
    @staticmethod
    def _data(df):
        pass

    @staticmethod
    def _groups_data(cmds_file):
        """
        Add commands to groups's data fields to exec.
        :param cmds_file: commands file,section's name is group name and option is network device command
        :return: group data dict
        """
        groups = {}
        conf = configparser.ConfigParser(allow_no_value=True)
        conf.read(cmds_file)
        for i in conf.sections():
            cmds = []
            for _ in conf.items(i):
                cmds.append(_[0])
            data = {
                i: {
                    "data": {"cmds": cmds}
                },
            }
            groups.update(data, )
        return groups