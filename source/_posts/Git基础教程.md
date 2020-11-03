---
title: Git基础教程
date: 2020-11-03 14:24:25
urlname: git
tags: 
    - Git
    - 版本控制
---

### 初始化配置
```
git config --global user.name "markLee"
git config --global user.email "946768930@qq.com"
```

### 初始化仓库
```
git init
```

### 基本操作
```
// 添加文件到暂存区，可以多次添加多种文件
git add .
```
![](git/提交.jpg)


```
// 提交文件到分支
git commit -m "版本更新"

```
![](git/添加.jpg)

```

// 查看当前仓库状态
git status

// 查看精简日志
git log --pretty=oneline

// 查看曾经输入的所有命令
git reflog

// 回退到指定commit
git reset --hard 887ef6b

// 回退到上一次commit
git reset --hard HEAD^

// 查看工作区和版本库内容区别
git diff HEAD -- readme.txt

// 撤销修改
1.git add之后撤销，回退到add后状态
2.git add之前撤销，和版本库状态一样
git checkout -- readme.txt

// 删除文件
git rm read.txt

// 生成公钥
ssh-keygen -t rsa -C "youremail@example.com"

// 关联远程仓库
git remote add origin git@github.com:michaelliao/learngit.git

// 删除远程仓库关联
git remote rm origin

// 推送代码
// -u 表达本地分支和远程分支相关联
git push -u origin master

// Linux与Windows换行符
git config --global core.autocrlf false

// 创建分支并切换
git checkout -b dev
git switch -c dev

// 创建本地及远程分支
git checkout -b dev origin/dev

// 列出所有分支
git branch

// 删除指定分支
git branch -d dev
git branch -D dev 强行删除，丢失未提交数据

// 把dev分支合并到当前分支
git merge dev

// 查看分支合并图
git log --graph

// 合并分支关闭fast forward模式
git merge --no-ff -m "merged bug fix 101" issue-101

// 当前分支已修改文件缓存一下
git stash

git stash list 查看当前缓存
git stash apply 恢复缓存
git stash drop 删除缓存
git stash pop 恢复并删除

git stash apply stash@{0} 恢复指定缓存

// 迁移指定commit
git cherry-pick 4c805e2

// 查看远程分支
git remote
git remote -v 详细信息

// 推送分支
git push origin master

// 本地分支关联远程分支
git branch --set-upstream-to=origin/dev dev

// 对指定提交打标签
git tag v0.9 f52c633

// 推送指定标签到远程仓库
git push origin v1.0

// 推送所有标签到远程仓库
git push origin --tags

// 删除指定标签
git tag -d v1.0

// 删除远程指定标签
git push origin:/refs/tags/v1.0

// 配置git命令别名
git config --global alias.st status

git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

```

@timeline{

##### 2016

@item{
###### 11月6日

为 Card theme 添加 page layout。
加快绿化空间好看
 
}

@item{
###### 10月31日

本地化多说。

}

@item{
###### 10月24日

为 Indigo 主题创建 Card 分支。

}

##### 2015

@item{
###### 2月24日

发布 Indigo 主题到 hexo.io。

}

@item{
###### 1月22日

创建 Indigo 主题。

}

}