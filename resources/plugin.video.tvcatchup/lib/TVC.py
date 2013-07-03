#       Copyright (C) 2012 
#       Written on behalf of TVCatchup
#       by Chris Grove (tvc@killergerbils.co.uk)
#       and Sean Poyser (seanpoyser@gmail.com)
#

import urllib2,urllib
import datetime
import base64
import xbmcaddon
import xbmcgui
import xbmc
import os
import re
import platform
from xml.etree import ElementTree

import dialogue

fuscat1=xbmcaddon.Addon(id='plugin.video.tvcatchup')

def Niswanob1(ordemo2):
 fuscat2=ord(ordemo2)
 return fuscat2

def fuscat3(bitboostdotcom1):
 bitboostdotcom2=chr(bitboostdotcom1)
 return bitboostdotcom2

def fuscat4(ordemo3):
 bitboostdotcom3=len(ordemo3)
 return bitboostdotcom3

def Chri3(Chri2,ordemo4):
 Niswanob2=int(Chri2,ordemo4)
 return Niswanob2

def bitboostdotcom5(Chri4,Niswanob3):
 bitboostdotcom4=''
 ordemo5=0
 Niswanob4=base64.b64decode(Chri4)
 Chri5=[Chri6 for Chri6 in       Niswanob4 if (Chri6!='\n') ]
 fuscat5=[Chri6 for Chri6 in       Niswanob3 if (Chri6!='\n') ]
 for Niswanob5 in range(0,fuscat4(Chri5),16):
  for Niswanob6 in range(0,8):
   if ((ordemo5 + Chri3(fuscat5[Niswanob6],16))<=fuscat4(Chri5)):
    bitboostdotcom4=(bitboostdotcom4 + fuscat3((Niswanob1(Chri5[(ordemo5 + Chri3(fuscat5[Niswanob6],16))]) - Chri3(fuscat5[(Niswanob6 + 8)],16))))


  ordemo5=(ordemo5 + 16)

 return bitboostdotcom4.rstrip(' ')

def fuscat7(Chri7,Chri8):
 if (Chri8==1):
  fuscat6='ba98763223b38343'
 elif (Chri8==2):
  fuscat6='d37e194813579bdf'
 elif (Chri8==3):
  fuscat6='38a7629b43303002'
 elif (Chri8==4):
  fuscat6='38d762ce433833b2'

 ordemo7=bitboostdotcom5(Chri7,fuscat6)
 return ordemo7

YV5SWko3TFtIa05NWVUiaQ=fuscat1.getAddonInfo(fuscat7('elhvenl1bHNobnUiUUsiNA==',3))

def bitboostdotcom7():
 today=datetime.datetime.today()
 ordemo8=today.strftime('%d')
 Chri9=today.strftime('%m')
 ChriA=today.strftime('%y')
 Niswanob7=today.strftime('%H')
 bitboostdotcom6=today.strftime('%M')
 Niswanob8=''
 Niswanob8=(Niswanob8 + ordemo8)
 Niswanob8=(Niswanob8 + fuscat3((Chri3(ordemo8,10) + 64)))
 Niswanob8=(Niswanob8 + fuscat3(((Chri3(ordemo8,10)*    2) + 64)))
 Niswanob8=(Niswanob8 + Chri9)
 Niswanob8=(Niswanob8 + fuscat3((Chri3(Chri9,10) + 64)))
 Niswanob8=(Niswanob8 + fuscat3(((Chri3(Chri9,10)*    2) + 64)))
 Niswanob8=(Niswanob8 + ChriA)
 Niswanob8=(Niswanob8 + fuscat3((Chri3(ChriA,10) + 64)))
 Niswanob8=(Niswanob8 + fuscat3(((Chri3(ChriA,10)*    2) + 64)))
 Niswanob8=(Niswanob8 + Niswanob7)
 Niswanob8=(Niswanob8 + fuscat3((Chri3(Niswanob7,10) + 64)))
 Niswanob8=(Niswanob8 + fuscat3(((Chri3(Niswanob7,10)*    2) + 64)))
 return base64.b64encode(Niswanob8)

