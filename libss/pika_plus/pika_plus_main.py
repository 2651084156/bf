import pika
from config import rabbitmq_config

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



def make_connection_P():
    connection = make_connection(username=username, password=password, host=hostname, port=port1)
    return connection

def send_get_list_work(body,queue,exchange):
# def send_get_list_work(body):
#     queue = 'pikpt'  # 队列名
#     routing_key = 'url_test'
#     exchange = 'pikpt'
    queue = queue  # 队列名
    routing_key = 'url_test'
    exchange = exchange

    connection = make_connection_P()
    channel = connection.channel()
    channel.confirm_delivery()  # 确认

    channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=True)
    # 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
    channel.queue_declare(queue=queue, durable=True)
    channel.queue_bind(exchange=exchange, queue=queue, routing_key=queue)
    aa = channel.basic_publish(exchange=exchange, routing_key=queue, body=body)
    connection.close()
