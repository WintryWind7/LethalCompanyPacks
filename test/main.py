from pack.base import pause_exit, check_env
from pack.version import tool_info
import pack.moudle as moudle

# 检查环境(管理员运行，目录，)
check_env()

# 工具信息载入
tool_info()

# 查询远程版本
moudle.show_version()

# 获取input
code, command = moudle.get_input()
moudle.if_uninstall(code)
moudle.show_info(command)   # 读取简介
moudle.download(command)    # 下载获取temp.zip
moudle.unzip(code)          # 选择不解压的
moudle.rm_temp()

print('程序正常退出')
pause_exit()

