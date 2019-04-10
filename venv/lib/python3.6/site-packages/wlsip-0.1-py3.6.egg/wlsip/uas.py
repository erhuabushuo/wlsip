import sys
import os.path
import subprocess
from tempfile import NamedTemporaryFile

import click

from .utils import get_script_directory

def uas(max_call_count, max_currency, cps, localhost, serverhost):
    """
    sipp 47.96.84.248:518 -sf xml/uas.xml -oocsf xml/ooc.xml -inf csv/callees.csv -m 1 -l 1 -r 1 -t un -i 10.10.10.106 -trace_msg -trace_err -message_file log/trace_msg.log -error_file log/trace_err.log
    """
    # 生成注册用户
    handle = NamedTemporaryFile(mode='wt', delete=False)
    handle.write('SEQUENTIAL\n')
    handle.write('# user, domain\n')
    for i in range(0, max_call_count):
        handle.write('9999{i};{serverhost}\n'.format(
            i=str(i),
            serverhost=serverhost
        ))
    handle.close()
    user_file_path = handle.name

    script_directory = get_script_directory()
    uas_xml_file_path = os.path.join(script_directory, 'xml/uas.xml')
    ooc_xml_file_path = os.path.join(script_directory, 'xml/ooc.xml')

    cmd = f"sipp {serverhost} -sf {uas_xml_file_path} -oocsf {ooc_xml_file_path} -inf {user_file_path} -m {max_call_count} -l {max_currency} -r {cps} -i {localhost} -trace_msg -trace_err -message_file /tmp/trace_msg.log -error_file /tmp/trace_err.log"
    subprocess.call(cmd, shell=True)
