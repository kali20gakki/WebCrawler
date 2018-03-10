#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------
File Name:    XiaoMi_API
Author:    Mrtutu
Date:    2018/3/10
Description:
------------------------------------

"""
import pygame
from aip import AipSpeech
import time
APP_ID = '10905127'
API_KEY = 'rD22XxBTNkhHv9SldqHD4WAv'
SECRET_KEY = 'oADbxnKio1jeyoaMM6IlrvOan8ttLFwF'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

content = 'surprise motherfucker'
result = client.synthesis(content, 'en ', 1, {
    'vol': 8,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

pygame.mixer.init()
print('auido.mp3')
pygame.mixer.music.set_volume(0.5)
track = pygame.mixer.music.load('auido.mp3')
pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.stop()