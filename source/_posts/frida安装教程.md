---
title: frida安装教程
date: 2020-11-04 15:36:27
urlname: frida_install
tags:
    - Android
    - 逆向
    - frida
---

需要安装python3，及已获取root权限手机或模拟器。

<!-- more -->

### 安装python3

```
https://www.python.org/downloads/release/python-360/

配置环境变量
```

### 安装frida

#### 更新pip
```
确认pip
python -m ensurepip

更新pip
python -m pip install --upgrade pip

安装wheel
pip install wheel

```

#### 安装
```
推荐FRIDA稳定版
pip install frida==12.8.0
pip install frida-tools==5.3.0
pip install objection==1.8.4
以上安装需要科学上网
```

### 运行frida-server

#### 下载
```
https://github.com/frida/frida/releases

含图形化页面服务端
https://github.com/wrlu/FridaHooker

```

#### 推送到模拟器

```
adb push frida-server-12.8.0-android-x86 /data/local/frida-server
su
chmod 777 frida-server
./frida-server

```

```
frida-ps -Ua
出现进程列表，表示连接成功
```