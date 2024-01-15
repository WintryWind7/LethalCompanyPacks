# 实现：检测是否有原版本->删除->下载zip->解压缩->根据需求移除
import os.path
import time
import zipfile
import requests
import sys
import shutil


def exit(t=3):
    time.sleep(t)
    sys.exit()

def download_file(url, local_filename):
    """使用requests下载BepInEX"""
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def check_control():
    """读取文件并检查是否有controls绑定"""
    if os.path.exists('./BepInEx/config/controls'):
        if os.path.exists('./temp'):
            shutil.rmtree('./temp')
        os.makedirs('./temp')
        shutil.move('./BepInEx/config/controls', './temp/controls')


def rm_Bep():
    rm_list = ['BepInEx', '_state', 'doorstop_config', 'arialuni_sdf_u2019', 'Sinter-Normal', 'winhttp.dll', 'mods.yml']

    for file in rm_list:
        if os.path.exists(file):
            shutil.rmtree(file)



def input_number():
    quit_list = ['quit', 'exit', ]
    package_list = ['test', '1000']
    rmc_list = ['uninstall']
    """
    输入需求密码

    输入: str形式数字或字母。
    一般的返回: 0测试，1...,quit,exit
    """
    print('\t需求代码\t\t包名')
    print('\t1000\t完整整合包')
    _count = 0
    while _count <5:
        _pwd = input('  请输入需求代码>>').replace(' ', '')

        if _pwd in quit_list:
            print('检测到退出指令，已退出!')
            exit()

        elif _pwd in package_list:
            print('正在下载整合包...')
            return _pwd

        elif _pwd in rmc_list:
            print('仅卸载整合包！')
            rm_Bep()
            print('done！')
            exit()
        _count += 1
    print('错误次数过多，程序退出')
    exit()


import zipfile
import os

import zipfile
import os


def unzip(exclusions):
    """解压"""
    print('开始解压!')
    zip_path = './temp.zip'
    extract_to = './'

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_files = zip_ref.namelist()

        # 确定 ZIP 文件中的第一个目录名称
        first_dir = zip_files[0].split('/')[0] + '/'

        for file in zip_files:
            if not any(file.startswith(exclusion) for exclusion in exclusions):
                # 检查是否为文件（非目录）
                if not file.endswith('/'):
                    # 调整文件路径，去掉最顶层目录部分
                    adjusted_file_path = os.path.join(extract_to, file[len(first_dir):])
                    # 创建必要的目录结构
                    os.makedirs(os.path.dirname(adjusted_file_path), exist_ok=True)
                    # 从 ZIP 文件中提取文件
                    with zip_ref.open(file) as source_file:
                        with open(adjusted_file_path, 'wb') as target_file:
                            target_file.write(source_file.read())
        print('done!')


def excluede_list(pwd):

    dt = {'1000': [''],
          'test': [''],
          }


    return dt.get(pwd)


def main():
    check_control()
    pwd = input_number()
    download_file('https://github.com/WintryWind7/LethalCompanyPacks/archive/refs/heads/main.zip', 'temp.zip')
    rm_Bep()
    unzip(excluede_list(pwd))



if __name__ == "__main__":
    main()