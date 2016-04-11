# http://www.pythonchallenge.com/pc/def/map.html

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
result = []

for l in str:
    if ord(l) in range(97, 123):
        if ord(l) + 2 > 122:
            result.append(chr(97 - 1 + (ord(l)+2) % 122))
        else:
            result.append(chr(ord(l)+2))


    else:
        result.append(l)

print "".join(result)
# i hope you didnt translate it zy hand. thats what computers are for. doing it in zy hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.


import string

a = "abcdefghijklmnopqrstuvwxyz"
b = "cdefghijklmnopqrstuvwxyzab"

table = string.maketrans(a, b)
print table
print str.translate(table)