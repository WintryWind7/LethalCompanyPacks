# Lethal Company 致命公司简体中文汉化

该汉化补丁已基本实现v49版本的汉化,支持终端中文和拼音简写指令。

实现了对终端的汉化，和对一些常用模组的汉化，修复了一些因为汉化导致出现显示乱码的bug

所有相关汉化表和指令表基本都存放在config\translations里面的cfg，可以自行修改和添加，支持热重载

可以通过修改GameTranslator.cfg里的设置来细调汉化

CMD-PY-Translate为拼音指令

CMD-ZH-Translate为中文指令

GuiText-Translate为对一些窗口的汉化

HUD-Translate则对聊天栏和Tip的一些汉化

Item-Translate为对物品的汉化

Terminal-Translate为终端汉化

Normal-Translate为强匹配汉化

SpecialText-Translate为弱匹配汉化

arialuni为字体文件

# 使用说明

可以 R2ModMan 管理器安装和使用。

1. R2Modman 中下载并启用这个MOD。

也可以下载压缩包，然后解压到Lethal Company根目录里面

## 重要说明

该汉化目前已脱离XUnity.AutoTranslator,而且有概率与其他汉化冲突，如果想要使用该汉化包

需要删除其他汉化，如果BepInEx\plugin文件夹里面有XUnity.AutoTranslator和XUnity.ResourceRedirector则建议也将其删除

目前该汉化还属于测试阶段，可能还存在一些bug或者未汉化到的地方
