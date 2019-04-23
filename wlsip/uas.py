import sys
import os.path
import subprocess
from tempfile import NamedTemporaryFile

import click

from .utils import get_script_directory

def uas(max_call_count, max_currency, cps, localhost, serverhost):
    # 生成注册用户
    handle = NamedTemporaryFile(mode='wt', delete=False)
    handle.write('SEQUENTIAL\n')
    handle.write('# user, domain\n')
    for i in range(0, max_call_count):
        handle.write('8888{i};{serverhost}\n'.format(
            i=str(i),
            serverhost=serverhost
        ))
    handle.close()
    user_file_path = handle.name

    script_directory = get_script_directory()
    uas_xml_file_path = os.path.join(script_directory, 'xml/uas.xml')
    ooc_xml_file_path = os.path.join(script_directory, 'xml/ooc.xml')

    cmd = f"sipp {serverhost} -sf {uas_xml_file_path} -aa -oocsf {ooc_xml_file_path} -inf {user_file_path} -m {max_call_count} -l {max_currency} -r {cps} -t un -i {localhost} -default_behaviors bye -trace_msg -trace_err -message_file /tmp/trace_msg.log -error_file /tmp/trace_err.log  -trace_stat -stf uas_stat.csv"
    print(cmd)
    subprocess.call(cmd, shell=True)
