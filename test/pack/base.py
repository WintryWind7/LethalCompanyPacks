import time
import sys
import ctypes
import os
import shutil


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
        print('路径不存在')
        return 0


def show_tools_version():
    """输出加载工具模板"""
    info()


def info(string, a=''):
    """作为基础的输出模板"""
    if a == '^':
        print('{:^55}'.format(string))
    elif a == '|^|':
        print('|{:^55}|'.format(string))
    elif a == '-':
        print('{:-55}'.format(string))
    elif a == '=':
        print('{:=55}'.format(string))
    elif a == '' or a == '<':
        print(string)
