oo000 = [ 'urllib' , 'urllib2' , 're' , 'os' , 'sys' , 'xbmcplugin' , 'xbmcgui' , 'xbmc' , 'TVClibs' , 'xbmcaddon' ]
ii = map ( __import__ , oo000 )
ii
if 51 - 51: IiI1i11I
__scriptname__ = "plugin.video.tvcatchup"
__author__ = 'dj_gerbil [tvc@killergerbils.co.uk]'
__svn_url__ = "http://tvcatchup-xbmc-addon.googlecode.com/svn/trunk/ tvcatchup-xbmc-addon-read-only"
__version__ = "1.4.4"
__phpurl__ = ii [ 8 ] . Ii ( "WVQvbHNDPXB3L3dyOUtJXVg1c3ApNHFpeC5qdj9fcTtUZmh6UFFmdGZ1ZHJrQFksS0h+Mld4Mm1meHJkOVtvXTgwbXFVZWV4ZmMyMGtVRWg+ZSB0a10jIGsgcyJMbSlSMg==" , 3 )
__cachefolder__ = "addon_data"
__settings__ = ii [ 9 ] . Addon ( id = 'plugin.video.tvcatchup' )
__addon__ = ii [ 9 ].Addon('plugin.video.tvcatchup')

SETTINGS = {
 'cache.path' : ii[7].translatePath(__addon__.getAddonInfo('profile'))
 }

if 16 - 16: iI11I1II1I1I + iiiii % ii1I - II1 - O0ooooo00oOO - ooOoO
def o0Oo ( ) : 
 if not ii[3].path.exists(SETTINGS['cache.path']):
  ii[3].makedirs(SETTINGS['cache.path'])
## i1IiI1I11 = ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "T:" + ii [ 3 ] . sep , __cachefolder__ ) )
## IIiIiII11i = i1IiI1I11 + ii [ 3 ] . sep + __scriptname__
## if not ii [ 3 ] . path . isdir ( IIiIiII11i ) :
##  try :
##   print "%s doesn't exist, creating" % IIiIiII11i
##   ii [ 3 ] . makedirs ( IIiIiII11i )
##  except IOError , o0oOOo0O0Ooo :
##   print "Couldn't create %s, %s" % ( IIiIiII11i , str ( o0oOOo0O0Ooo ) )
##   raise
## IIiIiII11i = i1IiI1I11 + ii [ 3 ] . sep + __scriptname__ + ii [ 3 ] . sep + 'TVC_cache'
## if not ii [ 3 ] . path . isdir ( IIiIiII11i ) :
##  try :
##   print "%s doesn't exist, creating" % IIiIiII11i
##   ii [ 3 ] . makedirs ( IIiIiII11i )
##  except IOError , o0oOOo0O0Ooo :
##   print "Couldn't create %s, %s" % ( IIiIiII11i , str ( o0oOOo0O0Ooo ) )
##   raise
## i1IiI1I11 = ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "T:" + ii [ 3 ] . sep , __cachefolder__ , __scriptname__ ) )
## I1ii11iIi11i = ii [ 3 ] . path . join ( i1IiI1I11 , 'TVC_cache' )
 I1IiI = __settings__ . getSetting ( 'uname' )
 o0OOO = __settings__ . getSetting ( 'pwd' )
 if o0OOO . find ( '.enc.' ) < 0 :
  str_list = []
  str_list.append(__phpurl__)
  str_list.append(ii [ 8 ] . Ii ( "bXFjQzRNcHJzb2hmTF8/OGBNbmkuVWRyQHRqZ20tS19MKmNoXnVxdSk9aWcoXE8ydlAmcnlCaGRmcHJjQk1laGpjIHcqYSMgdiBAInJeeU1A" , 3 ))
  str_list.append(o0OOO)
  iIiiiI = ii [ 1 ] . urlopen ("".join(str_list))
  Iii1ii1II11i = iIiiiI . read ( )
  __settings__ . setSetting ( 'pwd' , Iii1ii1II11i + '.enc.' )
 iI111iI = __settings__ . getSetting ( 'whatson' )
 if ( not I1IiI or I1IiI == '' ) or ( not o0OOO or o0OOO == '' ) :
  IIiIiII11i = ii [ 6 ] . Dialog ( )
  IIiIiII11i . ok ( 'Welcome to the TVCatchup plugin.' , 'To start using this plugin first go to www.TVCatchup.com' , 'and create a (free) account.' )
  __settings__ . openSettings ( )
  if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . I1i1iI1i - II
