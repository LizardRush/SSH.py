import subprocess
import platform
import json

hostname = json.load(open("./info.json"))["hostname"]
username = json.load(open("./info.json"))["username"]

def open_ssh_terminal(hostname, username):
    ssh_command = f'ssh {username}@{hostname}'

    os_name = platform.system()
    
    if os_name == 'Darwin':
        subprocess.run(['osascript', '-e', f'tell application "Terminal" to do script "{ssh_command}"'])
    elif os_name == 'Linux':
        subprocess.run(['gnome-terminal', '--', 'bash', '-c', ssh_command])
    elif os_name == 'Windows':
        subprocess.run(['start', 'cmd', '/k', ssh_command], shell=True)
    else:
        print(f"Unsupported OS: {os_name}")

open_ssh_terminal(hostname, username)
