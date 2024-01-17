# 实现：检测是否有原版本->删除->下载zip->解压缩->根据需求移除
import os.path
import time
import zipfile
import requests
import sys
import shutil
from tqdm import tqdm
import ctypes

def pause_exit():
    time.sleep(3)
    # sys.exit()

def check_admin():

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if not is_admin():
        print("此程序需要管理员权限运行。")
        pause_exit()

def check_dir():

    if os.path.exists('Lethal Company.exe'):
        return 0
    else:
        print('请将此文件放在游戏根目录下！')
        pause_exit()


check_admin()
check_dir()

print('{:-^50}'.format(''))
print('{:^50}'.format('Lethal Company Mods 加载工具'))
print('{:^50}'.format('version 1.2.1'))
print('{:^50}'.format('By WintryWind'))
print('{:-^50}'.format(''))


def show_version():
    url = 'https://raw.githubusercontent.com/WintryWind7/LethalCompanyPacks/main/BepInEx/config/Wintrymods_version.txt'
    if os.path.exists('./BepInEx/config/Wintrymods_version.txt'):
        with open('./BepInEx/config/Wintrymods_version.txt', 'r') as fr:
            for line in fr:
                ver = line
    else:
        ver = '未知'

    try:
        print(f'本地版本: {ver}')
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"远程整合包版本: {response.text}")
            print('')
            return 0
    except:
        pass
    print('无法读取远程版本')
    print('')

show_version()

def show_info(command):
    if command == 'i':
        url = 'https://raw.yzuu.cf/WintryWind7/LethalCompanyPacks/main/README.md'
    else:
        url = "https://raw.githubusercontent.com/WintryWind7/LethalCompanyPacks/main/README.md"
    try:
        print(f'尝试读取简介文件 如果卡住了请重新打开输入代码1000-i')
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(response.text)
            return 0
    except:
        pass
    print('无法读取简介文件')


def delete(path):
    if os.path.isfile(path):
        # 如果是文件，则直接删除
        os.remove(path)
    elif os.path.isdir(path):
        # 如果是目录，则删除该目录及其所有内容
        shutil.rmtree(path)


def download_file(url, local_filename):
    """使用requests下载BepInEX"""
    delete('temp.zip')
    response = requests.head(url, timeout=10)
    total_size = int(response.headers.get('content-iength', 0))

    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        # 初始化tqdm进度条
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=local_filename, ascii=True) as bar:
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1048576):
                    f.write(chunk)
                    bar.update(len(chunk))
    return local_filename


def check_control():
    # Done
    """读取文件并检查是否有controls绑定"""
    if os.path.exists('./BepInEx/config/controls'):
        if os.path.exists('./temp'):
            shutil.rmtree('./temp')
        os.makedirs('./temp')
        shutil.move('./BepInEx/config/controls', './temp/controls')


def rm_Bep():
    rm_list = ['BepInEx', '_state', 'doorstop_config.ini', 'arialuni_sdf_u2019', 'Sinter-Normal', 'winhttp.dll',
               'mods.yml', 'LICENSE', '.gitignore']

    for file in rm_list:
        delete(file)


def input_number():
    global _command
    quit_list = ['quit', 'exit', ]
    package_list = ['test', '1000', '4009', '9000', '1900']
    rmc_list = ['uninstall']
    """
    输入需求密码

    输入: str形式数字或字母。
    一般的返回: 0测试，1...,quit,exit
    """
    print('\t需求代码\t\t包名')
    print('\t1000\t完整整合包')
    print('\t1900\t不加载汉化(减少卡顿)')
    print('\t4009\t不加载自定义音效')
    print('')
    print('\tuninstall\t卸载mod')
    print('\tquit\t关闭程序')
    print('特殊：')
    print('-d 本地安装，需改名temp.zip')
    print('-i 使用国内镜像安装')
    print('')
    _count = 0
    while _count <5:
        __pwd = input('请输入需求代码>>').replace(' ', '')
        if len(__pwd) <6:
            __pwd = __pwd + '111111'
        _command = __pwd[5:6]
        _pwd = __pwd[:4]

        if _command == 'd':
            rm_Bep()
            unzip(excluede_list(_pwd))
            move_controls()
            rm_temp()
            pause_exit()


        if _pwd in quit_list:
            print('检测到退出指令，已退出!')
            pause_exit()

        elif _pwd in package_list:
            show_info(_command)
            print('正在下载整合包...')
            return _pwd

        elif _pwd in rmc_list:
            print('仅卸载整合包！')
            rm_Bep()
            rm_temp()
            print('done！')
            pause_exit()
        _count += 1
    print('错误次数过多，程序退出')
    pause_exit()


