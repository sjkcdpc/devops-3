#!/usr/bin/env python
""" 初始化创建 admin 账号"""
import os
import sys


def main():
    # 使用django配置文件进行设置
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops.settings')
    
    # 让django初始化
    import django
    django.setup()
    
    from django.core.cache import cache
    cache.set('test_123', ['x', 'y'], 600)
    print(cache.get('test_123'))
    print(type(cache.get('test_123')))
    
    cache.delete('leffss')
    
    
if __name__ == '__main__':
    # main()
    # x = b'\xe8\xb5'
    # print(x.decode('utf-8'))
    # y = '知'
    # print(y.encode('utf-8'))
    # print(y.encode('gbk'))
    #
    # a = 'xxxx'
    # print(a[0:2])
    # print(a[100:])

    msg = format('PLAY_{}'.format('xx'), '*<50')
    print(msg)

    msg = format('xx_{}'.format('yyy'), '*<50')
    print(msg)

