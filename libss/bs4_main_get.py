from bs4 import BeautifulSoup


def bs4_find(html,ru:dict):
    pass
    html =html
    a = BeautifulSoup(html, 'lxml')
    # exp ru={name:'',attrs:{"id": "content"}}

    a= a.find(name=ru['name'], attrs=ru['attrs'])
    return a
def prettify(html): #美化html
    '''

    :param html: 输入的html
    :return: 美化后的html
    '''
    html = html
    a = BeautifulSoup(html, 'lxml')
    a= a.prettify()
    return a

def bs4_find_all(html,ru:dict):
    pass
    html =html
    a = BeautifulSoup(html, 'lxml')
    # exp ru={name:'',attrs:{"id": "content"}}

    a= a.find_all(name=ru['name'], attrs=ru['attrs'])
    return a