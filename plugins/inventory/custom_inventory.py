from nornir.core.deserializer.inventory import Inventory
import pandas as pd


class CustomInventory(Inventory):
    def __init__(self, **kwargs):
        """
        Module pandas is required.
        A very simple inventory plugin to handle csv/excel file.
        Your file must have this keys:'host', 'username', 'password', 'device_type', 'device_name'
        The 'device_name' is alias of device(e.g. r1,sw1 and so on), and other keys is always used in netmiko.
        """
        hosts = self.get_file_content(kwargs["filename"])
        groups = {}
        defaults = {}

        super().__init__(hosts=hosts, groups=groups, defaults=defaults, **kwargs)

    def get_file_content(self,filename: str):
        # df : This host format can be used in netmiko directly.
        if ".csv" in filename.lower():
            df = pd.read_csv(filename)[['host', 'username', 'password', 'device_type', 'device_name']].to_dict(orient='records')
        else:
            df = pd.read_excel(filename)[['host', 'username', 'password', 'device_type', 'device_name']].to_dict(orient='records')
        hosts = {}
        for item in df:
            host = {
                item["device_name"]:{
                        'hostname': item["host"],
                        'password': item["password"],
                        'platform': item["device_type"],
                        'username': item["username"]
                        }
                }
            hosts.update(host)
        return hosts
