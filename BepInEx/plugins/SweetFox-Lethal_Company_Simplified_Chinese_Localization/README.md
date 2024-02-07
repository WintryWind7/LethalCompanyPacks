# Lethal Company 致命公司简体中文汉化

该汉化补丁已基本实现v49版本的汉化,支持终端中文和拼音简写指令,支持汉化其他mod.

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

由于R2Modman目前只有英文的版本，所以我自制了一个汉化包，翻译了大部分常用的功能。

下载地址：https://pan.baidu.com/s/1EB5InhINjEtGF6jE4xvrDA?pwd=eep1 

2. 也可以下载压缩包，然后解压到Lethal Company根目录里面

一些小更小补的更新和一些可替换字体会上传到百度云盘：https://pan.baidu.com/s/1TAaPCpTJ3uj3rfiQ8kt4aA?pwd=64n8

如果想更换字体，可以将GameTranslator.cfg里面的OverrideFontTextMeshPro = arialuni.cfg改为OverrideFontTextMeshPro = 你要想的字体，

粗字体就是 "Barialuni.cfg",细字体是 "Tarialuni.cfg"

目前版本的字体已兼容游戏，可以让游戏的TIP正常显示了，所以可以将Fix Tip Errors修改为false

# 重要说明

该汉化目前已脱离XUnity.AutoTranslator,而且有概率与其他汉化冲突，如果想要使用该汉化包

需要删除其他汉化，如果BepInEx\plugin文件夹里面有XUnity.AutoTranslator和XUnity.ResourceRedirector则建议也将其删除

目前该汉化还属于测试阶段，可能还存在一些bug或者未汉化到的地方

# BUG和反馈

作者的b站空间:https://space.bilibili.com/403741521

遇到问题和BUG可以来找我反馈(最近比较忙，可能不怎么更新和回复)

# 更新日志

## 1.8.33
+ 增加部分汉化，修复一些小bug
## 1.8.32
+ 修复 某些提示 不显示的BUG
## 1.8.31
+ 分离AHook,更改部分物品替换逻辑，修改提示修复代码
## 1.8.3
+ 重新提交mod
## 1.8.2
+ 尝试兼容 物品扩展槽模组 
## 1.8.1
+ 优化物品翻译，小调部分翻译逻辑
