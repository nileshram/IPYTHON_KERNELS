'''
Created on 24 Feb 2020

@author: nilesh
'''
from jupyter_client import BlockingKernelClient

Echo = BlockingKernelClient()
Echo.load_connection_file("/home/nilesh/.local/share/jupyter/runtime/kernel-30357.json")

#Echo.start_channels()
while True:
    data = input("?")
    Echo.execute(data)
    #print(Echo.get_shell_msg())
    print(Echo.get_iopub_msg())