def dirname(file, n=1):
    try:
        if n != 0:
            n -= 1
            file = os.path.dirname(file)
    except:
        pass
    return file



def unzip(exclusions):
    zip_path = './temp.zip'
    extract_to = './'

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_files = zip_ref.namelist()
        subfolder = zip_files[0].split('/')[0] + '/'

        for file in zip_files:
            if not any(dirname(file, 1).lower().endswith('/' + exclusion.lower())     # 文件夹排除
                       or dirname(file, 2).lower().endswith('/' + exclusion.lower())
                       or dirname(file, 3).lower().endswith('/' + exclusion.lower())
                       or dirname(file, 4).lower().endswith('/' + exclusion.lower())
                       or file.lower().endswith(exclusion.lower()) for exclusion in exclusions):    # 文件名排除
                if file.startswith(subfolder):
                    # 调整文件路径，移除子目录部分
                    adjusted_path = file[len(subfolder):]
                    if adjusted_path and not adjusted_path.endswith('/'):  # 确保不是子目录本身
                        adjusted_full_path = os.path.join(extract_to, adjusted_path)
                        os.makedirs(os.path.dirname(adjusted_full_path), exist_ok=True)
                        with zip_ref.open(file) as source_file, open(adjusted_full_path, 'wb') as target_file:
                            target_file.write(source_file.read())


def excluede_list(pwd):

    dt = {'1000': [],
          'test': [],
          '1900': ['LocalizationCore_BepInEx5汉化模组前置.dll', '精校汉化包V1-2', 'LocalizationCore', 'Translation',
                   'HK417KEN-Lethal_Company_Simplified_Chinese_Localization'],
          '4009': ['CustomSounds'],
          '9000': ['HDLethalCompany', 'HDLethalCompany画质优化.dll'],
          }

    ls = dt.get(pwd)
    lsa = ['README.md', 'LICENSE', 'test', '.gitignore', '.idea']
    for file in lsa:
        ls.append(file)
    return ls


def move_controls():
    if os.path.exists('temp'):
        shutil.move('./temp/controls', './BepInEx/config/controls')
        shutil.rmtree('temp')


def rm_temp():
    delete('temp')
    delete('temp.zip')

def download(command):
    if command == 'i':
        url = 'https://hub.yzuu.cf/WintryWind7/LethalCompanyPacks/archive/refs/heads/main.zip'
    else:
        url = 'https://github.com/WintryWind7/LethalCompanyPacks/archive/refs/heads/main.zip'

    for i in range(5):
        try:
            download_file(url, 'temp.zip')
            if os.path.exists('temp.zip'):
                break
        except:
            print(f'重试 第{i+1}次')
    if not os.path.exists('temp.zip'):
        print("[ERROR] 网络连接异常")
        pause_exit()

def main():
    check_control()     # Done
    pwd = input_number()
    download(_command)
    print('')
    print('正在解压并整理目录，请勿关闭...')
    rm_Bep()
    unzip(excluede_list(pwd))
    print('正在同步...')
    move_controls()
    rm_temp()
    print('删除多余文件...')


if __name__ == "__main__":
    main()
    print('Done!')
    pause_exit()