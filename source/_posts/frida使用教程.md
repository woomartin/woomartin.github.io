---
title: frida使用教程
date: 2020-11-04 18:54:54
urlname: frida_use
tags:
    - Android
    - 逆向
    - frida
---

### hook代码

```java

import frida
import sys

# hook代码，采用javascript编写
jscode = """
//javascript代码，重点
Java.perform(function () {
    var apkParseCompat = Java.use('com.hookandroid.apk.library.ApkParseCompat');

    apkParseCompat.isExitPackage.implementation = function(packageName){
        send("hook start isExitPackage...");
        send("参数1：" + packageName);
        return true;
    }

});
"""
 
# 自定义回调函数
def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

# 重点的4行代码
process = frida.get_remote_device().attach('com.hookandroid.apk.sample')
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
sys.stdin.read()

```