import shlex
import os
import subprocess


def get_env(env):
    process_env = os.environ.copy()
    for key, value in env:
        process_env[key] = value
    return process_env


def execute(cmd, env=[]):
    print('######', cmd, '######')
    popen = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, universal_newlines=True, env=get_env(env))
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


def execute_sync(cmd, env=[]):
    print('######', cmd, '######')
    return subprocess.Popen(shlex.split(cmd), env=get_env(env)).communicate()


def read_file(path):
    with open(path) as file_:
        return file_.read()


def write_file(path, text):
    f = open(path, 'w')
    f.write(text)
    f.close()