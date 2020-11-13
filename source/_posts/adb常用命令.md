---
title: adb常用命令
date: 2020-11-03 18:24:39
urlname: adb
tags:
    - adb
---

#### 卸载系统应用

```
adb shell pm uninstall [-k] [--user USER_ID] 包名
参数说明：
-k 卸载应用且保留数据与缓存，如果不加 -k 则全部删除。
--user 指定用户 id，Android 系统支持多个用户，默认用户只有一个，id=0。
可以用这个命令，user 和 debug 版本都可以用，所有应用都能卸载掉。

比如这里卸载 360 浏览器：
adb shell pm uninstall -k --user 0 com.qihoo.browser

恢复安装
adb shell pm install-existing --user 0 com.qihoo.browser

```

#### debug模式启动apk
```

debug启动
adb shell am start -D -n com.ali.tg.testapp/.MainActivity

等待debug
adb shell am set-debug-app -w com.example.jishuxiaoheiwu.appdebugsample

设置持久debug
adb shell am set-debug-app -w --persistent  com.example.jishuxiaoheiwu.appdebugsample

清除持久debug
adb shell am clear-debug-app


```

#### 查看栈顶Activity
```
adb shell dumpsys activity top | findstr ACTIVITY

adb shell dumpsys activity top | findstr pid
```