def loadTVCXml():
 NiswanobA=bitboostdotcom7()
 AbitboostdotcomA=[(fuscat7('eilydi0tOWovKzkpK3Z5OA==',2),fuscat1.getSetting(fuscat7('JyFxdjFnaHt4bnl2bXJSUmpsIyRvSyMoI3BwY2hLOnc=',1))),(fuscat7('bjAjdFZlI3tkND85K3YiWA==',4),fuscat1.getSetting(fuscat7('ZEZzeG9aZHB5c2Z5d1s+QE91IHMvYiMgdSBnIndZXGg=',3))),(fuscat7('WGAjZzhndnZrO1kwK2QiVQ==',4),fuscat7('TjwgZy5FI25rIGQiIndmMQ==',3)),(fuscat7('KCYjfT1BaHN2fmRybFxZeQ==',1),NiswanobA),(fuscat7('JDtvei9lbHNobnUiUUA/Yg==',3),YV5SWko3TFtIa05NWVUiaQ)]
 AbitboostdotcomA=urllib.urlencode(AbitboostdotcomA)
 bitboostdotcomA=fuscat7('OmAvbEh5PXB3L3dyL0AiWVtGc3A5VnFpeC5qdlhXRkwzYmh6RiJmdGZ1ZHIlTSs0TU9+Mm5EMm1meHJkbTVacDdqbXFUeWV4ZmMyZyVDW1M+Q2h0Z1VzLmpwNSJvbzFI',3)
 req=urllib2.Request(bitboostdotcomA, AbitboostdotcomA)
 req.add_header("Content-type", "application/x-www-form-urlencoded")
 bitboostdotcom8=urllib2.urlopen(req).read()
 IiII1I1Tit = re.compile('<div style="background: red; padding: 10px; color: #FFFFFF">(.+?)</div>').findall(bitboostdotcom8)
 if len(IiII1I1Tit) <> 0:
  dialogue.doOK('TVCatchup', ['', 'Listings Download Error', IiII1I1Tit[0]])
  xbmc.log('script.tvcatchup - Plugin halted. '+IiII1I1Tit[0]+' http://plugins.tvcatchup.com/~xbmc/')
  exit()
 else:
  try:
   ret = ElementTree.fromstring(bitboostdotcom8)
  except:
   dialogue.doOK('TVCatchup', ['', 'XMLTV Location Issue', 'Please check you Location\Time Zone settings'])
   xbmc.log('[script.tvcatchup] - XMLTV Location Issue Tripped')
   xbmc.log('script.tvcatchup ' + bitboostdotcom8)
   exit()
  if ret <> None:
   return ret
  else:
   dialogue.doOK('TVCatchup', ['', 'Listings Download Error', 'Please check your settings and try again.'])
   xbmc.log('[script.tvcatchup] - Plugin halted due to the XML being empty. Check you can connect to http://plugins.tvcatchup.com/~xbmc/')
   exit()

