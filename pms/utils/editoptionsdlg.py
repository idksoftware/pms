'''
Created on Mar 4, 2014

@author: wzw7yn
'''
import wx
import os.path
from xml.dom import minidom

from xml.parsers.expat import ExpatError
from xmlutils import XmlUtils
import xml.etree.ElementTree as ET

class OptionsDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self, title, xmlfile):
        wx.Dialog.__init__(self, None, -1, "Add Option", size=(600, 600))
        '''
        Constructor
        '''
        self.panel = OptionsPanel(self, title, xmlfile)
        sizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)

        sizer.Add(self.panel, 1, wx.EXPAND)
        sizer.Add(btnSizer, 0, wx.ALIGN_RIGHT | wx.ALL, 2)

        self.SetSizer(sizer)
        self.SetInitialSize()
        
    def Update(self):
        optlist = self.panel.listCtrl.GetItems()
        self.panel.cfg.write(optlist)

class OptionsPanel(wx.Panel):
    def __init__(self, parent, title, xmlfile):
        super(OptionsPanel, self).__init__(parent, style=wx.LB_BOTTOM)

        title_lbl= wx.StaticText(self, label=title)
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.cfg = OptionReader(xmlfile)
        
        #cfg.write("/home/wzw7yn/workspace/pms/main/test.xml")
        atList = self.cfg.read()
        newOptionLbl = wx.StaticText(self, -1, "Activity Type:")
        self.listCtrl = wx.ListBox(self, -1, (10, 30), (200, 120), atList, wx.LB_SINGLE | wx.LB_SORT)
        self.addButton = wx.Button(self, -1, "Add", size=(50, 23))
        self.editButton = wx.Button(self, -1, "Edit", size=(50, 23))
        self.deleteButton = wx.Button(self, -1, "Delete", size=(50, 23))

        btnSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer.Add(self.addButton)
        btnSizer.Add(self.editButton)
        btnSizer.Add(self.deleteButton)

        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(newOptionLbl, (1, 1))
        grpSizer.Add(self.listCtrl, (1, 2))
        grpSizer.Add(btnSizer, (1, 3))



        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)
        self.listCtrl.Bind(wx.EVT_LISTBOX_DCLICK , self.OnItemSelected)
        self.listCtrl.Bind(wx.EVT_LISTBOX , self.OnClicked)

        self.addButton.Bind(wx.EVT_BUTTON , self.OnAdd)
        self.editButton.Bind(wx.EVT_BUTTON , self.OnEdit)
        self.deleteButton.Bind(wx.EVT_BUTTON , self.OnDelete)

    def OnItemSelected(self, event):
        print "Here 1"

    def OnClicked(self, event):
        self.selection = self.listCtrl.GetSelection()

    def OnAdd(self, event):
        
        dialog = AddDialog("Add Option", None)
        if dialog.ShowModal() == wx.ID_OK:
            print dialog.GetOption()
            self.listCtrl.AppendAndEnsureVisible(dialog.GetOption())

    def OnEdit(self, event):
        self.selstr = self.listCtrl.GetStringSelection()

        dialog = AddDialog("Edit Option", self.selstr)
        if dialog.ShowModal() == wx.ID_OK:
            self.listCtrl.Delete(self.listCtrl.GetSelection())
            self.listCtrl.AppendAndEnsureVisible(dialog.GetOption())

    def OnDelete(self, event):
        pass
    
   

class AddDialog(wx.Dialog):
    '''
    classdocs
    '''


    def __init__(self, title, option):
        if option == None:
            caption = "Add Option"
        else:
            caption = "Edit Option"
        wx.Dialog.__init__(self, None, -1, caption, size=(600, 600))
        '''
        Constructor
        '''
        self.panel = AddPanel(self, title, caption, option)
        sizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)

        sizer.Add(self.panel, 1, wx.EXPAND)
        sizer.Add(btnSizer, 0, wx.ALIGN_RIGHT | wx.ALL, 2)

        self.SetSizer(sizer)
        self.SetInitialSize()
        
    def GetOption(self):
        return self.panel.GetOption()

class AddPanel(wx.Panel):
    def __init__(self, parent, title, caption, option):
        super(AddPanel, self).__init__(parent, style=wx.LB_BOTTOM)

        title_lbl= wx.StaticText(self, label=title)
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        
        newOptionLbl = wx.StaticText(self, -1, caption +":")
        if option == None:
            self.newOption = wx.TextCtrl(self, -1, "", size=(200, 23))
        else:
            self.newOption = wx.TextCtrl(self, -1, option, size=(200, 23))
        grpSizer = wx.GridBagSizer(vgap=8, hgap=8)

        grpSizer.Add(newOptionLbl, (1, 1))
        grpSizer.Add(self.newOption, (1, 2))

        mainSizer.Add(grpSizer, 0, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(mainSizer)

    def GetOption(self):
        return self.newOption.GetValue()

class OptionReader:
    
    def __init__(self, xmlfile):
        self.xmlfile = xmlfile
        self.opts = list()
        
    def read(self) :
        
        if os.path.exists(self.xmlfile) == False:
            return self.opts
        xmldoc = minidom.parse(self.xmlfile)
        options = xmldoc.getElementsByTagName("Item")
        if options == None:
            return -1;
        self.opts = list()
        for item in options:
            self.opts.append(item.childNodes[0].data)
        return self.opts
    
    def write(self, opts):
        rootEle = ET.Element("Options")
        
        for item in opts:
            itemEle = ET.SubElement(rootEle, "Item")
            itemEle.text = str(item)
        tree = ET.ElementTree(rootEle)
        ##ET.p  (tree, "<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        tree.write(self.xmlfile, "UTF-8") 
        
        
    def updateComboBox(self,ctrl):
        self.read()
        ctrl.Clear()
        for item in self.opts:
            ctrl.Append(item)
    





class TestApp(wx.App):
    def OnInit(self):
        dialog = OptionsDialog("test", "/home/wzw7yn/workspace/pms/main/options.xml")

        print "Opening Dialog"
        if dialog.ShowModal() == wx.ID_OK:
            dialog.Update()
        print "Closing CPDEditDialog"
        return True


if __name__=="__main__":
    #cfg = OptionReader()
    #cfg.read("/home/wzw7yn/workspace/pms/main/options.xml")
    #cfg.write("/home/wzw7yn/workspace/pms/main/test.xml")
    app = TestApp(False)
    app.MainLoop()
