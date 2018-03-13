#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------
File Name:    Express
Author:    Mrtutu
Date:    2018/3/10
Description:
------------------------------------

"""
import requests

def inquire(postID):
    requests_url = 'http://www.kuaidi100.com/query'

    parmes = {
        'type': 'tiantian',
        'postid': postID,

    }

    r = requests.post(requests_url, data=parmes)
    return r.json()


def main():
    req = inquire(668426395329)
    print(req)

if __name__ == '__main__':
    main()