def getMissingNow(bitboostdotcom6):
 bitboostdotcom9=None
 NiswanobA=bitboostdotcom7()
 AbitboostdotcomA=[(fuscat7('KCYjfT1BaHN2fmRybFxZeQ==',1),NiswanobA),(fuscat7('NGcjJGIiIyh1cHZ3U05ubw==',1),(fuscat1.getSetting(fuscat7('QmZxdngnaHt4bnl2OC0qOnRYIyQnOyMoI3BwY04hMEk=',1)))),(fuscat7('XlN4cmhXaG5ydHoiIT1OSw==',3),fuscat7('IylMci1VK3wvK3ckWG8nNQ==',2)),(fuscat7('a3c+a3liKWYvcElWO2R1Zw==',2),bitboostdotcom6)]
 AbitboostdotcomA=urllib.urlencode(AbitboostdotcomA)
 ordemo9=fuscat7('ckwvbEx3PXB3L3dyTz0kVnI9c3BgTnFpeC5qdlNWczxtNWh6JDhmdGZ1ZHI4ZFVMemN+Ml4nMm1meHJkOFUtbzJIbXE2VWV4ZmMyZ3VuQEhlSWh0U2NzLmpwNSJpN0M+',3)
 req=urllib2.Request(ordemo9, AbitboostdotcomA)
 req.add_header("Content-type", "application/x-www-form-urlencoded")
 bitboostdotcom8=urllib2.urlopen(req).read()
 IiII1I1Tit = re.compile('<title>(.+?)</title>').findall(bitboostdotcom8)
 IiII1I1Sta = re.compile('<start>(.+?)</start>').findall(bitboostdotcom8)
 IiII1I1End = re.compile('<end>(.+?)</end>').findall(bitboostdotcom8)
 bitboostdotcom9=[IiII1I1Tit[0],IiII1I1Sta[0],IiII1I1End[0]]
 return bitboostdotcom9

def getMissingNext(bitboostdotcom6):
 NiswanobA=bitboostdotcom7()
 AbitboostdotcomA=[(fuscat7('KCYjfT1BaHN2fmRybFxZeQ==',1),NiswanobA),(fuscat7('NGcjJGIiIyh1cHZ3U05ubw==',1),(fuscat1.getSetting(fuscat7('QmZxdngnaHt4bnl2OC0qOnRYIyQnOyMoI3BwY04hMEk=',1)))),(fuscat7('XlN4cmhXaG5ydHoiIT1OSw==',3),fuscat7('SUQjclF4I3xoMkMpK3siMg==',4)),(fuscat7('a3c+a3liKWYvcElWO2R1Zw==',2),bitboostdotcom6)]
 AbitboostdotcomA=urllib.urlencode(AbitboostdotcomA)
 ordemo9=fuscat7('ckwvbEx3PXB3L3dyTz0kVnI9c3BgTnFpeC5qdlNWczxtNWh6JDhmdGZ1ZHI4ZFVMemN+Ml4nMm1meHJkOFUtbzJIbXE2VWV4ZmMyZ3VuQEhlSWh0U2NzLmpwNSJpN0M+',3)
 req=urllib2.Request(ordemo9, AbitboostdotcomA)
 req.add_header("Content-type", "application/x-www-form-urlencoded")
 bitboostdotcom8=urllib2.urlopen(req).read()
 IiII1I1Tit = re.compile('<title>(.+?)</title>').findall(bitboostdotcom8)
 IiII1I1Sta = re.compile('<start>(.+?)</start>').findall(bitboostdotcom8)
 IiII1I1End = re.compile('<end>(.+?)</end>').findall(bitboostdotcom8)
 bitboostdotcom9=[IiII1I1Tit[0],IiII1I1Sta[0],IiII1I1End[0]]
 return bitboostdotcom9

