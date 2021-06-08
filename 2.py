# !/usr/bin/env python3
# -*- coding: utf-8 -*-

f = ''
if __name__ == '__main__':
    s = "очепятка"
    print("до:", s)
    f += s[0] + s[3] + s[2] + s[1] + s[7] + s[5] + s[6] + s[7]
    print("после:", f)
