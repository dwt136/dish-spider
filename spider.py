#!/usr/bin/env python2
from pyquery import PyQuery as pq
import requesocks
import json
import logging
import time


entries = {
    'jiangchangcaipu': 'http://www.meishij.net/chufang/diy/jiangchangcaipu/',
    'sijiacai': 'http://www.meishij.net/chufang/diy/sijiacai/',
    'langcaipu': 'http://www.meishij.net/chufang/diy/langcaipu/',
    'haixian': 'http://www.meishij.net/chufang/diy/haixian/',
    'recaipu': 'http://www.meishij.net/chufang/diy/recaipu/',
    'tangbaocaipu': 'http://www.meishij.net/chufang/diy/tangbaocaipu/',
    'sushi': 'http://www.meishij.net/chufang/diy/sushi/',
    'jiangliaozhanliao': 'http://www.meishij.net/chufang/diy/jiangliaozhanliao/',
    'weibolucaipu': 'http://www.meishij.net/chufang/diy/weibolucaipu/',
    'huoguo': 'http://www.meishij.net/chufang/diy/huoguo/',
    'tianpindianxin': 'http://www.meishij.net/chufang/diy/tianpindianxin/',
    'gaodianxiaochi': 'http://www.meishij.net/chufang/diy/gaodianxiaochi/',
    'ganguo': 'http://www.meishij.net/chufang/diy/ganguo/',
    'rujiangcai': 'http://www.meishij.net/chufang/diy/rujiangcai/',
    'yinpin': 'http://www.meishij.net/chufang/diy/yinpin/',
    'zaocan': 'http://www.meishij.net/chufang/diy/zaocan/',
    'wucan': 'http://www.meishij.net/chufang/diy/wucan/',
    'wancan': 'http://www.meishij.net/chufang/diy/wancan/',
    'xiawucha': 'http://www.meishij.net/chufang/diy/xiawucha/',
    'yexiao': 'http://www.meishij.net/chufang/diy/yexiao/',
    'laonian': 'http://www.meishij.net/chufang/diy/laonian/',
    'chanfu': 'http://www.meishij.net/chufang/diy/chanfu/',
    'yunfu': 'http://www.meishij.net/chufang/diy/yunfu/',
    'baobaocaipu': 'http://www.meishij.net/chufang/diy/baobaocaipu/',
    'jibingtiaoli': 'http://www.meishij.net/yaoshanshiliao/jibingtiaoli/',
    'gongnengxing': 'http://www.meishij.net/yaoshanshiliao/gongnengxing/',
    'zangfu': 'http://www.meishij.net/yaoshanshiliao/zangfu/',
    'renqunshanshi': 'http://www.meishij.net/yaoshanshiliao/renqunshanshi/',
    'chuancai': 'http://www.meishij.net/china-food/caixi/chuancai/',
    'xiangcai': 'http://www.meishij.net/china-food/caixi/xiangcai/',
    'yuecai': 'http://www.meishij.net/china-food/caixi/yuecai/',
    'dongbeicai': 'http://www.meishij.net/china-food/caixi/dongbeicai/',
    'lucai': 'http://www.meishij.net/china-food/caixi/lucai/',
    'zhecai': 'http://www.meishij.net/china-food/caixi/zhecai/',
    'sucai': 'http://www.meishij.net/china-food/caixi/sucai/',
    'qingzhencai': 'http://www.meishij.net/china-food/caixi/qingzhencai/',
    'mincai': 'http://www.meishij.net/china-food/caixi/mincai/',
    'hucai': 'http://www.meishij.net/china-food/caixi/hucai/',
    'jingcai': 'http://www.meishij.net/china-food/caixi/jingcai/',
    'hubeicai': 'http://www.meishij.net/china-food/caixi/hubeicai/',
    'huicai': 'http://www.meishij.net/china-food/caixi/huicai/',
    'yucai': 'http://www.meishij.net/china-food/caixi/yucai/',
    'xibeicai': 'http://www.meishij.net/china-food/caixi/xibeicai/',
    'yuguicai': 'http://www.meishij.net/china-food/caixi/yuguicai/',
    'jiangxicai': 'http://www.meishij.net/china-food/caixi/jiangxicai/',
    'shancicai': 'http://www.meishij.net/china-food/caixi/shancicai/',
    'guangxicai': 'http://www.meishij.net/china-food/caixi/guangxicai/',
    'gangtai': 'http://www.meishij.net/china-food/caixi/gangtai/',
    'other': 'http://www.meishij.net/china-food/caixi/other/',
    'sichuan': 'http://www.meishij.net/china-food/xiaochi/sichuan/',
    'guangdong': 'http://www.meishij.net/china-food/xiaochi/guangdong/',
    'beijing': 'http://www.meishij.net/china-food/xiaochi/beijing/',
    'shanxii': 'http://www.meishij.net/china-food/xiaochi/shanxii/',
    'shandong': 'http://www.meishij.net/china-food/xiaochi/shandong/',
    'shanxi': 'http://www.meishij.net/china-food/xiaochi/shanxi/',
    'hunan': 'http://www.meishij.net/china-food/xiaochi/hunan/',
    'henan': 'http://www.meishij.net/china-food/xiaochi/henan/',
    'shanghai': 'http://www.meishij.net/china-food/xiaochi/shanghai/',
    'jiangsu': 'http://www.meishij.net/china-food/xiaochi/jiangsu/',
    'hubei': 'http://www.meishij.net/china-food/xiaochi/hubei/',
    'chongqing': 'http://www.meishij.net/china-food/xiaochi/chongqing/',
    'tianjin': 'http://www.meishij.net/china-food/xiaochi/tianjin/',
    'hebei': 'http://www.meishij.net/china-food/xiaochi/hebei/',
    'zhejiang': 'http://www.meishij.net/china-food/xiaochi/zhejiang/',
    'xinjiang': 'http://www.meishij.net/china-food/xiaochi/xinjiang/',
    'jiangxi': 'http://www.meishij.net/china-food/xiaochi/jiangxi/',
    'fujian': 'http://www.meishij.net/china-food/xiaochi/fujian/',
    'guangxi': 'http://www.meishij.net/china-food/xiaochi/guangxi/',
    'yunnan': 'http://www.meishij.net/china-food/xiaochi/yunnan/',
    'liaoning': 'http://www.meishij.net/china-food/xiaochi/liaoning/',
    'jilin': 'http://www.meishij.net/china-food/xiaochi/jilin/',
    'guizhou': 'http://www.meishij.net/china-food/xiaochi/guizhou/',
    'anhui': 'http://www.meishij.net/china-food/xiaochi/anhui/',
    'taiwan': 'http://www.meishij.net/china-food/xiaochi/taiwan/',
    'gansu': 'http://www.meishij.net/china-food/xiaochi/gansu/',
    'xianggang': 'http://www.meishij.net/china-food/xiaochi/xianggang/',
    'menggu': 'http://www.meishij.net/china-food/xiaochi/menggu/',
    'ningxia': 'http://www.meishij.net/china-food/xiaochi/ningxia/',
    'qinghai': 'http://www.meishij.net/china-food/xiaochi/qinghai/',
    'hainan': 'http://www.meishij.net/china-food/xiaochi/hainan/',
    'xizang': 'http://www.meishij.net/china-food/xiaochi/xizang/',
    'chengduxiaochi': 'http://www.meishij.net/china-food/xiaochi/chengduxiaochi/',
    'heilongjiang': 'http://www.meishij.net/china-food/xiaochi/heilongjiang/',
    'hanguo': 'http://www.meishij.net/chufang/diy/guowaicaipu1/hanguo/',
    'japan': 'http://www.meishij.net/chufang/diy/guowaicaipu1/japan/',
    'ccmd': 'http://www.meishij.net/chufang/diy/guowaicaipu1/ccmd/',
    'faguo': 'http://www.meishij.net/chufang/diy/guowaicaipu1/faguo/',
    'yidali': 'http://www.meishij.net/chufang/diy/guowaicaipu1/yidali/',
    'usa': 'http://www.meishij.net/chufang/diy/guowaicaipu1/usa/',
    'dongnanya': 'http://www.meishij.net/chufang/diy/guowaicaipu1/dongnanya/',
    'moxige': 'http://www.meishij.net/chufang/diy/guowaicaipu1/moxige/',
    'aozhou': 'http://www.meishij.net/chufang/diy/guowaicaipu1/aozhou/',
    'other': 'http://www.meishij.net/chufang/diy/guowaicaipu1/other/',
    'canqianxiaochi': 'http://www.meishij.net/chufang/diy/guowaicaipu1/canqianxiaochi/',
    'tangpin': 'http://www.meishij.net/chufang/diy/guowaicaipu1/tangpin/',
    'zhucai': 'http://www.meishij.net/chufang/diy/guowaicaipu1/zhucai/',
    'zhushi': 'http://www.meishij.net/chufang/diy/guowaicaipu1/zhushi/',
    'yinpin': 'http://www.meishij.net/chufang/diy/guowaicaipu1/yinpin/',
    'tiandian': 'http://www.meishij.net/chufang/diy/guowaicaipu1/tiandian/',
    'dangaomianbao': 'http://www.meishij.net/hongpei/dangaomianbao/',
    'bingganpeifang': 'http://www.meishij.net/hongpei/bingganpeifang/',
    'tianpindianxin': 'http://www.meishij.net/hongpei/tianpindianxin/',
    'hongpeigongju': 'http://www.meishij.net/hongpei/hongpeigongju/',
    'hongpeichangshi': 'http://www.meishij.net/hongpei/hongpeichangshi/',
    'hongpeiyuanliao': 'http://www.meishij.net/hongpei/hongpeiyuanliao/',
}