def getTVCStreamUrl(NiswanobB,fuscat8):
 fuscat9=bitboostdotcom7()
 AbitboostdotcomA=[(fuscat7('djQjJGBDIyh1cHZ3b2g3JA==',1),fuscat1.getSetting(fuscat7('JyFxdjFnaHt4bnl2bXJSUmpsIyRvSyMoI3BwY2hLOnc=',1))),(fuscat7('RXYgdFAhI3NkIHYiVUZFWQ==',3),fuscat1.getSetting(fuscat7('b2pkeYAsaWiGfnAwenV3SFApdXUtVy9pLys1aDZwJ3U=',2))),(fuscat7('W1AgZ2EjI25rIGQiTFonWg==',3),fuscat8.id),(fuscat7('THgjfVdIaHN2fmRyXydbLQ==',1),fuscat9),(fuscat7('elhvenl1bHNobnUiUUsiNA==',3),YV5SWko3TFtIa05NWVUiaQ),(fuscat7('RSsjfUY4d3FvbHhzN1tdVA==',1),fuscat1.getSetting(fuscat7('Ilxfem1NcmVsc2d2LGNUclRHIHZKPiNtaCBkIic0JS0=',3))),(fuscat7('XmpEd3Y5Wnd9eERDM3RsLCF9cHNwczJ3fnolZ0JodixqKVQjLWwwJS8rIl1ObScn',2),fuscat1.getSetting(fuscat7('aEptd1xAZGV3aXVwZWZdP2lHdGtJcnJyYm9zZV13Vyd6bSBzaigjIG8gIyJCZ25J',3)))]
 AbitboostdotcomA=urllib.urlencode(AbitboostdotcomA)
 bitboostdotcomA=fuscat7('O1dzM3lRMkJzf3dqOmoqMS4ydzJVdXZ2bHJ4bmEnXG1ucnN5dEtra3dsZngpZE4wQz9lfGwhgTdwemYweV5tVktkaGduZ3Bqezpmb1RsW1EvOCN0R2NreDE9anIxVlp0',1)
 req=urllib2.Request(bitboostdotcomA, AbitboostdotcomA)
 req.add_header("Content-type", "application/x-www-form-urlencoded")
 bitboostdotcomB=urllib2.urlopen(req).read()
 if bitboostdotcomB.startswith('rtmp://') or bitboostdotcomB.startswith('http://') == True:
  return bitboostdotcomB

 errorCode=re.compile('>(.+?)</').findall(bitboostdotcomB)
 e='Unknown Error'
 if len(errorCode) > 0:
  e = errorCode[0]
 #dialogue.doOK('TVCatchup', ['', 'Playback Link Error', e])
 xbmc.log('[script.tvcatchup] - Playback Link failed. ' + e)
 return None

def ConvertToTVCChannels(ordemoC):
 xbmc.log('[script.tvcatchup] Converting XMLTV ident to TVC ident')
 AbitboostdotcomA=[(fuscat7('Kikldi1aXWovK08xZnZ5Yw==',2),fuscat1.getSetting(fuscat7('JyFxdjFnaHt4bnl2bXJSUmpsIyRvSyMoI3BwY2hLOnc=',1))),(fuscat7('ZSkjdEwwI3tkYG5nK3YiQA==',4),fuscat1.getSetting(fuscat7('b2pkeYAsaWiGfnAwenV3SFApdXUtVy9pLys1aDZwJ3U=',2))),(fuscat7('QClgeC1hWHMvK0xUaWdqZQ==',2),fuscat7('O2l1Z0pDaH5yVCtnf3EieQ==',4)),(fuscat7('QXdUa3lXVWYvcCUsWWR1LQ==',2),ordemoC)]
 AbitboostdotcomA=urllib.urlencode(AbitboostdotcomA)
 bitboostdotcomA=fuscat7('UkNxdzwmTnmCOkVvN2l3aT1sUmt6ZCRmf3o9K2twdFtFfE93fz5TaoVwWkp2dnlacDdiZnxxImo9bjlHSGp6SzxZd248Ol00eFRFeGd2SChiNzVndVc4an97Pidlb39IeClmIy1tUiUvK1ZsTSEnag==',2)
 req=urllib2.Request(bitboostdotcomA, AbitboostdotcomA)
 req.add_header("Content-type", "application/x-www-form-urlencoded")
 ordemoCd = urllib2.urlopen(req).read()
 return ordemoCd

def GetEmptyChannelTitle(ordemoC):
 title = GetChannelTitle(ordemoC)
 if title == "Unknown":
  return 'Sorry no EPG Data is available for this channel'
 return title

