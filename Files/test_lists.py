

import wx

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2BUTTON1, wxID_FRAME2LISTBOX1, wxID_FRAME2PANEL1, 
 wxID_FRAME2STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame2(wx.Frame):
    
    variables = ['a','b','c']
    
    
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(495, 183), size=wx.Size(1285, 653),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame2')
        self.SetClientSize(wx.Size(1285, 653))

        self.panel1 = wx.Panel(id=wxID_FRAME2PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1285, 653),
              style=wx.TAB_TRAVERSAL)

        self.listBox1 = wx.ListBox(choices=['self.variables'],
              id=wxID_FRAME2LISTBOX1, name='listBox1', parent=self.panel1,
              pos=wx.Point(80, 56), size=wx.Size(144, 280), style=0)
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox,
              id=wxID_FRAME2LISTBOX1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label='staticText1', name='staticText1', parent=self.panel1,
              pos=wx.Point(392, 136), size=wx.Size(69, 15), style=0)

        self.button1 = wx.Button(id=wxID_FRAME2BUTTON1, label='button1',
              name='button1', parent=self.panel1, pos=wx.Point(96, 360),
              size=wx.Size(85, 30), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME2BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnListBox1Listbox(self, event):
        print self.listBox1.Selection
        self.staticText1.Destroy()
        self.Refresh()
#        event.Skip()

    def OnButton1Button(self, event):
        #self.staticText1.Label = self.listBox1.Selection
        #self.Refresh()
        event.Skip()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
