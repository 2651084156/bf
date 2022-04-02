import time
import base64
from libss.get_html import get_requests_html2
from .useful_help import get_ua, get_try_number, get_timeout
from .code1 import code_get
import libss.css_main_get as css_get
import libss.xpath_main_get as xpath_get
import libss.bs4_main_get as bs4_1

class analyze:
    '''
    解析核心
    '''
    def __init__(self, link, get_rule: list, uuid):
        '''

        :param link: 链接
        :param get_rule: 获取规则
        :param uuid: 就是uuid不过用处迷惑
        '''
        self.link = link
        self.get_rule = get_rule
        self.num = {}
        self.r_state = 0
        self.rep_back = '' #接收返回值
        self.uuid = uuid
        self.ua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
        self.trn = 5
        self.timeo = 5

    def get_num(self, name):
        # print(name)
        a = self.num.get(name)
        return a

    def run(self):  # 启动函数


        for list1 in self.get_rule:

            if self.r_state == 1:
                break
            else:

                # print(type({'fsdfsdf': 'dsadsad'}))
                self.worket(list1)

    def worket(self, rule: dict):  # 工作函数
        rule1 = rule
        main = list(rule1.keys())[0]
        # print(main)
        if main == 'get_link_f':
            aa1 = get_ua()
            if aa1 is None:
                uas = self.ua
            else:
                uas = aa1
            ab = get_try_number()
            if ab is None:
                try_number = self.trn
            else:
                try_number = ab
            ab1 = get_timeout()
            if ab1 is None:
                timeout = self.timeo
            else:
                timeout = ab1
            html1 = get_requests_html2(link=self.link, headers=uas, timeout=timeout, try_number=try_number)
            # print(html1)
            if isinstance(html1, list):
                if html1[0] == 'time_out@@@@@@@':
                    self.r_state = 1

                    self.rep_back = ['time_out@@@@@@@','a']
                    return 'time_out@@@@@@@'
                if html1[0] == 'errrr':
                    self.r_state = 1
                    self.rep_back = ['errrr',html1[1]]
                    return 'errrr'
            else:
                self.num['main'] = html1
        #
        # elif main == 'test':
        #     time.sleep(1)
        #     print('ok')

        elif main == 'get_link_f_r':
            aa1 = get_ua()
            if aa1 is None:
                uas = self.ua
            else:
                uas = aa1
            ab = get_try_number()
            if ab is None:
                try_number = self.trn
            else:
                try_number = ab
            ab1 = get_timeout()
            if ab1 is None:
                timeout = self.timeo
            else:
                timeout = ab1
            html1 = get_requests_html2(link=self.link, headers=uas, timeout=timeout, try_number=try_number)
            if isinstance(html1, list):
                if html1[0] == 'time_out@@@@@@@':
                    self.r_state = 1

                    self.rep_back = ['time_out@@@@@@@', 'a']
                    return 'time_out@@@@@@@'
                if html1[0] == 'errrr':
                    self.r_state = 1
                    self.rep_back = ['errrr', html1[1]]
                    return 'errrr'
            else:


                html1.html.render()
                self.num['main'] = html1.html.html



        elif main == 'get_link':
            ma = rule1.get(main)
            link1 = self.get_num(ma[0])
            nu = self.get_num(ma[1]) #bug

            aa2 = get_ua()
            if aa2 is None:
                uas = self.ua
            else:
                uas = aa2
            ab = get_try_number()
            if ab is None:
                try_number = self.trn
            else:
                try_number = ab
            ab1 = get_timeout()
            if ab1 is None:
                timeout = self.timeo
            else:
                timeout = ab1
            html1 = get_requests_html2(link=link1, headers=uas, timeout=timeout, try_number=try_number)
            if isinstance(html1, list):
                if html1[0] == 'time_out@@@@@@@':
                    self.r_state = 1

                    self.rep_back = ['time_out@@@@@@@', 'a']
                    return 'time_out@@@@@@@'
                if html1[0] == 'errrr':
                    self.r_state = 1
                    self.rep_back = ['errrr', html1[1]]
                    return 'errrr'
            else:
                self.num[nu] = html1

        elif main == 'get_link_r':
            ma = rule1.get(main)
            link1 = self.get_num(ma[0])
            nu = self.get_num(ma[1])

            aa2 = get_ua()
            if aa2 is None:
                uas = self.ua
            else:
                uas = aa2
            ab = get_try_number()
            if ab is None:
                try_number = self.trn
            else:
                try_number = ab
            ab1 = get_timeout()
            if ab1 is None:
                timeout = self.timeo
            else:
                timeout = ab1
            html1 = get_requests_html2(link=link1, headers=uas, timeout=timeout, try_number=try_number)
            if isinstance(html1, list):
                if html1[0] == 'time_out@@@@@@@':
                    self.r_state = 1

                    self.rep_back = ['time_out@@@@@@@', 'a']
                    return 'time_out@@@@@@@'
                if html1[0] == 'errrr':
                    self.r_state = 1
                    self.rep_back = ['errrr', html1[1]]
                    return 'errrr'

            # print('aaaa')
            else:
                html1.html.render()
                self.num[nu]  = html1.html.html

        elif main == 'get_img_to_base64':
            ma = rule1.get(main)
            link1 = self.get_num(ma[0])
            nu = ma[1]  #大bug啊！<br /><br />

            aa2 = get_ua()
            if aa2 is None:
                uas = self.ua
            else:
                uas = aa2
            ab = get_try_number()
            if ab is None:
                try_number = self.trn
            else:
                try_number = ab
            ab1 = get_timeout()
            if ab1 is None:
                timeout = self.timeo
            else:
                timeout = ab1
            html1 = get_requests_html2(link=link1, headers=uas, timeout=timeout, try_number=try_number)
            if isinstance(html1, list):
                if html1[0] == 'time_out@@@@@@@':
                    self.r_state = 1

                    self.rep_back = ['time_out@@@@@@@', 'a']
                    return 'time_out@@@@@@@'
                if html1[0] == 'errrr':
                    self.r_state = 1
                    self.rep_back = ['errrr', html1[1]]
                    return 'errrr'
            else:
                aaa= base64.b64encode(html1.content)
                self.num[nu] = aaa

        elif main == 'code_get_m':
            a = self.get_num('main')
            b = code_get(a)
            self.num['main'] = b

        elif main == 'code_get':

            a1 = rule1.get(main)
            a1a = a1[0]
            bb = a1[1]
            a = self.get_num(a1a)
            b = code_get(a)
            self.num[bb] = b
        elif main == 'get_list_item':

            a1 = rule1.get(main)
            listt = a1[0]
            aint = a1[1]
            num = a1[2]
            self.num[num] = listt[aint]


        elif main == 'cycle':
            a1 = rule1.get(main)
            cy = 1
            while True:

                if self.r_state == 1:
                    break
                else:
                    if cy == 0:
                        break
                    for i in a1:
                        if self.r_state == 1:
                            break
                        else:
                            ab = self.worket(i)
                            if ab == 'break':
                                cy = 0

        elif main == 'cy_b':
            return 'break'

        elif main == 'copy_a_to_b':
            a1 = rule1.get(main)
            a = a1[0]
            b = a1[1]
            a2a = self.get_num(a)
            self.num[b] = a2a


        elif main == 'if_a,b':
            r = rule1.get(main)
            a = r[0]
            b = r[1]
            m = r[2]
            li = r[3]
            a1a = self.get_num(a)
            bb = self.get_num(b)
            if m == '==':
                if a1a == bb:
                    for i in li:
                        if self.r_state == 1:
                            break
                        else:
                            ab = self.worket(i)
            if m == '<=':
                if a1a <= bb:
                    for i in li:
                        if self.r_state == 1:
                            break
                        else:
                            ab = self.worket(i)

            if m == '<':
                if a1a < bb:
                    for i in li:
                        if self.r_state == 1:
                            break
                        else:
                            ab = self.worket(i)

            if m == '>=':
                if a1a >= bb:
                    for i in li:
                        if self.r_state == 1:
                            break
                        else:
                            ab = self.worket(i)

            if m == '>':
                if a1a > bb:
                    for i in li:
                        if self.r_state == 1:
                            break
                        else:
                            ab = self.worket(i)

            if m == '!=':
                if a1a != bb:
                    for i in li:
                        if self.r_state == 1:
                            break
                        else:
                            ab = self.worket(i)

        elif main == 'add_num':
            r = rule1.get(main)
            a = r[0]
            nnn = r[1]
            self.num[a] = nnn

        elif main == 'get_list_item':
            r = rule1.get(main)
            li = r[0]
            intf = r[1]
            nmnm = r[2]
            self.num[nmnm] = li[intf]

        # elif main =='for_list':
        #     r =rule1.get(main)
        #     li =r[0]
        #     s=r[1]
        #     for i in li:
        #         for

        elif main == 'add_none':

            r = rule1.get(main)
            self.num[r] = None

        elif main == 'return_num':
            r = rule1.get(main)
            self.rep_back = self.num.get(r)
            self.r_state = 1
            return 0

        elif main == 'make_list':
            r = rule1.get(main)
            listt = r[0]
            lisy = r[1]
            cccc = []
            for i in lisy:
                a = self.get_num(i)
                cccc.append(a)
            self.num[listt] = cccc

        elif main == 'str_add':
            r = rule1.get(main)
            a = str(self.get_num(r[0]))
            b = str(self.get_num(r[1]))
            c = ''.join([a,b])
            self.num[r[2]] = c

        elif main == 'for_list':
            r = rule1.get(main)
            l = self.get_num(r[0])

            num1 =r[1]
            c =r[2]
            for ii3 in l:
                if self.r_state == 1:
                    break
                else:
                    self.num[num1] = ii3
                    # print(l)
                    for inii in c:
                        if self.r_state == 1:
                            break
                        else:
                            ab = self.worket(inii)

        elif main=='str()':
            r = rule1.get(main)
            strr =self.get_num(r[0])
            b = r[1]
            a = str(strr)
            self.num[b] = a

        elif main == 'replace_str':
            r = rule1.get(main)
            strr = self.get_num(r[0])
            repacea1 = r[1]
            repacea2 = r[2]
            b = r[3]

            a =strr.replace(repacea1,repacea2)
            self.num[b] =a

        elif main == 'reversed_list': #倒序列表
            r = rule1.get(main)
            listt = self.get_num(r[0])

            b = r[1]

            a =list(reversed(listt))
            self.num[b] =a

        elif main == 'deduplication': #去重模块
            r = rule1.get(main)
            list1 = self.get_num(r [0]) # 链接
            list2=self.get_num(r [1]) #章名
            b=self.get_num(r [2])
            list1_r=list(reversed(list1))
            list2_r = list(reversed(list2))
            listtt1 =[]
            listtt2 = []
            for i in range(len(list1_r)):
                if list1_r[i] not in listtt1:
                    listtt1.append(list1_r[i])
                    listtt2.append(list2_r[i])
            listtt1 = reversed(listtt1)
            listtt2 = reversed(listtt2)
            self.num[b] = [listtt1,listtt2]

        elif main == 'add_list':
            r = rule1.get(main)
            listt = r[0]
            lisy = r[1]

            litttt =self.get_num(listt)
            if litttt == None:
                litttt = []

            a = self.get_num(lisy)
            litttt.append(a)
            self.num[listt] = litttt






        # #####################################上面核心下面实用############################# #


















        elif main == 'fix':
            r = rule1.get(main)
            html = self.get_num(r)
            a = xpath_get.xpath_get(html=html,ru='/*')
            # print(a)
            html2 =xpath_get.xpath_out_html(a[0])
            self.num[r] =html2
            # print(html2)

        elif main =='css_find':
            r = rule1.get(main)
            html = self.get_num(r[0])
            rule21 =r[1]
            back = r[2]

            c = css_get.css_find(html=html,rule=rule21)

            self.num[back]=c


        elif main == 'css_get_item':
            r = rule1.get(main)
            html = self.get_num(r[0])
            rule21 = r[1]
            back = r[2]
            c = css_get.css_get_item(html=html, rule=rule21)
            self.num[back] = c

        elif main == 'css_get_attr':
            r = rule1.get(main)
            html = self.get_num(r[0])
            rule21 = r[1]
            back = r[2]
            c = css_get.css_get_attr(html=html, attr=rule21)
            self.num[back] = c

        elif main =='css_get_text':
            r = rule1.get(main)
            html = self.get_num(r[0])

            back = r[2]
            c = css_get.css_get_text(html=html)
            self.num[back] = c

        elif main == 'css_get_html':
            r = rule1.get(main)
            html = self.get_num(r[0])

            back = r[2]
            c = css_get.css_get_html(html=html)
            self.num[back] = c

        elif main == 'xpath_get':
            r = rule1.get(main)
            h = r[0]
            ru = r[1]
            b= r[2]
            html = self.get_num(h)
            a = xpath_get.xpath_get(html=html, ru=ru)
            # print(a)
            html2 = a
            self.num[b] = html2

        elif main == 'xpath_out_html':
            r = rule1.get(main)
            h = r[0]

            b= r[1]
            node = self.get_num(h)
            a = xpath_get.xpath_out_html(xpathL=node)
            # print(a)
            html2 = a
            self.num[b] = html2


        elif main == 'xpath_out_test':
            r = rule1.get(main)
            h = r[0]

            b= r[1]
            html = self.get_num(h)
            a = xpath_get.xpath_out_test(html=html)
            # print(a)
            html2 = a
            self.num[b] = html2

        elif main == 'bs4_find':
            r = rule1.get(main)
            h = r[0]
            ru = r[1]
            b = r[2]
            html = self.get_num(h)
            a = bs4_1.bs4_find(html=html,ru=ru)
            html2 = a
            self.num[b] = html2

        elif main == 'bs4_find_all':
            r = rule1.get(main)
            h = r[0]
            ru = r[1]
            b = r[2]
            html = self.get_num(h)
            a = bs4_1.bs4_find_all(html=html,ru=ru)
            html2 = a
            self.num[b] = html2



        elif main == 'prettify': #美化html
            r = rule1.get(main)
            h = r[0]
            b = r[1]
            html = self.get_num(h)
            a = bs4_1.prettify(html=html)
            html2 = a
            self.num[b] = html2