def GetChannelTitle(ordemoC):
 if ordemoC == '1'  : return 'BBC One'
 if ordemoC == '2'  : return 'BBC Two'
 if ordemoC == '3'  : return 'ITV1'
 if ordemoC == '83' : return 'ITV1 HD'
 if ordemoC == '4'  : return 'Channel 4'
 if ordemoC == '5'  : return 'Channel 5'
 if ordemoC == '64' : return 'ITV1+1'
 if ordemoC == '20' : return 'Channel 4 +1'
 if ordemoC == '75' : return 'Channel 5 + 1'
 if ordemoC == '12' : return 'BBC Three'
 if ordemoC == '13' : return 'BBC Four'
 if ordemoC == '6'  : return 'ITV2' 
 if ordemoC == '23' : return 'ITV2 +1'
 if ordemoC == '9'  : return 'ITV3'
 if ordemoC == '28' : return 'ITV3 +1'
 if ordemoC == '10' : return 'ITV4'
 if ordemoC == '29' : return 'ITV4 +1'
 if ordemoC == '8'  : return 'E4'
 if ordemoC == '21' : return 'E4 +1'
 if ordemoC == '11' : return 'More 4'
 if ordemoC == '27' : return 'More4 +1'
 if ordemoC == '16' : return 'Film 4'
 if ordemoC == '30' : return 'Film4 +1'
 if ordemoC == '106': return '4seven'
 if ordemoC == '14' : return 'Dave'
 if ordemoC == '7'  : return '5USA'
 if ordemoC == '77' : return '5USA + 1'
 if ordemoC == '15' : return '5*'
 if ordemoC == '76' : return '5* + 1'
 if ordemoC == '18' : return 'CBBC Channel'
 if ordemoC == '24' : return 'CBeebies'
 if ordemoC == '19' : return 'CITV'
 if ordemoC == '36' : return 'Pick TV'
 if ordemoC == '74' : return 'Challenge'
 if ordemoC == '73' : return 'Quest'
 if ordemoC == '26' : return 'Yesterday'
 if ordemoC == '66' : return 'Really'
 if ordemoC == '65' : return 'Red Button'
 if ordemoC == '17' : return 'BBC News'
 if ordemoC == '31' : return 'BBC Parliament'
 if ordemoC == '34' : return 'Sky News'
 if ordemoC == '50' : return 'Al Jazeera'
 if ordemoC == '25' : return '4Music'
 if ordemoC == '37' : return 'Viva'
 if ordemoC == '58' : return 'Movies4Men'
 if ordemoC == '60' : return 'Movies4Men +1'
 if ordemoC == '33' : return 'QVC'
 if ordemoC == '84' : return 'NHK'
 if ordemoC == '39' : return 'Ideal World'
 if ordemoC == '40' : return 'Ideal Extra'
 if ordemoC == '41' : return 'Ideal & More'
 if ordemoC == '42' : return 'Create & Craft'
 if ordemoC == '63' : return 'Vintage TV'
 if ordemoC == '67' : return 'Channel AKA'
 if ordemoC == '68' : return 'Showcase TV'
 if ordemoC == '70' : return 'Greatest Hits'
 if ordemoC == '71' : return 'Clubbing TV'
 if ordemoC == '72' : return 'BritAsia TV'
 if ordemoC == '78' : return 'Russia Today'
 if ordemoC == '94' : return 'Catch My Bet'
 if ordemoC == '93' : return 'Bid TV'
 if ordemoC == '95' : return 'Price-Drop TV'
 if ordemoC == '96' : return 'Speed Auction'
 if ordemoC == '140' : return 'Insportive'
  
 return 'Unknown'

