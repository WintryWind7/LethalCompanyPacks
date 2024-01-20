import requests
from .base import delete
from tqdm import tqdm
import os
import zipfile


def download_file(url):
    """使用requests下载BepInEX"""
    delete('temp.zip')
    response = requests.head(url, timeout=10)
    total_size = int(response.headers.get('content-iength', 0))

    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        with tqdm(total=total_size, unit='B', unit_scale=True, desc='temp.zip', ascii=True) as bar:
            with open('temp.zip', 'wb') as f:
                for chunk in r.iter_content(chunk_size=8388608):
                    f.write(chunk)
                    bar.update(len(chunk))


def dirname(file, n=1):
    """获取目录名，方便排除文件"""
    if n != 0:
        temp = os.path.dirname(file)
        return dirname(temp, n-1)
    return file


def unzip(exclusions):
    """解压文件，排除传入列表中的文件"""
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


def show_version():
    """检查本地版本和远程版本"""
    url = 'https://raw.githubusercontent.com/WintryWind7/LethalCompanyPacks/main/BepInEx/config/Wintrymods_version.txt'
    if os.path.exists('./BepInEx/config/Wintrymods_version.txt'):
        with open('./BepInEx/config/Wintrymods_version.txt', 'r') as fr:
            for line in fr:
                ver = line
    else:
        ver = '未知'
    print(f'本地版本: {ver}')
    for _ in range(2):
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"远程整合包版本: {response.text}")
                print('')
                return 0
        except:
            pass
        url = 'https://raw.yzuu.cf/WintryWind7/LethalCompanyPacks/main/BepInEx/config/Wintrymods_version.txt'
    print('无法读取远程版本')
    print('')


def show_info(command):
    """查询远程README.md文件"""
    if command == 'i':
        url = 'https://raw.yzuu.cf/WintryWind7/LethalCompanyPacks/main/README.md'
    else:
        url = "https://raw.githubusercontent.com/WintryWind7/LethalCompanyPacks/main/README.md"
    try:
        print(f'尝试读取简介文件。')
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(response.text)
            return 0
    except:
        pass
    print('无法读取简介文。')


def get_input():
    """获取需求代码"""
