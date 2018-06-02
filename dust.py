#-*- coding: utf-8 -*-
import urllib.request
#from xml.etree.ElementTree import parse
from xml.dom import minidom


class Dust_data():
    def dust_play(self,pos):
        #data = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구','서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']
        url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?ServiceKey=XOM%2FEajQsNftQu9Gi3BhcIw3Szs0WBMukVi5grFNgLHMuu7WLgc%2FAsNe4MjntZeXjABmJJaSzjhYJ3tBCn4m1A%3D%3D&numOfRows=25&pageSize=30&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&searchCondition=DAILY"
        data = urllib.request.urlopen(url).read()
        xmlFile = "test.xml"
        f = open(xmlFile, "wb")
        f.write(data)
        f.close()
# tree = parse("test.xml")
# note = tree.getroot()
#
# for atype in note.findall('itemList'):
#     print(atype.get('foobar'))
        try:
            data = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']
            found = data.index(pos)
           # print("%d is prime number, index=%d" % (val, found))
            xmldoc = minidom.parse('test.xml')
            body = xmldoc.getElementsByTagName('body')
            itemlist = body[0].getElementsByTagName('items')
            item = itemlist[0].getElementsByTagName('item')[20]
            item_dust = item.getElementsByTagName('pm10Value')
            return item_dust[0].firstChild.data

        except ValueError:
            return "값이 없음"



        #x = check_prime_number(pos)

    def dust_play2(self, pos):
        # data = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구','서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']
        url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?ServiceKey=XOM%2FEajQsNftQu9Gi3BhcIw3Szs0WBMukVi5grFNgLHMuu7WLgc%2FAsNe4MjntZeXjABmJJaSzjhYJ3tBCn4m1A%3D%3D&numOfRows=25&pageSize=30&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&searchCondition=DAILY"
        data = urllib.request.urlopen(url).read()
        xmlFile = "test.xml"
        f = open(xmlFile, "wb")
        f.write(data)
        f.close()
        # tree = parse("test.xml")
        # note = tree.getroot()
        #
        # for atype in note.findall('itemList'):
        #     print(atype.get('foobar'))
        try:
            data = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구',
                    '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']
            found = data.index(pos)
            # print("%d is prime number, index=%d" % (val, found))
            xmldoc = minidom.parse('test.xml')
            body = xmldoc.getElementsByTagName('body')
            itemlist = body[0].getElementsByTagName('items')
            item = itemlist[0].getElementsByTagName('item')[20]
            item_dust = item.getElementsByTagName('pm25Value')
            return item_dust[0].firstChild.data

        except ValueError:
            return "값이 없음"

        # x = check_prime_number(pos)

    def check_prime_number(self,val):
        try:
            data = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']
            found = data.index(val)
            print("%d is prime number, index=%d" % (val, found))
        except ValueError:
            print("%s is not prime number" % (val,))