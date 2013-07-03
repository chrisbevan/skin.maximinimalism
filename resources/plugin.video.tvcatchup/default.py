moduleNames= ['urllib2','os','sys','xbmcgui','xbmc','xbmcaddon','zipfile','re']
modules = map(__import__, moduleNames)
modules

__settings__ = modules [ 5 ] . Addon ( id = 'plugin.video.tvcatchup' )
__addon__ = modules [ 5 ].Addon('plugin.video.tvcatchup')

modules[2].path.insert(0, modules[1].path.join(__addon__.getAddonInfo('path'), 'lib'))
modules[2].path.insert(0, modules[1].path.join(__addon__.getAddonInfo('path'), 'resources'))

tmp_lib=__import__('TVClibs')
TVC=__import__('TVC')
dialogue=__import__('dialogue')

__scriptname__ = "plugin.video.tvcatchup"
__author__     = 'dj_gerbil [tvc@killergerbils.co.uk]'
__svn_url__    = ""
__version__    = "1.4.4"
__phpurl__ = tmp_lib.Ii( "WVQvbHNDPXB3L3dyOUtJXVg1c3ApNHFpeC5qdj9fcTtUZmh6UFFmdGZ1ZHJrQFksS0h+Mld4Mm1meHJkOVtvXTgwbXFVZWV4ZmMyMGtVRWg+ZSB0a10jIGsgcyJMbSlSMg==" , 3 )    

iIiiiI = modules[0].urlopen( __phpurl__ + "?func=chansavailable")
chansavailable = iIiiiI.readlines()
settingsfile = open(__addon__.getAddonInfo('path')+'/resources/settings.xml',mode="rb")
settingsfile2 = open(__addon__.getAddonInfo('path')+'/resources/language/English/strings.xml',mode="rb")
lines = settingsfile.readlines()
lines2 = settingsfile2.readlines()
settingsfile.close()
settingsfile2.close()
differences = False
for bob2 in range(0,len(chansavailable)):
  lineexists = False
  for bob in range(1,len(lines)-1):
    if (lines[bob].find(chansavailable[bob2].replace(" ","_").replace("\n",""))<>-1):
      lineexists = True
  if (lineexists <> True):
    differences = True
if (differences <> False):
  settingsfile = open(__addon__.getAddonInfo('path')+'/resources/settings.xml',mode="wb")
  settingsfile2 = open(__addon__.getAddonInfo('path')+'/resources/language/English/strings.xml',mode="wb")
  settingsfile.write(lines[0])
  settingsfile2.write(lines2[0])
  for bob in range(1,len(lines)-1):
    settingsfile.write(lines[bob])
    settingsfile2.write(lines2[bob])
  for bob2 in range(0,len(chansavailable)):
    lineexists = False
    for bob in range(1,len(lines)-1):
      if (lines[bob].find(chansavailable[bob2].replace(" ","_").replace("\n",""))<>-1):
        lineexists = True
    if (lineexists <> True):
      settingsfile.write('\t<setting id="'+chansavailable[bob2].replace(" ","_").replace("\n","")+'" label="'+str(3000+len(lines)-2+bob2)+'" type="bool" default="true" />'+"\n")
      settingsfile2.write('\t<string id="'+str(3000+len(lines)-2+bob2)+'">'+chansavailable[bob2].replace("\n","")+'</string>'+"\n")
  settingsfile.write(lines[len(lines)-1])
  settingsfile2.write(lines2[len(lines2)-1])
  settingsfile.close()
  settingsfile2.close()

tmp_lib2=__import__('TVClibs2',globals())

messageID = TVC.checkLatestMessage()
if int(__addon__.getSetting('MessageID')) < int(messageID):
  messageText = TVC.getLatestMessage()
  messageTitle = messageText[0]
  messageText[0] = ""
  for j in range(0,len(messageText)-1):
      messageText[j] = messageText[j].replace("\r","").replace("\n","")
  dialogue.doOK(messageTitle,messageText)
  __addon__.setSetting('MessageID', messageID)

tmp_lib2.oO00ooo0()

