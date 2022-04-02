import requests
from requests_html import HTMLSession



def get_requests_html(link, headers, timeout=10, try_number=1):
    i = 0
    while i < try_number:
        try:
            s = HTMLSession()
            c = s.get(link, headers=headers, timeout=timeout)
            print(c)
            return c
        # except requests.exceptions.ConnectTimeout:
        except :
            i = i + 1

    return 'time_out@@@@@@@'
    # i = 0
    #
    # s = HTMLSession()
    # c = s.get(link, headers=headers, timeout=timeout)
    # print(c)
    # return c
    #
    #     # except requests.exceptions.ConnectTimeout:


    # return 'time_out@@@@@@@'




def get_requests_html2(link, headers, timeout=10, try_number=1):
    a =get_requests_html(link=link,headers=headers,timeout=timeout,try_number=try_number)

    if a != 'time_out@@@@@@@':
        if a.status_code == 200:
            return a
        else:

            return ['errrr',a.status_code]

    return ['time_out@@@@@@@']