#! /usr/bin/python3
# -*- coding: utf-8 -*-
import time
import os
import shutil
columns = shutil.get_terminal_size().columns

in_str = "저기 이거 얼른 드세요🥤 "
cnt = 0
a = ''

def wait_for_kana():
    time.sleep(0.5)
    return

while 1:
    if(cnt != 3):
        os.system('clear')
        print(in_str[0:2].center(columns))
        time.sleep(1)
        for i in range(3):
            os.system('clear')
            a = a + '.'
            alpha = (in_str[0:2] + a)
            print(alpha.center(columns))
            wait_for_kana()
        time.sleep(1)
        os.system('clear')
        beta = (in_str[0:2]+a+ " 가나씨!")
        print(beta.center(columns))
        time.sleep(1)
        print(in_str[3:].center(columns))
        time.sleep(2)
        cnt = cnt + 1
        a = ''
    else:
        os.system('clear')
        print("😘😘😘😘😘시들기 전에 😘😘😘😘😘 ".center(columns-4))
        print("🌈🌈🌈To. 꽃가나 From. 🐟🌈🌈🌈".center(columns))
        flowers = ['🌻' for _ in range(0,80)]
        print(''.join(flowers))
        time.sleep(5)
        cnt = 0
