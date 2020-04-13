# SetRandBingWP

一个给桌面设置一张随机Bing壁纸的小程序

可以将程序添加到右键菜单更加方便使用：
打开注册表，找到目录：计算机\HKEY_CLASSES_ROOT\Directory\Background\shell，新建项WallPaper，其默认值填写”随机更换壁纸”，再创建二级子节点command，其默认值填写可执行文件路径。

使用了[必应壁纸接口](https://github.com/xCss/bing)
