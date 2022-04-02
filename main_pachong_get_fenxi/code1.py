import chardet


def code_get(txt):

    code = chardet.detect(txt.content)  # 获取编码

    if code['encoding'] == 'utf-8':
        a3 = txt.content.decode('utf-8')

        return a3
    else:
        try:
            fwe = txt.content.decode(code['encoding'])

            fwe1 = fwe.encode('utf-8')
            ff = fwe1.decode('utf-8')
            return ff
        except UnicodeDecodeError:
            if code['encoding'] == 'GB2312':
                fwe = txt.content.decode('gbk')

                fwe1 = fwe.encode('utf-8')
                ff = fwe1.decode('utf-8')
                return ff

def code_getb(txt):
    code = chardet.detect(txt)  # 获取编码

    if code['encoding'] == 'utf-8':
        a3 = txt.decode('utf-8')

        return a3
    else:

        fwe = txt.decode(code['encoding'])

        fwe1 = fwe.encode('utf-8')
        ff = fwe1.decode('utf-8')
        return ff
