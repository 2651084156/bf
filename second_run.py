from main_pachong_get_fenxi.main_pachong_get_fenxi import analyze
from config import rabbitmq_config
import pika
from libss.pika_plus.pika_plus_main import  send_get_list_work
def make_connection(username,password,host,port):
    '''

    :param username: rabbitmq的用户名
    :param password:rabbitmq的密码
    :param host:rabbitmq的ip地址
    :param port:rabbitmq的端口
    :return: 返回连接对象
    '''
    credentials = pika.PlainCredentials(username=username, password=password)
    parameters = pika.ConnectionParameters(host=host, port=port, credentials=credentials)
    connection = pika.BlockingConnection(parameters=parameters)
    return connection

hostname = rabbitmq_config.rabbitmq_hostname
port1=rabbitmq_config.rabbitmq_port
username =rabbitmq_config.rabbitmq_username
password=rabbitmq_config.rabbitmq_password
#
# hostname = '192.168.1.112'
# port=5672
def make_connection_P():
    connection12 = make_connection(username=username, password=password, host=hostname, port=port1)
    return connection12

# queue = 'oss.url_test'
queue = 'senc'

connection = make_connection_P()
channel = connection.channel()
channel.queue_declare(queue=queue,durable=True)

def callback(ch, method, properties, body): #返回的是字节
    # print (" [x] Received %r" % (body,))
    ccc =body.decode("utf-8")
    print('开始处理：' + ccc)
    a123 =analyze(link=ccc,get_rule=[{'get_link_f': ''} ,{'code_get_m':''} ,{'xpath_get':['main','/html/body/div[2]/div/div[3]/ul/*//a/@href','back']},{'for_list':['back','abd',[ {'add_list':['aaaee','abd']}] ]},{'return_num':'aaaee'}],uuid=114514)
    a123.run()
    ccc = a123.rep_back
    for i in ccc:
        ac = 'https://www.52shukuwang.com' + i
        aa = ac.encode('utf-8')
        # print(aa)

        send_get_list_work(body=aa, queue='thri', exchange='thri')  # 最好这里也输入字节



    # print(properties)
    # print(method)
    # print(method.delivery_tag)
    # print(ch)

    ch.basic_ack(delivery_tag=method.delivery_tag)  # 发送ack消息

#添加不按顺序分配消息的参数,可有可无
# channel.basic_qos(prefetch_count=1)
# 告诉rabbitmq使用callback来接收信息
channel.basic_consume(on_message_callback=callback,queue=queue,auto_ack=False)#no_ack来标记是否需要发送ack，默认是False，开启状态

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理,按ctrl+c退出
# print(' [*] Waiting for messages. To exit press CTRL+C')
# a=channel.basic_get(queue=queue,auto_ack=True)
# print(a)
# if a[0 ] is None:
#     print('nnnnnnn')
channel.start_consuming()
