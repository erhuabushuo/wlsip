import os.path

import ifaddr

def get_ips():
    ips = []
    adapters = ifaddr.get_adapters()
    for adapter in adapters:
        for ip in adapter.ips:
            if isinstance(ip.ip, str):
                ips.append(ip.ip)
    return ips


def get_script_directory():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))