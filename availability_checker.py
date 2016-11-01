# coding=utf-8
import time

import requests
from lxml import html


def get_airpods():
    url = "http://www.apple.com/uk/airpods/"
    page = requests.get(url)
    tree = html.fromstring(page.content)
    for elements in tree:
        for e in elements:
            print e
    result = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "violator", " " ))]/text()')[0]
    return result

if __name__ == "__main__":
    result = get_airpods()
    print result
    while True:
        if result != u"10 月底发售":
            # 通过server酱发送通知,替换<yourkey>部分内容
            #requests.get('http://sc.ftqq.com/<yourkey>send?text=airpods 发布时间:%s' % result)
            break
        else:
            time.sleep(5*60)
            result = get_airpods()
            print result