def verifyCredentials():
 cFsgZ1tJI25rIGQiNT5ccw = '1'
 fuscat9=bitboostdotcom7()
 AbitboostdotcomA=[(fuscat7('djQjJGBDIyh1cHZ3b2g3JA==',1),fuscat1.getSetting(fuscat7('JyFxdjFnaHt4bnl2bXJSUmpsIyRvSyMoI3BwY2hLOnc=',1))),(fuscat7('RXYgdFAhI3NkIHYiVUZFWQ==',3),fuscat1.getSetting(fuscat7('b2pkeYAsaWiGfnAwenV3SFApdXUtVy9pLys1aDZwJ3U=',2))),(fuscat7('W1AgZ2EjI25rIGQiTFonWg==',3),cFsgZ1tJI25rIGQiNT5ccw),(fuscat7('THgjfVdIaHN2fmRyXydbLQ==',1),fuscat9),(fuscat7('elhvenl1bHNobnUiUUsiNA==',3),YV5SWko3TFtIa05NWVUiaQ),(fuscat7('RSsjfUY4d3FvbHhzN1tdVA==',1),fuscat1.getSetting(fuscat7('Ilxfem1NcmVsc2d2LGNUclRHIHZKPiNtaCBkIic0JS0=',3)))]
 AbitboostdotcomA=urllib.urlencode(AbitboostdotcomA)
 bitboostdotcomA=fuscat7('O1dzM3lRMkJzf3dqOmoqMS4ydzJVdXZ2bHJ4bmEnXG1ucnN5dEtra3dsZngpZE4wQz9lfGwhgTdwemYweV5tVktkaGduZ3Bqezpmb1RsW1EvOCN0R2NreDE9anIxVlp0',1)
 req=urllib2.Request(bitboostdotcomA, AbitboostdotcomA)
 req.add_header("Content-type", "application/x-www-form-urlencoded")
 bitboostdotcomB=urllib2.urlopen(req).read()
 if bitboostdotcomB.startswith('rtmp://') == True:
  return ''
 else:
  errorCode=re.compile('>(.+?)</').findall(bitboostdotcomB)
  e='Unknown Error'
  if len(errorCode) > 0:
   e = errorCode[0]
  return e

def checkLatestMessage():
 if hasattr(os, 'uname'):
  (sysname, nodename, release, version, machine) = os.uname()
 else:
  (sysname, nodename, release, version, machine, processor) = platform.uname() 
 AbitboostdotcomA=[(fuscat7('eGkjJDIqIyhmeXhoQlwmYQ==',1),fuscat7('Py50cGMjdmVkIHcieGRfZg==',3)),('platform',sysname),('version',YV5SWko3TFtIa05NWVUiaQ)]
 AbitboostdotcomA=urllib.urlencode(AbitboostdotcomA)
 bitboostdotcomA=fuscat7("KGV2Mz55MkJzf3dqRzY5O1lCc3FOcnJrcGxrcSxmYFdyPnl2T0doe3Vwd3dYMF88VFsxc05NZjZ2cGZrSW4xOCNTcDM2LkxYRDpud3g4YD11RnMySFlob2R+dmddc21oUlsjJFtHIygjK3NqLC1naw==",1)
 req=urllib2.Request(bitboostdotcomA, AbitboostdotcomA)
 req.add_header("Content-type", "application/x-www-form-urlencoded")
 ordemoCd = urllib2.urlopen(req).read()
 return ordemoCd

def getLatestMessage():
 if hasattr(os, 'uname'):
  (sysname, nodename, release, version, machine) = os.uname()
 else:
  (sysname, nodename, release, version, machine, processor) = platform.uname() 
 AbitboostdotcomA=[(fuscat7('QClgeC1hWHMvK0xUaWdqZQ==',2),fuscat7('PyxqcSdhZHtoano8cHYiYQ==',4)),('platform',sysname),('version',YV5SWko3TFtIa05NWVUiaQ)]
 AbitboostdotcomA=urllib.urlencode(AbitboostdotcomA)
 bitboostdotcomA=fuscat7("OWkvbHVTPXB3L3d1USgwWT5Tb3MjN2Zta21kclt1P2I3MmV5NEh2cndyaHhKRSI/N3NjbTBZMXNmb2gwZS50alMvSXlSV1NBbi8yb2xMX1FLImVpUlpqYXYudnJKS3IrKU4gbDVTIyBzICMiU1wvbg==",3)
 req=urllib2.Request(bitboostdotcomA, AbitboostdotcomA)
 req.add_header("Content-type", "application/x-www-form-urlencoded")
 ordemoCd = urllib2.urlopen(req).readlines()
 return ordemoCd
