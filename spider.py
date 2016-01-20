#!/usr/bin/env python2
from gevent import monkey; monkey.patch_socket()
from pyquery import PyQuery as pq
import gevent
import requests
import json


entries = [
    'http://www.meishij.net/chufang/diy/jiangchangcaipu/',
    'http://www.meishij.net/chufang/diy/sijiacai/',
    'http://www.meishij.net/chufang/diy/langcaipu/',
    'http://www.meishij.net/chufang/diy/haixian/',
    'http://www.meishij.net/chufang/diy/recaipu/',
    'http://www.meishij.net/chufang/diy/tangbaocaipu/',
    'http://www.meishij.net/chufang/diy/sushi/',
    'http://www.meishij.net/chufang/diy/jiangliaozhanliao/',
    'http://www.meishij.net/chufang/diy/weibolucaipu/',
    'http://www.meishij.net/chufang/diy/huoguo/',
    'http://www.meishij.net/chufang/diy/tianpindianxin/',
    'http://www.meishij.net/chufang/diy/gaodianxiaochi/',
    'http://www.meishij.net/chufang/diy/ganguo/',
    'http://www.meishij.net/chufang/diy/rujiangcai/',
    'http://www.meishij.net/chufang/diy/yinpin/',
    'http://www.meishij.net/chufang/diy/zaocan/',
    'http://www.meishij.net/chufang/diy/wucan/',
    'http://www.meishij.net/chufang/diy/wancan/',
    'http://www.meishij.net/chufang/diy/xiawucha/',
    'http://www.meishij.net/chufang/diy/yexiao/',
    'http://www.meishij.net/chufang/diy/laonian/',
    'http://www.meishij.net/chufang/diy/chanfu/',
    'http://www.meishij.net/chufang/diy/yunfu/',
    'http://www.meishij.net/chufang/diy/baobaocaipu/',
    'http://www.meishij.net/yaoshanshiliao/jibingtiaoli/',
    'http://www.meishij.net/yaoshanshiliao/gongnengxing/',
    'http://www.meishij.net/yaoshanshiliao/zangfu/',
    'http://www.meishij.net/yaoshanshiliao/renqunshanshi/',
    'http://www.meishij.net/china-food/caixi/chuancai/',
    'http://www.meishij.net/china-food/caixi/xiangcai/',
    'http://www.meishij.net/china-food/caixi/yuecai/',
    'http://www.meishij.net/china-food/caixi/dongbeicai/',
    'http://www.meishij.net/china-food/caixi/lucai/',
    'http://www.meishij.net/china-food/caixi/zhecai/',
    'http://www.meishij.net/china-food/caixi/sucai/',
    'http://www.meishij.net/china-food/caixi/qingzhencai/',
    'http://www.meishij.net/china-food/caixi/mincai/',
    'http://www.meishij.net/china-food/caixi/hucai/',
    'http://www.meishij.net/china-food/caixi/jingcai/',
    'http://www.meishij.net/china-food/caixi/hubeicai/',
    'http://www.meishij.net/china-food/caixi/huicai/',
    'http://www.meishij.net/china-food/caixi/yucai/',
    'http://www.meishij.net/china-food/caixi/xibeicai/',
    'http://www.meishij.net/china-food/caixi/yuguicai/',
    'http://www.meishij.net/china-food/caixi/jiangxicai/',
    'http://www.meishij.net/china-food/caixi/shancicai/',
    'http://www.meishij.net/china-food/caixi/guangxicai/',
    'http://www.meishij.net/china-food/caixi/gangtai/',
    'http://www.meishij.net/china-food/caixi/other/',
    'http://www.meishij.net/china-food/xiaochi/sichuan/',
    'http://www.meishij.net/china-food/xiaochi/guangdong/',
    'http://www.meishij.net/china-food/xiaochi/beijing/',
    'http://www.meishij.net/china-food/xiaochi/shanxii/',
    'http://www.meishij.net/china-food/xiaochi/shandong/',
    'http://www.meishij.net/china-food/xiaochi/shanxi/',
    'http://www.meishij.net/china-food/xiaochi/hunan/',
    'http://www.meishij.net/china-food/xiaochi/henan/',
    'http://www.meishij.net/china-food/xiaochi/shanghai/',
    'http://www.meishij.net/china-food/xiaochi/jiangsu/',
    'http://www.meishij.net/china-food/xiaochi/hubei/',
    'http://www.meishij.net/china-food/xiaochi/chongqing/',
    'http://www.meishij.net/china-food/xiaochi/tianjin/',
    'http://www.meishij.net/china-food/xiaochi/hebei/',
    'http://www.meishij.net/china-food/xiaochi/zhejiang/',
    'http://www.meishij.net/china-food/xiaochi/xinjiang/',
    'http://www.meishij.net/china-food/xiaochi/jiangxi/',
    'http://www.meishij.net/china-food/xiaochi/fujian/',
    'http://www.meishij.net/china-food/xiaochi/guangxi/',
    'http://www.meishij.net/china-food/xiaochi/yunnan/',
    'http://www.meishij.net/china-food/xiaochi/liaoning/',
    'http://www.meishij.net/china-food/xiaochi/jilin/',
    'http://www.meishij.net/china-food/xiaochi/guizhou/',
    'http://www.meishij.net/china-food/xiaochi/anhui/',
    'http://www.meishij.net/china-food/xiaochi/taiwan/',
    'http://www.meishij.net/china-food/xiaochi/gansu/',
    'http://www.meishij.net/china-food/xiaochi/xianggang/',
    'http://www.meishij.net/china-food/xiaochi/menggu/',
    'http://www.meishij.net/china-food/xiaochi/ningxia/',
    'http://www.meishij.net/china-food/xiaochi/qinghai/',
    'http://www.meishij.net/china-food/xiaochi/hainan/',
    'http://www.meishij.net/china-food/xiaochi/xizang/',
    'http://www.meishij.net/china-food/xiaochi/chengduxiaochi/',
    'http://www.meishij.net/china-food/xiaochi/heilongjiang/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/hanguo/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/japan/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/ccmd/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/faguo/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/yidali/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/usa/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/dongnanya/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/moxige/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/aozhou/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/other/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/canqianxiaochi/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/tangpin/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/zhucai/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/zhushi/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/yinpin/',
    'http://www.meishij.net/chufang/diy/guowaicaipu1/tiandian/',
    'http://www.meishij.net/hongpei/dangaomianbao/',
    'http://www.meishij.net/hongpei/bingganpeifang/',
    'http://www.meishij.net/hongpei/tianpindianxin/',
    'http://www.meishij.net/hongpei/hongpeigongju/',
    'http://www.meishij.net/hongpei/hongpeichangshi/',
    'http://www.meishij.net/hongpei/hongpeiyuanliao/',
    ]