def Oo ( ) :
 I1IiI = __settings__ . getSetting ( 'uname' )
 o0OOO = __settings__ . getSetting ( 'pwd' )
 if o0OOO . find ( '.enc.' ) > 0 :
  I1Ii11I1Ii1i = __settings__ . getSetting ( 'pwd' )
  o0OOO = I1Ii11I1Ii1i . rstrip ( '.enc.' )
 else:
  str_list = []
  str_list.append(__phpurl__)
  str_list.append(ii [ 8 ] . Ii ( "bXFjQzRNcHJzb2hmTF8/OGBNbmkuVWRyQHRqZ20tS19MKmNoXnVxdSk9aWcoXE8ydlAmcnlCaGRmcHJjQk1laGpjIHcqYSMgdiBAInJeeU1A" , 3 ))
  str_list.append(o0OOO)
  iIiiiI = ii [ 1 ] . urlopen ("".join(str_list))
  Iii1ii1II11i = iIiiiI . read ( )
  __settings__ . setSetting ( 'pwd' , Iii1ii1II11i + '.enc.' )
  I1Ii11I1Ii1i = __settings__ . getSetting ( 'pwd' )
  o0OOO = I1Ii11I1Ii1i . rstrip ( '.enc.' )
 str_list = []
 str_list.append(__phpurl__)
 str_list.append(ii [ 8 ] . Ii ( 'd2pjQzwycHJzb2hmQ3hXUD9cbmk1ZWRyQHRqZzxjOFV2SGNoKnlxdSk9aWMxQ2gzaChzeVcoeCZ3ZWt0LnFRbkY8IEFANiMgIyAjIlt2dEtk' , 3 ))
 str_list.append(I1IiI)
 str_list.append("&pass=")                   
 str_list.append(o0OOO)
 iIiiiI = ii [ 1 ] . urlopen ("".join(str_list))
 Iii1ii1II11i = iIiiiI . read ( )
 Ooo = ii [ 2 ] . compile ( 'authKey] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 if len ( Ooo ) <= 0 :
  o0oOoO00o = ii [ 2 ] . compile ( ' #FFFFFF">(.+?)</div>' ) . findall ( Iii1ii1II11i )
  IIiIiII11i = ii [ 6 ] . Dialog ( )
  IIiIiII11i . ok ( 'TVCatchup Plugin Error.' , o0oOoO00o [ 0 ] , 'Please check your settings.' )
 else :
  return Ooo [ 0 ]
  if 43 - 43: O0OOo . II1Iiii1111i
def i1IIi11111i ( authkey , name ) :
 QqQ = __settings__ . getSetting ( 'video_stream' )
 if QqQ == "3":
  QqQq = "0"
 elif QqQ == "2":
  QqQq = "1"
 elif QqQ == "1":
  QqQq = "2"
 elif QqQ == "0":
  QqQq = "3"
 str_list = []
 str_list.append(__phpurl__)
 str_list.append(ii [ 8 ] . Ii ( 'ZUJjQz4scHJzb2hmaEJQS2Jnbmk6WmRyQHRqZ0MyNUpNOWNoTk5xdSk9aWVpbnczSmZubClfbGxka3EiO2lCWlY=' , 3 ))
 str_list.append(authkey)
 str_list.append("&quality=")
 str_list.append(QqQq)
 iIiiiI = ii [ 1 ] . urlopen ("".join(str_list))
 Iii1ii1II11i = iIiiiI . read ( )
 chanident = ii [ 2 ] . compile ( 'ident] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 o000o0o00o0Oo = ii [ 2 ] . compile ( 'PlayLink] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 IiII1I1i1i1ii = ii [ 2 ] . compile ( 'title] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 IiII1I1i1i1iis = ii [ 2 ] . compile ( 'start] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 IiII1I1i1i1iie = ii [ 2 ] . compile ( 'end] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 IiII1I1i1i1iid = ii [ 2 ] . compile ( 'duration] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 IiII1I1i1i1iig = ii [ 2 ] . compile ( 'genres] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 IiII1I1i1i1iip = ii [ 2 ] . compile ( 'description] => (.+?)\n' ) . findall ( Iii1ii1II11i )
 if len ( o000o0o00o0Oo ) <= 0 :
  o0oOoO00o = ii [ 2 ] . compile ( ' #FFFFFF">(.+?)</div>' ) . findall ( Iii1ii1II11i )
  IIiIiII11i = ii [ 6 ] . Dialog ( )
  IIiIiII11i . ok ( 'TVCatchup Plugin Error.' , o0oOoO00o [ 0 ] , 'Please contact DJ_Gerbil or TVC Support for advice.' )
 else :
  iiiI11 = ii [ 6 ] . ListItem ( IiII1I1i1i1ii [ 0 ] )
  iiiI11 . setIconImage ( 'defaultVideo.png' )
  str_list = []
  str_list.append("T:")
  str_list.append(ii [ 3 ] . sep)
  i1IiI1I11 = SETTINGS['cache.path'] #ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "".join(str_list) , __cachefolder__ , __scriptname__ ) )
  OOooO = ii [ 3 ] . path . join ( i1IiI1I11 , chanident[0] + "enabled.png" )
  iiiI11 . setThumbnailImage ( OOooO )
  ii [ 7 ] . executebuiltin ( "xbmc.Notification('Now Playing...'," + IiII1I1i1i1ii[0] + " , 10000, %s)" % ( ii [ 3 ] . path . join (i1IiI1I11 , 'TVC_cache' , chanident[0] + "enabled.png" ) , ) )
  #ii [ 7 ] . Player ( ii [ 7 ] . PLAYER_CORE_DVDPLAYER ) . play ( o000o0o00o0Oo[0] , iiiI11 )
  ii [ 7 ] . Player (  ) . play ( o000o0o00o0Oo[0] , iiiI11 )
  if 58 - 58: i11iiII + OooooO0oOO + oOo0 / oo0Ooo0
def I1I11I1I1I ( ) :
 Ooo = Oo ( )
 #i1IiI1I11 = ii [ 7 ] . translatePath ( ii [ 3 ] . path . join ( "T:" + ii [ 3 ] . sep , __cachefolder__ , __scriptname__ ) )
 I1ii11iIi11i = SETTINGS['cache.path']#ii [ 3 ] . path . join ( i1IiI1I11 , 'TVC_cache' )
 iI111iI = __settings__ . getSetting ( 'whatson' )
 iIiiiI = ii [ 1 ] . urlopen ( __phpurl__ + "?permcode=granted&func=channels" )
 OooO0OO = iIiiiI . read ( )
 iiiIi = ii [ 2 ] . compile ( 'channel_id] -> (.+?)<br />' ) . findall ( OooO0OO )
 IiIIIiI1I1 = ii [ 2 ] . compile ( 'channel_name] -> (.+?)<br />' ) . findall ( OooO0OO )
 OoO000 = ii [ 2 ] . compile ( 'channel_status] -> (.+?)<br />' ) . findall ( OooO0OO )
 IIiiIiI1 = ii [ 2 ] . compile ( 'channel_logo] -> (.+?)<br />' ) . findall ( OooO0OO )
 iiiI11 = ii [ 2 ] . compile ( 'now_programme_name] -> (.+?)<br />' ) . findall ( OooO0OO )
 iiIiIIi = ii [ 2 ] . compile ( 'now_programme_start] -> (.+?)<br />' ) . findall ( OooO0OO )
 ooOoo0O = ii [ 2 ] . compile ( 'now_programme_end] -> (.+?)<br />' ) . findall ( OooO0OO )
 ooOoo0Opd = ii [ 2 ] . compile ( 'now_programme_duration] -> (.+?)<br />' ) . findall ( OooO0OO )
 ooOoo0Opg = ii [ 2 ] . compile ( 'now_programme_genres] -> (.+?)<br />' ) . findall ( OooO0OO )
 ooOoo0Opdes = ii [ 2 ] . compile ( 'description] -> (.+?)<br />' ) . findall ( OooO0OO )
 iiiI11n = ii [ 2 ] . compile ( 'next_programme_name] -> (.+?)<br />' ) . findall ( OooO0OO )
 iiIiIIin = ii [ 2 ] . compile ( 'next_programme_start] -> (.+?)<br />' ) . findall ( OooO0OO )
 ooOoo0On = ii [ 2 ] . compile ( 'next_programme_end] -> (.+?)<br />' ) . findall ( OooO0OO )
 OooO0 = 0
 for II11iiii1Ii in range ( 0 , len ( iiiIi ) ) :
  jamie = __settings__ . getSetting ( IiIIIiI1I1[II11iiii1Ii].replace(" ","_") )
  if (jamie == "true"):
   if OoO000 [ II11iiii1Ii ] == "enabled" :
    if not ii [ 3 ] . path . exists ( I1ii11iIi11i + ii [ 3 ] . sep + iiiIi [ II11iiii1Ii ] + "enabled.png" ) :
     iIiiiI = ii [ 1 ] . urlopen ( IIiiIiI1 [ II11iiii1Ii ] )
     Iii1ii1II11i = iIiiiI . read ( )
     file = open ( I1ii11iIi11i + ii [ 3 ] . sep + iiiIi [ II11iiii1Ii ] + "enabled.png" , mode = "wb" )
     file . write ( Iii1ii1II11i )
     file . close ( )
    if iI111iI == "true" :
     str_list = []
     #str_list.append(str ( II11iiii1Ii + 1 ))
     #str_list.append(": ")
     #str_list.append(IiIIIiI1I1 [ II11iiii1Ii ]) #Channel name
     str_list.append(iiIiIIi [ OooO0 ] [ 11 : 16 ]) #current start
     str_list.append(" - ")
     str_list.append(iiiI11 [ OooO0 ])
     #str_list.append(" - From: ")
     #str_list.append(" - To: ")
     #str_list.append(ooOoo0O [ OooO0 ] [ 11 : 16 ]) #next start
     #str_list.append(" - Next: ")
     #str_list.append(iiiI11n [ OooO0 ])
     str_list2 = []
     str_list2.append('&auth=')
     str_list2.append(Ooo)
     str_list2.append('&chan=')
     str_list2.append(iiiIi [ II11iiii1Ii ])
     str_list3 = []
     str_list3.append(I1ii11iIi11i) #channel logo
     str_list3.append(ii [ 3 ] . sep)
     str_list3.append(iiiIi [ II11iiii1Ii ])
     str_list3.append("enabled.png")
     str_list4 = []
     str_list4.append(ooOoo0O [ OooO0 ] [ 11 : 16 ])
     str_list4.append(" - ")
     #str_list4.append(iiiI11 [ II11iiii1Ii ])
     #str_list4.append(". Up Next: ")
     str_list4.append(iiiI11n [ II11iiii1Ii ])
     #str_list4.append(".")
     OO0o ( "".join(str_list), "".join(str_list2) , 3 , "".join(str_list3) , ooOoo0Opd [ II11iiii1Ii ] , IiIIIiI1I1 [ II11iiii1Ii ] , ooOoo0Opdes [ II11iiii1Ii ] , "".join(str_list4) , len ( iiiIi )  )
     OooO0 = OooO0 + 1
    else :
     str_list = []
     str_list.append(str ( II11iiii1Ii + 1 ))
     str_list.append(": ")
     str_list.append(IiIIIiI1I1 [ II11iiii1Ii ])
     str_list2 = []
     str_list2.append('&auth=')
     str_list2.append(Ooo)
     str_list2.append('&chan=')
     str_list2.append(iiiIi [ II11iiii1Ii ])
     str_list3 = []
     str_list3.append(I1ii11iIi11i)
     str_list3.append(ii [ 3 ] . sep)
     str_list3.append(iiiIi [ II11iiii1Ii ])
     str_list3.append("enabled.png")
     OO0o ( "".join(str_list) , "".join(str_list2) , 3 , "".join(str_list3) , ooOoo0Opd [ II11iiii1Ii ] , ooOoo0Opg [ II11iiii1Ii ] , ooOoo0Opdes [ II11iiii1Ii ] , iiiI11 [ II11iiii1Ii ] , len ( iiiIi ) )
   else :
    if not ii [ 3 ] . path . exists ( I1ii11iIi11i + ii [ 3 ] . sep + iiiIi [ II11iiii1Ii ] + "disabled.png" ) :
     iIiiiI = ii [ 1 ] . urlopen ( IIiiIiI1 [ II11iiii1Ii ] )
     Iii1ii1II11i = iIiiiI . read ( )
     file = open ( I1ii11iIi11i + ii [ 3 ] . sep + iiiIi [ II11iiii1Ii ] + "disabled.png" , mode = "wb" )
     file . write ( Iii1ii1II11i )
     file . close ( )
    str_list = []
    str_list.append(str ( II11iiii1Ii + 1 ))
    str_list.append(": ")
    str_list.append(IiIIIiI1I1 [ II11iiii1Ii ])
    str_list.append(" - Channel Is Currently Offline")
    str_list2 = []
    str_list2.append('&auth=')
    str_list2.append(Ooo)
    str_list2.append('&chan=')
    str_list2.append(iiiIi [ II11iiii1Ii ])
    str_list3 = []
    str_list3.append(I1ii11iIi11i)
    str_list3.append(ii [ 3 ] . sep)
    str_list3.append(iiiIi [ II11iiii1Ii ])
    str_list3.append("disabled.png")
    OO0o ( "".join(str_list) , "".join(str_list2) , 3 , "".join(str_list3) , ooOoo0Opd [ II11iiii1Ii ] , ooOoo0Opg [ II11iiii1Ii ] , "Offline" , iiiI11 [ II11iiii1Ii ] , len ( iiiIi ) )
    OooO0 = OooO0 + 1
  else:
   OooO0 = OooO0 + 1
 ii [ 5 ] . endOfDirectory ( int(ii[4].argv[1]), cacheToDisc=False )
 if 82 - 82: i1I1i1Ii11 . iiiii - i11iiII * O00oOoOoO0o0O + Oo0ooO0oo0oO + ooOoO
def O0O ( ) :
 O00o0OO = [ ]
 I11i1 = ii [ 4 ] . argv [ 2 ]
 if len ( I11i1 ) >= 2 :
  iIi1ii1I1 = ii [ 4 ] . argv [ 2 ]
  o0 = iIi1ii1I1 . replace ( '?' , '' )
  if ( iIi1ii1I1 [ len ( iIi1ii1I1 ) - 1 ] == '/' ) :
   iIi1ii1I1 = iIi1ii1I1 [ 0 : len ( iIi1ii1I1 ) - 2 ]
  I11II1i = o0 . split ( '&' )
  O00o0OO = { }
  for IIIIIooooooO0oo in range ( len ( I11II1i ) ) :
   IIiiiiiiIi1I1 = { }
   IIiiiiiiIi1I1 = I11II1i [ IIIIIooooooO0oo ] . split ( '=' )
   if ( len ( IIiiiiiiIi1I1 ) ) == 2 :
    O00o0OO [ IIiiiiiiIi1I1 [ 0 ] ] = IIiiiiiiIi1I1 [ 1 ]
 return O00o0OO
 if 13 - 13: oOo0 + O0oo0OO0 - ii1I + oo0Ooo0 . OooooO0oOO + O00oOoOoO0o0O
def OO0o ( name , url , mode , iconimage , duration , genre , description , realname , total ) :
 str_list = []
 str_list.append(ii [ 4 ] . argv [ 0 ])
 str_list.append("?url=")
 str_list.append(ii [ 0 ] . quote_plus ( url ))
 str_list.append("&mode=")
 str_list.append(str ( mode ))
 str_list.append("&name=")
 str_list.append(ii [ 0 ] . quote_plus ( name ))
 Ii = "".join(str_list)
 oo0O0oOOO00oO = True
 OooOooooOOoo0 = ii [ 6 ] . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI111iI = __settings__ . getSetting ( 'realname' )
 if (iI111iI<>"true"):
  OooOooooOOoo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name,'genre': genre ,'duration': str(duration) , 'plot': description , 'plotoutline': description} )
 else: #LINE BELOW IS HACKED TO BUGGERY
  OooOooooOOoo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name, 'genre': realname, 'duration': str(duration), 'director': genre} )
 oo0O0oOOO00oO = ii [ 5 ] . addDirectoryItem ( handle = int(ii[4].argv[1]) , url = Ii , listitem = OooOooooOOoo0 , isFolder = False , totalItems = total )
 return oo0O0oOOO00oO
 if 71 - 71: oo0Ooo0 % II % O0OOo
def oO00ooo0 ( ) :
 iIi1ii1I1 = O0O ( )
 o00 = o0Oo ( )
 OooOooo = None
 O000oo0O = None
 OOOO = None
 if 10 - 10: O0OOo / ooOoO * O0OOo
 try :
  OooOooo = ii [ 0 ] . unquote_plus ( iIi1ii1I1 [ "url" ] )
 except :
  pass
 try :
  O000oo0O = ii [ 0 ] . unquote_plus ( iIi1ii1I1 [ "name" ] )
 except :
  pass
 try :
  OOOO = int ( iIi1ii1I1 [ "mode" ] )
 except :
  pass
  if 29 - 29: I1i1iI1i % ooOoO + i1I1i1Ii11 / Oo0ooO0oo0oO + O0OOo * Oo0ooO0oo0oO
 if OOOO == None or OooOooo == None or len ( OooOooo ) < 1 :
  I1I11I1I1I ( )
 elif OOOO == 1 :
  I1I11I1I1I ( )
 elif OOOO == 3 :
  i1IIi11111i ( OooOooo , O000oo0O )
  if 42 - 42: i11iiII + II
