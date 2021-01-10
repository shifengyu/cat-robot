# cat-robot

<p align="center">
  <a href="https://doc.sfy18178.com.cn" target="_blank">
    <img width="128" src="https://www.sfy18178.com.cn/wp-content/uploads/2020/08/21582690901_.pic_.jpg" alt="cat-robot">
  </a>
</p>

<p align="center">
  cat-robot 是一个小巧而灵活的语音智能助手
</p>

## 目录

* [特性](#特性)
* [环境要求](#环境要求)
* [安装](#安装)
* [运行](#运行)
* [配置](#配置)
* [插件](#插件)
* [FAQ](#faq)
* [免责声明](#免责声明)

## 特性
* 模块化。功能插件、语音识别、语音合成、对话机器人都做到了高度模块化，第三方插件单独维护，方便继承和开发自己的插件。
* 中文英文支持。集成百度中英文语音识别和语音合成技术，且可以继续扩展。
* 对话机器人支持。支持接入Emotibot 等在线对话机器人。
* 灵活可配置。支持定制机器人名字，支持选择语音识别和合成的插件。
* 后台配套支持。提供配套后台，可实现远程操控、修改配置和日志查看等功能。

cat-robot 的工作模式：
<p align="center">
  <img src="https://download.sfy18178.com.cn/cat-robot/img/workflow.png" alt=" cat-robot 的工作模式">
</p>
cat-robot 被唤醒后，先通过STT转换成文字，然后中英文判断来确认是什么语言，如果是英语那么就通过翻译把它转换成中文，然后在通过Emotibot 等在线对话工具进行对话，然后在有TTS输出，并播放。



## 环境要求 ##

### Python 版本 ###

cat-robot 只支持 Python 3.7+，不支持 Python 2.x 。

### 设备要求 ###

cat-robot 支持运行在以下的设备和系统中：

* 64bit Mac OS X
* 64bit Ubuntu（12.04 and 14.04）
* 树莓派的所有型号（Raspbian 系统）

## 安装 ##

见 [cat-robot 安装教程](https://doc.sfy18178.com.cn/#/cat-robot?id=安装)。


## 运行 ##
在终端输入
```bash
python3 cat.py
```
就可以运行了
cat-robot 在运行期间还会启动一个后台管理端，提供了远程对话、查看修改配置、查看 log 、安装插件等能力。

- 默认地址：http://localhost:8000
- 默认账户名：admin
- 默认密码：123456

建议正式使用时修改用户名和密码，以免泄漏隐私。

## 配置 ##

参考[配置文件的内容和注解](https://doc.sfy18178.com.cn/#/cat-robot?id=配置文件)进行配置即可。

## 插件 ##

* [官方插件列表](https://doc.sfy18178.com.cn/#/cat-robot)

## FAQ

- 我能否更换成其他唤醒词，而不是叫“小白”？

  - 能。到 [snowboy官网](http://snowboy.kitt.ai/) 训练一个自己的唤醒词，然后将生成的 pmdl 文件放到 cat-robot的static目录下，并修改static目录下setting.json文件里的pmdl

## 免责声明

* cat-robot 只用作个人使用，如因使用 cat-robot 导致任何损失，本人概不负责。