data = {}


def grab_dish(link):
    page = requests.get(link).text
    if page == '404 Not Found':
        return
    parser = pq(page)
    dish = {}
    try:
        title = parser('.title')[0][0].text
    except:
        print 'ERR'
        print page
    dish['title'] = title
    dish['craft'] = parser('.w127')[0][1].text
    dish['taste'] = parser('.w127')[1][1].text
    dish['difficulty'] = parser('.w270')[0][1][2].text
    dish['people'] = int('0' + parser('.w270')[1][1][2].text[:-2])
    dish['prepare_time'] = parser('.w270')[2][1][2].text
    dish['process_time'] = parser('.w270')[3][1][2].text
    dish['description'] = parser('.materials p').html()[18:-18]
    dish['main_ingre'] = {i[0].text: i[1].text for i in parser('.zl h4')}
    dish['sub_ingre'] = {i[0][0].text: i[1].text for i in parser('.fuliao li')}
    data[title] = dish


def grab_list(entry):
    dishes = []
    link = entry
    while link is not None:
        page = requests.get(entry).text
        parser = pq(page)
        hrefs = [tile.attrib['href'] for tile in parser('.big')]
        dishes += [gevent.spawn(grab_dish, href) for href in hrefs]
        next_page = parser('.next')
        link = None if len(next_page) == 0 else next_page[0].attrib['href']
    gevent.joinall(dishes)
    print 'OK: %s' % entry


if __name__ == '__main__':
    gevent.joinall([gevent.spawn(grab_list, e) for e in entries])
    with open('result', 'w') as f:
        f.write(json.dumps([i[1] for i in data.iteritems()]))
    print 'Done.'