def get(url):
    logging.info('GET: %s' % url)
    session = requesocks.session()
    r = session.get(url)
    return r.text


def grab_dish(link):
    page = get(link)
    if page == '404 Not Found':
        logging.warning('404: %s' % link)
        return None, None
    parser = pq(page)
    if len(parser('.notfound404_wraper')) == 1:
        logging.warning('404: %s' % link)
        return None, None
    try:
        dish = {}
        title = parser('.title')[0][0].text
        dish['title'] = title
        dish['craft'] = parser('.w127')[0][1].text
        dish['taste'] = parser('.w127')[1][1].text
        dish['difficulty'] = parser('.w270')[0][1][2].text
        dish['people'] = int('0' + parser('.w270')[1][1][2].text[:-2])
        dish['prepare_time'] = parser('.w270')[2][1][2].text
        dish['process_time'] = parser('.w270')[3][1][2].text
        desc_html = parser('.materials p').html()
        dish['description'] = '' if desc_html is None else desc_html[18:-18]
        dish['main_ingre'] = {}
        for i in parser('.zl h4'):
            dish['main_ingre'][i[0].text] = i[1].text
        dish['sub_ingre'] = {}
        for i in parser('.fuliao li'):
            dish['sub_ingre'][i[0][0].text] = i[1].text
        logging.info('OK: %s' % link)
        return title, dish
    except:
        logging.warning('parsing: %s' % link)
        return None, None


def grab_list(prefix, entry):
    data = {}
    link = entry
    while link is not None:
        page = get(entry)
        parser = pq(page)
        hrefs = [tile.attrib['href'] for tile in parser('.big')]
        for href in hrefs:
            title, dish = grab_dish(href)
            if title is not None:
                data[title] = dish
            time.sleep(0.8)
        next_page = parser('.next')
        link = None if len(next_page) == 0 else next_page[0].attrib['href']
    with open('result/%s.json' % prefix, 'w') as f:
        f.write(json.dumps([i[1] for i in data.iteritems()]))
    logging.info('OK: %s' % entry)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    rootLogger = logging.getLogger()
    fileHandler = logging.FileHandler("spider.log")
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    for p, e in entries.iteritems():
        grab_list(p, e)
    print 'Done.'
