# -*- coding:utf-8 -*-
import re

rerull = '://+.+?/'
rerull1 = '^http'
rerull12 = '(.*?/){3}'
linkru = '^[^http://|^https://](.*?\.){2}.[^\.|^/]*$'
lintw = []
# lcbt = ''
rl = '^(.*?\.){2}.[^\.|^/]*'
https = '^https'
http = '^http'

'''

intest = input()
back = re.search(rerull, intest)
innn = ''

if back == None:
    print(back)
else:
    innn = back.group()
    innn = innn.replace('://', '')
    innn = innn.replace('/', '')
    print(innn)
    '''


def relink(link,):
    idf = 0
    lintw = []
    ids12 = 111
    # global lcbt
    link11 = link
    a = re.search(linkru, link11)
    if a is not None:
        return link11
    b = re.search(rl, link11)
    if b is None:
        return '链接格式无法识别id000909091123'
    back = re.search(rerull1, link11)
    if back is None:
        # print('未检测到http已自动处理处理如下')
        link11 = 'http://' + link11
        # print(link11)
    back = re.search(rerull12, link11)
    if back is None:
       # print('未检测到结尾/已自动处理处理如下')
        link11 = link11 + '/'
        # print(link11)
        ids12 = 10

   #back1 = re.search(https, link11)
    #if back1 ==None:

     #   if not None:
      #      return link11
      #  else:
       #    return '链接格式无法识别id000909091123'



    back = re.search(rerull, link11)
    if back == None:
        # print('a')
       # print(lintw)
        return '链接格式无法识别id000909091123'
    else:
        #print('aaaa')
        innn = back.group()
        innn = innn.strip('://')
        innn = innn.strip('/')

       # print(lintw)
        return innn




def clear_html_re(src_html):
    '''
    正则清除HTML标签
    :param src_html:原文本
    :return: 清除后的文本
    '''
    content = re.sub(r"</?(.+?)>", "", src_html) # 去除标签
    # content = re.sub(r"&nbsp;", "", content)
    #dst_html = re.sub(r"\s+", "", content)  # 去除空白字符
    return content
