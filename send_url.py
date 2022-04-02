from libss.pika_plus.pika_plus_main import  send_get_list_work


# for i in range(100):
#     send_get_list_work(body='http://127.0.0.1/test/1.html',queue='qqq',exchange='qqq') #最好这里也输入字节

print('请输入爬取的页数')
aa = input()
# print(type(aa))

bb = int(aa)
# print(type(bb))
aaa = 'https://www.52shukuwang.com/gl/index.html'
ccc =aaa.encode('utf8')
# print(ccc)
send_get_list_work(body=ccc,queue='first',exchange='first')
print('正在添加:'+aaa)
i2=2
eeee ='https://www.52shukuwang.com/gl/index_2.html'
if bb>1:
    for i in range(bb-1):
        aew ='https://www.52shukuwang.com/gl/index_'+str(i2)+'.html'
        ccc1 = aew.encode('utf8')

        send_get_list_work(body=ccc,queue='first',exchange='first')
        print('正在添加:'+aew)
        i2 +=1