#       Copyright (C) 2012 
#       Written on behalf of TVCatchup
#       by Chris Grove (tvc@killergerbils.co.uk)
#       and Sean Poyser (seanpoyser@gmail.com)
#

import xbmc
import xbmcgui
import xbmcaddon
import os
from types import StringType
from types import UnicodeType

KEY_NAV_BACK = 92
KEY_ESC_ID   = 10
KEY_ESC_CODE = 61467
ACTION_BACK  = 92
ACTION_PARENT_DIR = 9
ACTION_PREVIOUS_MENU = 10

ADDON = xbmcaddon.Addon(id = 'script.tvcatchup')

THEME = ADDON.getSetting('skin')

xmlfile = os.path.join(xbmc.translatePath(ADDON.getAddonInfo('path')), 'resources', 'skins',  'Default', '720p', THEME + '-script-tvcatchup-dialog.xml')
if not os.path.exists(xmlfile):
    PREFIX = ""
else:
    PREFIX = THEME + '-'

C_DIALOG_BOX   = 4300
C_DIALOG_TITLE = 4302
C_DIALOG_TEXT  = 4303
C_DIALOG_YES   = 4301
C_DIALOG_NO    = 4304
C_DIALOG_ICON  = 4305
C_DIALOG_OKAY  = 4306

class DialogBoxOk(xbmcgui.WindowXMLDialog):

    def __new__(cls, Prams):
        return super(DialogBoxOk, cls).__new__(cls, PREFIX + 'script-tvcatchup-dialog.xml', ADDON.getAddonInfo('path'))
        
    def __init__(self, Prams):
        super(DialogBoxOk, self).__init__()

        self.Title   = Prams[0]
        self.Icon    = Prams[1]
        self.Button1 = Prams[2]
        self.Message = ""
        for j in range(3,len(Prams)):
            self.Message = self.Message + Prams[j] + "\n"
        
    def onInit(self):
        try:            
            self.getControl(C_DIALOG_NO).setVisible(False)
            self.getControl(C_DIALOG_YES).setVisible(False)

            dialogTitle = self.getControl(C_DIALOG_TITLE)
            dialogTitle.setLabel(self.Title)

            dialogButton1 = self.getControl(C_DIALOG_OKAY)
            dialogButton1.setLabel(self.Button1)

            dialogText = self.getControl(C_DIALOG_TEXT)
            dialogText.setText(self.Message)
                       
            if self.Icon <> None:
                dialogIcon = self.getControl(C_DIALOG_ICON) 
                dialogIcon.setImage(self.Icon) 

            self.setFocus(dialogButton1)    
        except:
            pass
    
    def onAction(self, action):
        try:
            if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK, ACTION_BACK, KEY_ESC_ID]:
                self.close()
                return
        except:
            pass

    def onClick(self, controlId):
        try:            
            self.close()            
        except:
            pass

    def onFocus(self, controlId):
        pass

class DialogBoxYesNo(xbmcgui.WindowXMLDialog):
    
    def __new__(cls, Prams):
        return super(DialogBoxYesNo, cls).__new__(cls, PREFIX + 'script-tvcatchup-dialog.xml', ADDON.getAddonInfo('path'))
        
    def __init__(self, Prams):
        super(DialogBoxYesNo, self).__init__()

        self.buttonClicked = None
        self.Title         = Prams[0]
        self.Icon          = Prams[1]
        self.Button1       = Prams[2]
        self.Button2       = Prams[3]
        self.Message       = ""
        for j in range(4,len(Prams)):
            self.Message = self.Message + Prams[j] + "\n"
        
    def onInit(self):        
        try:  
            self.getControl(C_DIALOG_OKAY).setVisible(False)
          
            dialogTitle = self.getControl(C_DIALOG_TITLE)
            dialogTitle.setLabel(self.Title)

            dialogButton1 = self.getControl(C_DIALOG_YES)
            dialogButton1.setLabel(self.Button1)

            dialogButton2 = self.getControl(C_DIALOG_NO)
            dialogButton2.setLabel(self.Button2)

            dialogText = self.getControl(C_DIALOG_TEXT)
            dialogText.setText(self.Message)
            
            if self.Icon <> None:
                dialogIcon = self.getControl(C_DIALOG_ICON)            
                dialogIcon.setImage(self.Icon)     

            self.setFocus(dialogButton1)        
        except:
            pass


    def onAction(self, action):
        try:
            if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK, ACTION_BACK, KEY_ESC_ID]:
                self.close()
                return
        except:
            pass

    def onClick(self, controlId):
        try:            
            self.buttonClicked = controlId
            self.close()
        except:
            pass

    def onFocus(self, controlId):
        pass

def yesno(Prams):
    dialogbox = DialogBoxYesNo(Prams)
    dialogbox.doModal()
    clickid = dialogbox.buttonClicked
    del dialogbox
    return clickid == C_DIALOG_YES

def ok(Prams):
    dialogbox = DialogBoxOk(Prams)
    dialogbox.doModal()
    del dialogbox

def doYesNo(title, message, yesLabel = 'Yes', noLabel = 'No', icon = None):

    prams = [title, icon, yesLabel, noLabel]

    if type(message) is StringType or type(message) is UnicodeType:
        prams.append(message)
    else:
        for i in range(0,len(message)):
            prams.append(message[i])
    
    dialogbox = DialogBoxYesNo(prams)
    dialogbox.doModal()
    clickid = dialogbox.buttonClicked
    del dialogbox    
    return clickid == C_DIALOG_YES

def doOK(title, message, okLabel = 'Okay', icon = None):

    prams = [title, icon, okLabel]

    if type(message) is StringType or type(message) is UnicodeType:
        prams.append(message)
    else:
        for i in range(0,len(message)):
            prams.append(message[i])

    dialogbox = DialogBoxOk(prams)
    dialogbox.doModal()
    del dialogbox    
