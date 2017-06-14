# !/usr/bin/python
# coding:utf-8

# CSRF_ENABLED配置启用了跨站请求攻击保护
CSRF_ENABLED = True
# SECRET_KEY设置当CSRF启用时有效，这将生成一个加密的token供表单验证使用
SECRET_KEY = 'you-will-never-guess'
