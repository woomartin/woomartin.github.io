---
title: c语言入门
date: 2021-01-21 14:53:13
urlname: c
tags:
    - C语言
---

#### 宏定义

```c
#define time 2021
#define M(x, y) time*(x>y?x:y)
```

#### 指针

```c
int a = 100;
int *b = &a; // 内存地址赋值
printf("值1：%d, %d\n", a, *b);

*b = 200; // 真正赋值

printf("值2：%d, %d\n", a, *b);
printf("内存地址：%#x, %#x\n", a, *b);

b++;// 主动修改内存地址
printf("值3：%d, %d\n", a, *b);
printf("内存地址：%#x, %#x\n", a, *b);

int arr[] = {66, 15, 100, 888, 252};
printf("%d\n", sizeof(arr));
printf("%d\n", sizeof(int));

int len = sizeof(arr) / sizeof(int);
printf("数组长度：%d\n", len);

printf("值：%d\n", *(arr + 1));// 等价
printf("值：%d\n", arr[1]);// 等价

int *p = arr;
printf("指针：%d\n", *(p + 1));// 15 取数组第一个数字
printf("指针：%d\n", *p + 1);// 67 取数组第0个数字+1
printf("指针：%d\n", *p++);// 66
printf("指针：%d\n", *p);// 15
printf("指针：%d\n", *++p);// 100
printf("指针：%d\n", ++*p);// 101
printf("指针：%d\n", *p);// 101
```