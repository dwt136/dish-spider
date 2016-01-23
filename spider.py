#!/usr/bin/env python2
from pyquery import PyQuery as pq
import sys
import requesocks
import json
import logging
import codecs


def get(url):
    logging.info('GET: %s' % url)
    try:
        session = requesocks.session()
        session.proxies = {
            'http': 'socks5://localhost:9050',
            'https': 'socks5://localhost:9050',
        }
        r = session.get(url)
        return r.text
    except:
        return None


def grab_dish(link):
    page = get(link)
    if page is None:
        logging.warning('open: %s' % link)
        return None
    if page == '404 Not Found':
        logging.warning('404: %s' % link)
        return None
    parser = pq(page)
    if len(parser('.notfound404_wraper')) == 1:
        logging.warning('404: %s' % link)
        return None
    try:
        dish = {}
        dish['title'] = parser('.title')[0][0].text
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
        return dish
    except:
        logging.warning('parsing: %s' % link)
        return None


def grab_list(prefix, entry):
    link = entry
    while link is not None:
        data = []
        page = get(link)
        parser = pq(page)
        hrefs = [tile.attrib['href'] for tile in parser('.big')]
        for href in hrefs:
            dish = grab_dish(href)
            if dish is not None:
                data.append(dish)
        name = link.replace('/', '-')
        f = codecs.open('result/%s.json' % name, 'w', "utf-8")
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
        f.close()
        next_page = parser('.next')
        link = None if len(next_page) == 0 else next_page[0].attrib['href']
    logging.info('OK: %s' % entry)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: %s <entry>' % sys.argv[0]
        sys.exit(1)
    name = sys.argv[1].replace('/', '-')

    logging.getLogger().setLevel(logging.INFO)
    logFormatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    rootLogger = logging.getLogger()
    fileHandler = logging.FileHandler('logs/%s.log' % name)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    grab_list(name, sys.argv[1])
    print 'Done.'
