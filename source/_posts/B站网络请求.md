---
title: B站网络请求
date: 2021-01-25 10:30:24
urlname: bilibili
tags: 
    - 抓包
---

[BiliApi.py](bilibili/BiliApi.py)

#### 获取视频列表

```
https://api.bilibili.com/x/player/pagelist?bvid=BV1tp4y1i7rL&jsonp=jsonp
```

#### 获取视频Url

```
https://api.bilibili.com/x/player/playurl?cid=217171581&avid=&bvid=BV1tp4y1i7rL&qn=80&fourk=0&otype=json
```

#### 下载视频

```
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: https://www.bilibili.com/video/BV1tp4y1i7rL
Accept-Encoding: gzip, deflate
```