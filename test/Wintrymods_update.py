# 实现：检测是否有原版本->删除->下载zip->解压缩->根据需求移除
import os.path
import time
import zipfile
import requests
import sys
import shutil
from tqdm import tqdm

print('{:-^50}'.format(''))
print('{:^50}'.format('Lethal Company Mods 加载工具'))
print('{:^50}'.format('version 1.0.0'))
print('{:^50}'.format('By WintryWind'))
print('{:-^50}'.format(''))


def show_info():
    url = f"https://raw.githubusercontent.com/WintryWind7/LethalCompanyPacks/master/README.md"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print("无法获取文件内容")



def exit(t=3):
    time.sleep(t)
    sys.exit()


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
    response = requests.head(url)
    total_size = int(response.headers.get('content-length', 0))

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
    """读取文件并检查是否有controls绑定"""
    if os.path.exists('./BepInEx/config/controls'):
        if os.path.exists('./temp'):
            shutil.rmtree('./temp')
        os.makedirs('./temp')
        shutil.move('./BepInEx/config/controls', './temp/controls')


def rm_Bep():
    rm_list = ['BepInEx', '_state', 'doorstop_config.ini', 'arialuni_sdf_u2019', 'Sinter-Normal', 'winhttp.dll',
               'mods.yml', 'LICENSE']

    for file in rm_list:
        delete(file)


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
    print('\t9000\t不加载HD画质优化插件')
    print('\t4009\t不加载自定义音效(不包括音响)')

    print('\tuninstall\t卸载mod')
    print('\tquit\t关闭程序')
    _count = 0
    while _count <5:
        _pwd = input('请输入需求代码>>').replace(' ', '')

        if _pwd in quit_list:
            print('检测到退出指令，已退出!')
            exit()

        elif _pwd in package_list:
            show_info()
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


def unzip(exclusions):
    zip_path = './temp.zip'
    extract_to = './'

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_files = zip_ref.namelist()
        subfolder = zip_files[0].split('/')[0] + '/'

        for file in zip_files:
            if not any(os.path.dirname(file).lower().endswith('/' + exclusion.lower()) or file.lower().endswith(exclusion.lower()) for exclusion in exclusions):
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
          '4009': ['CustomSounds'],
          '9000': ['HDLethalCompany', 'HDLethalCompany画质优化.dll'],
          }

    ls = dt.get(pwd)
    lsa = ['README.md', 'LICENSE', 'test', '.gitignore', ]
    for file in lsa:
        ls.append(file)
    return ls


def move_controls():
    if os.path.exists('temp'):
        shutil.move('./temp/controls', './BepInEx/config/controls')
        shutil.rmtree('temp')

def main():
    check_control()
    pwd = input_number()
    for i in range(5):
        try:
            download_file('https://github.com/WintryWind7/LethalCompanyPacks/archive/refs/heads/master.zip', 'temp.zip')
            if os.path.exists('temp.zip'):
                break
        except:
            print(f'重试 {i+1}')
    if not os.path.exists('temp.zip'):
        print("[ERROR] 网络连接异常")
        exit()
    print('---')
    print('正在整理目录...')
    rm_Bep()
    unzip(excluede_list(pwd))
    move_controls()



if __name__ == "__main__":
    main()