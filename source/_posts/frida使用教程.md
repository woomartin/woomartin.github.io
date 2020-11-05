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

```python
import frida
import sys

# hook代码，采用javascript编写
jscode = """
//javascript代码，重点
Java.perform(function () {
    var apkParseCompat = Java.use('com.hookandroid.apk.library.ApkParseCompat');

    // 打印日志工具
    console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));

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


```

进入指定app内存
objection -g com.android.settings explore

内存中so
memory list modules

内存中so函数
memory list exports libssl.so

内存中activity
android hooking list activities

内存中所有类
android hooking list classes

观察内存类调用
android hooking watch class android.bluetooth.BluetoothDevice

```