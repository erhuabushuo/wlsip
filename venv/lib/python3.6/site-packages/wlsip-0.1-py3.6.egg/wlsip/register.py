import sys
import os.path
import subprocess
from tempfile import NamedTemporaryFile

import click

from .utils import get_script_directory

def register(max_call_count, max_currency, cps, localhost, serverhost):
    """
    sipp 47.96.84.248:518 -sf xml/register.xml -inf csv/user_data.csv -m 100 -l 100 -r 100 -t un -i 192.168.0.115 -trace_msg -trace_err -message_file log/trace_msg.log -error_file log/trace_err.log
    """
    # 生成注册用户
    handle = NamedTemporaryFile(mode='wt', delete=False)
    handle.write('SEQUENTIAL\n')
    handle.write('# user, domain\n')
    for i in range(0, max_call_count):
        handle.write('test_{i};{serverhost}\n'.format(
            i=str(i),
            serverhost=serverhost
        ))
    handle.close()
    user_file_path = handle.name

    script_directory = get_script_directory()
    xml_file_path = os.path.join(script_directory, 'xml/register.xml')

    cmd = f"sipp {serverhost} -sf {xml_file_path} -inf {user_file_path} -m {max_call_count} -l {max_currency} -r {cps} -i {localhost} -trace_msg -trace_err -message_file /tmp/trace_msg.log -error_file /tmp/trace_err.log"
    subprocess.call(cmd, shell=True)