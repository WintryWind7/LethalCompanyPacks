import time
import sys
import ctypes
import os
import shutil


class VerPack(object):
    ver_list = []
    def __init__(self, code, name):
        self.code = code.lower()
        self.name = name
        self.exclusions = []
        VerPack.ver_list.append(self)


def get_ver_pack(code):
    for ver in VerPack.ver_list:
        if ver.code == code:
            return ver
    return 0


def pause_exit():
    """暂停并退出程序"""
    time.sleep(3)
    sys.exit()


def check_admin():
    """检查是否为管理员运行"""
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if not is_admin():
        print("此程序需要管理员权限运行。")
        pause_exit()


def check_dir():
    """检查当前文件是否在游戏根目录下"""
    if os.path.exists('Lethal Company.exe'):
        return 0
    else:
        print('请将此文件放在游戏根目录下！')
        pause_exit()


def check_env():
    """检查运行环境"""
    check_admin()
    check_dir()


def delete(path):
    """删除文件"""
    if os.path.exists(path):
        if os.path.isfile(path):    # 如果是文件，则直接删除
            os.remove(path)
        elif os.path.isdir(path):   # 如果是目录，则删除该目录及其所有内容
            shutil.rmtree(path)
        return 1
    else:
        return 0


def info(string='', a=''):
    """作为基础的输出模板"""
    if a == '^':
        print('{:^55}'.format(string))
    elif a == '|^|':
        print('| {:^51} |'.format(string))
    elif a == '|<|':
        print('| {:<51} |'.format(string))
    elif a == '-':
        print('{:-55}'.format(string))
    elif a == '=':
        print('{:=^55}'.format(string))
    elif a == '' or a == '<':
        print(string)


def info_two(string1, string2, a=''):
    """按照表格格式输出信息"""
    print('{:^18}{:^36}'.format(string1, string2))






