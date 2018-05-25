import urllib.request
#from xml.etree.ElementTree import parse
from xml.dom import minidom


class Bus_data():
    def bus_play(self,data):
        id = data
        url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey=umfGiqjtzOMarryKchlVrnqw7%2BGPqeV1bDPWigHtwAFpAB8d5lfQ8TXoBvRDCRecXTrmkbz24APGWQR0kPY3Ow%3D%3D&arsId="
        url = url + id
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

        xmldoc = minidom.parse('test.xml')
        itemlist = xmldoc.getElementsByTagName('itemList')
        item = itemlist[0].getElementsByTagName('arrmsg1')
        return item[0].firstChild.data
