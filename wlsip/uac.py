import sys
import os.path
import subprocess
from tempfile import NamedTemporaryFile

import click

from .utils import get_script_directory

def uac(max_call_count, max_currency, cps, localhost, serverhost):
    # 生成注册用户
    handle = NamedTemporaryFile(mode='wt', delete=False)
    handle.write('SEQUENTIAL\n')
    handle.write('# user, domain, callee\n')
    for i in range(0, max_call_count):
        handle.write('9999{i};{serverhost};8888{i}\n'.format(
            i=str(i),
            serverhost=serverhost
        ))
    handle.close()
    user_file_path = handle.name

    script_directory = get_script_directory()
    uac_xml_file_path = os.path.join(script_directory, 'xml/uac.xml')

    cmd = f"sipp {serverhost} -sf {uac_xml_file_path} -aa -inf {user_file_path} -m {max_call_count} -l {max_currency} -r {cps} -t un -i {localhost} -default_behaviors all -trace_msg -trace_err -message_file /tmp/trace_msg.log -error_file /tmp/trace_err.log  -trace_stat -stf uac_stat.csv"
    print(cmd)
    subprocess.call(cmd, shell=True)
