import subprocess
import datetime
import os
import re
import time

def tracker():

    while True:

        init = ['git', 'init']
        status = ['git', 'status']
        add = ['git', 'add', '.']
        connect = ['git', 'remote', 'add', 'origin', 'https://github.com/1ms17me105/test_git1.git']
        commit = ['git', 'commit', '-m', f'{datetime.datetime.now()}']
        push = ['git', 'push', '-u', 'origin', 'main']

        if not os.path.isdir('.git'):
            subprocess.call(init)

        PIPE = subprocess.PIPE

        def process(action):
            command = subprocess.Popen(action, stdout = PIPE, stderr = PIPE)
            stdoutput, error = command.communicate()
            return {'output': stdoutput.decode("utf-8"), 'error': error.decode("utf-8")}
        
        remote_connect = process(connect)

        status_check = process(status)

        if re.search(r'\nChanges not staged for commit:\n', status_check['output']):
            stage = process(add)

        if re.search(r'\nUntracked files:\n', status_check['output']):
            comm = process(commit)

        pushing = process(push)

        print(f'Pushed now!')

        time.sleep(60)

tracker()