#
# aa = analyze('http://127.0.0.1/test/1.html', [{'get_link_f': ''},{'code_get_m':''} ],
#              'dddd')
# aa.run()
# aaaa=aa.num
# print(aaaa.get('main'))
# print(aa.rep_back)
#
#
# aqqqa = analyze('http://127.0.0.1/test/1.html', [{'get_link_f': ''} ,{'add_num': ['rule', '#content']},{'code_get_m':''},{'fix':'main'}, {'css_find':['main','rule','back']},{'css_find':['main','rule','back']} ,{'return_num': 'back'}]  ,'dddd')
# aqqqa.run()
# print(aqqqa.rep_back)

# aqqqa = analyze('https://www.hetushu.com/book/5625/4195639.html', [{'get_link_f_r': ''}   ,{'add_num': ['rule', '#content']},{'css_find':['main','rule','main']},{'return_num': 'main'}]  ,'dddd')
# aqqqa.run()
# print(aqqqa.rep_back)
#
# aqqqa = analyze('http://127.0.0.1/test/1.html',
#                 [{'add_num': ['a', 1]}, {'add_num': ['b', '齉齾龗麤鱻爩龖']}, {'add_num': ['c', 1]},{'add_num': ['acc', '']},{'add_num': ['aaa', ['齉齾龗麤鱻爩龖','dsdsad','dsdasdas']]},
#                  {'make_list': ['listn', ['a', 'b', 'c']]}, {'for_list': ['aaa', 'iinn',[{'str_add':['acc','iinn','acc']}]]}  ,{'str_add':['a','b','c']},{'return_num': 'acc'}], 'dddd')
# aqqqa.run()
# print(aqqqa.rep_back)

# 齉齾龗麤鱻爩龖
#
# def get2(listt,num):
#     a= num
#     c = listt.keys()
#     c = list(c)[0]
#     print(c)
#     if c == 'test':
#         num['main']=num['main'] +listt[c]
#         return num
#
#
# def get1(html,list1):
#     dir = {'main':html}
#     a = ''
#     for l in list1:
#         print(l)
#         aaa= get2(l,dir)
#         dir = aaa
#     print(dir)
#
# get1('dsadsad',[{'test':'2222'},{'test':'2222'}])
