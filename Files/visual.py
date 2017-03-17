#Boa:Frame:final_Frame

import wx
import helper

def create(parent):
    return final_Frame(parent)

[wxID_FINAL_FRAME, wxID_FINAL_FRAMECLASSNUMBER_STATICTEXT, 
 wxID_FINAL_FRAMECLASSNUMBER_TEXTCTRL, wxID_FINAL_FRAMEGENERALCLASS_LISTBOX, 
 wxID_FINAL_FRAMEGO_BUTTON, wxID_FINAL_FRAMELOGON_BUTTON, 
 wxID_FINAL_FRAMELOGON_PANEL, wxID_FINAL_FRAMEPASSWORD_STATICTEXT, 
 wxID_FINAL_FRAMEPASSWORD_TEXTCTRL, wxID_FINAL_FRAMEQUARTER_LISTBOX, 
 wxID_FINAL_FRAMESELECT_BUTTON, wxID_FINAL_FRAMESPECIFICCLASS_LISTBOX, 
 wxID_FINAL_FRAMESTATUS_TEXTCTRL, wxID_FINAL_FRAMEUSERNAME_STATICTEXT, 
 wxID_FINAL_FRAMEUSERNAME_TEXTCTRL, 
] = [wx.NewId() for _init_ctrls in range(15)]

