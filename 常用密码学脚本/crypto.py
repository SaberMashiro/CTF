#coding:utf-8
import hashlib
import binascii
import HTMLParser
import cgi
import string
import re
import getopt

def hex2str(s):# 68656c6c6f  => hello
    print binascii.unhexlify(s)

def hex0x2str(s):#0x680x650x6c0x6c0x6f => hello
    s = s.replace('0x','')
    print binascii.unhexlify(s)

def decode_html(s):#&lt;  =>  <
    html_parser = HTMLParser.HTMLParser()
    print html_parser.unescape(s)

def encode_html(s):# <  => &lt;
    print cgi.escape(s)

def decodeZhalan(s):
    elen = s.__len__()
    field=[]
    for i in range(2,elen):
             if(elen%i==0):
                 field.append(i)

    for f in field:
        b = elen / f
        result = {x:'' for x in xrange(b)}
        for i in xrange(elen):
            a = i % b;
            result.update({a:result[a] + s[i]})
        d = ''
        for i in range(b):
            d = d + result[i]
        print '分为\t'+str(f)+'\t'+'栏时，解密结果为：  '+d

def Kaisa(s):
    table = string.maketrans(string.ascii_lowercase + string.ascii_uppercase,\
     string.ascii_lowercase[i:] + string.ascii_lowercase[:i] + \
     string.ascii_uppercase[i:] + string.ascii_uppercase[:i])
    for i in xrange(26):
        s = s.translate(table)
        print str(i)+"--"+s

def usage():
    #提示信息
    print '''
    -h --help                     print the help
    -s --h2s                      68656c6c6f  => hello
    -S --h02s                     0x680x650x6c0x6c0x6f => hello
    -d --decode_html              &lt;  =>  <
    -e --encode_html              <  => &lt;
    -z --zhalan                   栅栏密码
    -K --kaisa                    凯撒密码

    '''
if __name__ == '__main__':
    try:
        opts,args = getopt.getopt(sys.argv[1:],"hc::",["help","h2s=","h02s=",\
            "decode_html=","encode_html=","zhalan=","kaisa="])
    except getopt.GetoptError as err:
        print str(err)
        usage()
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-s","--h2s"):
            hex2str(a)
        elif o in ("-S","--h02s"):
            hex0x2str(a)
        elif o in ("-d","--decode_html"):
            decode_html(a)
        elif o in ("-e","--encode_html"):
            encode_html(a)
        elif o in ("-z","--zhalan"):
            decodeZhalan(a)
        elif o in ("-K","--kaisa"):
            Kaisa(a)

        else:
            assert False,"Unhandled Option"



