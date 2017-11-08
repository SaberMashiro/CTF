#coding:utf-8
import hashlib
import binascii
import HTMLParser
import cgi
import string
import re
import argparse
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
        print u'分为\t'+str(f)+'\t'+'栏时，解密结果为：  '.encode('utf-8')+d

def Kaisa(s):
    table = string.maketrans(string.ascii_lowercase + string.ascii_uppercase,\
     string.ascii_lowercase[1:] + string.ascii_lowercase[:1] + \
     string.ascii_uppercase[1:] + string.ascii_uppercase[:1])
    for i in xrange(26):
        s = s.translate(table)
        print str(i)+"--"+s

Usuage=u'''
    -h --help                     print the help
    -s --h2s                      68656c6c6f  => hello
    -S --h02s                     0x680x650x6c0x6c0x6f => hello
    -d --decode_html              &lt;  =>  <
    -e --encode_html              <  => &lt;
    -z --zhalan                   栅栏密码
    -K --kaisa                    凯撒密码
    注意：winodws里输入特殊字符时应该用 ^转义,如^<
    linux中请用\
    '''
if __name__ == '__main__':
    parser = argparse.ArgumentParser(Usuage)
    parser_group = parser.add_argument_group('a')
    parser_group.add_argument("-s","--h2s",dest="h2s")
    parser_group.add_argument("-S","--h02s",dest="h02s")
    parser_group.add_argument("-d","--decode_html",dest="decode_html")
    parser_group.add_argument("-e","--encode_html",dest="encode_html")
    parser_group.add_argument("-z","--zhalan",dest="zhalan")
    parser_group.add_argument("-K","--kaisa",dest="kaisa")
   # print parser.parse_known_args()
    args,opt = parser.parse_known_args()
    #print args.__dict__
        #print Usage
    #print opt
    try:
        if args.h2s:
            hex2str(args.h2s)
        elif args.h02s:
            hex0x2str(args.h02s)
        elif args.decode_html:
            decode_html(args.decode_html)
        elif args.encode_html:
            print args.encode_html
            print type(args.encode_html)
            encode_html(args.encode_html)
        elif args.zhalan:
            decodeZhalan(args.zhalan)
        elif args.kaisa:
            Kaisa(args.kaisa)
    except:
        print "Unhandled Option"