class final_Frame(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FINAL_FRAME, name=u'final_Frame',
              parent=prnt, pos=wx.Point(487, 251), size=wx.Size(1273, 653),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Sniper - v .03-2')
        self.SetClientSize(wx.Size(1273, 653))

        self.logon_Panel = wx.Panel(id=wxID_FINAL_FRAMELOGON_PANEL,
              name=u'logon_Panel', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1273, 653), style=wx.TAB_TRAVERSAL)

        self.username_StaticText = wx.StaticText(id=wxID_FINAL_FRAMEUSERNAME_STATICTEXT,
              label=u'Username:', name=u'username_StaticText',
              parent=self.logon_Panel, pos=wx.Point(20, 30), size=wx.Size(72,
              15), style=0)

        self.password_StaticText = wx.StaticText(id=wxID_FINAL_FRAMEPASSWORD_STATICTEXT,
              label=u'Password:', name=u'password_StaticText',
              parent=self.logon_Panel, pos=wx.Point(20, 70), size=wx.Size(69,
              15), style=0)

        self.username_TextCtrl = wx.TextCtrl(id=wxID_FINAL_FRAMEUSERNAME_TEXTCTRL,
              name=u'username_TextCtrl', parent=self.logon_Panel,
              pos=wx.Point(120, 30), size=wx.Size(80, 21), style=0, value=u'')

        self.password_TextCtrl = wx.TextCtrl(id=wxID_FINAL_FRAMEPASSWORD_TEXTCTRL,
              name=u'password_TextCtrl', parent=self.logon_Panel,
              pos=wx.Point(120, 70), size=wx.Size(80, 21), style=0, value=u'')

        self.logon_Button = wx.Button(id=wxID_FINAL_FRAMELOGON_BUTTON,
              label=u'Log In', name=u'logon_Button', parent=self.logon_Panel,
              pos=wx.Point(60, 120), size=wx.Size(85, 30), style=0)
        self.logon_Button.Bind(wx.EVT_BUTTON, self.OnLogon_ButtonButton,
              id=wxID_FINAL_FRAMELOGON_BUTTON)

        self.status_TextCtrl = wx.TextCtrl(id=wxID_FINAL_FRAMESTATUS_TEXTCTRL,
              name=u'status_TextCtrl', parent=self.logon_Panel, pos=wx.Point(30,
              600), size=wx.Size(600, 21), style=0, value=u'Status:')

        self.quarter_ListBox = wx.ListBox(choices=[],
              id=wxID_FINAL_FRAMEQUARTER_LISTBOX, name=u'quarter_ListBox',
              parent=self.logon_Panel, pos=wx.Point(20, 163), size=wx.Size(220,
              80), style=0)

        self.generalclass_ListBox = wx.ListBox(choices=[],
              id=wxID_FINAL_FRAMEGENERALCLASS_LISTBOX,
              name=u'generalclass_ListBox', parent=self.logon_Panel,
              pos=wx.Point(20, 250), size=wx.Size(220, 240), style=0)

        self.classnumber_StaticText = wx.StaticText(id=wxID_FINAL_FRAMECLASSNUMBER_STATICTEXT,
              label=u'Class Number:', name=u'classnumber_StaticText',
              parent=self.logon_Panel, pos=wx.Point(20, 511), size=wx.Size(95,
              15), style=0)

        self.classnumber_TextCtrl = wx.TextCtrl(id=wxID_FINAL_FRAMECLASSNUMBER_TEXTCTRL,
              name=u'classnumber_TextCtrl', parent=self.logon_Panel,
              pos=wx.Point(130, 510), size=wx.Size(100, 21), style=0,
              value=u'')

        self.go_Button = wx.Button(id=wxID_FINAL_FRAMEGO_BUTTON, label=u'GO',
              name=u'go_Button', parent=self.logon_Panel, pos=wx.Point(60, 540),
              size=wx.Size(85, 30), style=0)
        self.go_Button.Bind(wx.EVT_BUTTON, self.OnGo_ButtonButton,
              id=wxID_FINAL_FRAMEGO_BUTTON)

        self.specificclass_ListBox = wx.ListBox(choices=[],
              id=wxID_FINAL_FRAMESPECIFICCLASS_LISTBOX,
              name=u'specificclass_ListBox', parent=self.logon_Panel,
              pos=wx.Point(256, 16), size=wx.Size(320, 136), style=0)

        self.select_Button = wx.Button(id=wxID_FINAL_FRAMESELECT_BUTTON,
              label=u'Select', name=u'select_Button', parent=self.logon_Panel,
              pos=wx.Point(377, 172), size=wx.Size(85, 30), style=0)
        self.select_Button.Bind(wx.EVT_BUTTON, self.OnSelect_ButtonButton,
              id=wxID_FINAL_FRAMESELECT_BUTTON)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGoButton(self, event):
        #self.password_TextCtrl.Value = self.username_TextCtrl.Value
        self.logon_Panel.Destroy()
        self.Refresh()
        #event.Skip()

    def OnLogon_ButtonButton(self, event):
        ''' Logs on, creates quarter list and subject area list '''
        
        self.status_TextCtrl.Value = 'loading...'
        
        self.Refresh()
        
        username = self.username_TextCtrl.Value
        password = self.password_TextCtrl.Value
        
        schedule.logon(username, password)
        quarter_list, subject_area_list = schedule.get_list_of_courses()
        
        self.quarter_ListBox.Set(quarter_list)
        self.generalclass_ListBox.Set(subject_area_list)
        

        
        
        self.Refresh()
        #event.Skip()

    def OnGo_ButtonButton(self, event):
        
        quarter = self.quarter_ListBox.GetStringSelection()
        subject_area = self.generalclass_ListBox.GetStringSelection()
        class_number = self.classnumber_TextCtrl.Value
        
        schedule.set_list_of_courses(quarter, subject_area, class_number)
        
        specific_classes = schedule.get_specific_class()

        self.specificclass_ListBox.Set(specific_classes)
        self.Refresh()
        #print quarter
        event.Skip()

    def OnSelect_ButtonButton(self, event):
        
        self.status_TextCtrl.Value = 'settings saved!'
        specific_class = self.specificclass_ListBox.GetSelection()
        
        schedule.save_data(specific_class)
        
        
        self.Refresh()
        event.Skip()


if __name__ == '__main__':
    
    schedule = helper.Info()
    quarter_list=[]
    subject_area_list=[]
    
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
